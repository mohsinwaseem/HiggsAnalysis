#! /usr/bin/env python

import os
import sys
import imp
from optparse import OptionParser
import gc
import cPickle

import HiggsAnalysis.HeavyChHiggsToTauNu.datacardtools.MulticrabPathFinder as PathFinder
import HiggsAnalysis.HeavyChHiggsToTauNu.datacardtools.DataCardGenerator as DataCard
from HiggsAnalysis.HeavyChHiggsToTauNu.tools.aux import load_module


def main(opts):
    #gc.set_debug(gc.DEBUG_LEAK)
    #gc.set_debug(gc.DEBUG_STATS)
    print "Loading datacard:", opts.datacard
    config = load_module(opts.datacard)
    datacardgenerator = DataCard.DataCardGenerator(config,opts)

    #memoryDump()

def memoryDump():
    dump = open("memory_pickle.txt", 'w')
    for obj in gc.get_objects():
        i = id(obj)
        size = sys.getsizeof(obj, 0)
        #    referrers = [id(o) for o in gc.get_referrers(obj) if hasattr(o, '__class__')]
        referents = [id(o) for o in gc.get_referents(obj) if hasattr(o, '__class__')]
        if hasattr(obj, '__class__'):
            cls = str(obj.__class__)
            cPickle.dump({'id': i, 'class': cls, 'size': size, 'referents': referents}, dump)


if __name__ == "__main__":
    parser = OptionParser(usage="Usage: %prog [options]")
    parser.add_option("-x", "--datacard", dest="datacard", action="store", help="Name (incl. path) of the datacard to be used as an input")
    parser.add_option("--QCDfactorised", dest="useQCDfactorised", action="store_true", default=False, help="Use factorised method for QCD measurement")
    parser.add_option("--QCDinverted", dest="useQCDinverted", action="store_true", default=False, help="Use inverted method for QCD measurement")
    parser.add_option("--debugConfig", dest="debugConfig", action="store_true", default=False, help="Enable debugging print for config parsing")
    parser.add_option("--debugMining", dest="debugMining", action="store_true", default=False, help="Enable debugging print for data mining")
    parser.add_option("--debugQCD", dest="debugQCD", action="store_true", default=False, help="Enable debugging print for QCD measurement")
    (opts, args) = parser.parse_args()

    myStatus = True
    if opts.datacard == None:
        print "Error: Missing datacard!\n"
        myStatus = False
    if opts.useQCDfactorised and opts.useQCDinverted:
        print "Error: use either '--QCDfactorised' or '--QCDinverted' (only one can exist in the datacard)"
        myStatus = False
    if not myStatus:
        parser.print_help()
        sys.exit()

    # Run main program
    main(opts)
