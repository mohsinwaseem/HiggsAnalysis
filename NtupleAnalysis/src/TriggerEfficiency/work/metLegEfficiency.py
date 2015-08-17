#!/usr/bin/env python

from HiggsAnalysis.NtupleAnalysis.main import Process, PSet, Analyzer
from HiggsAnalysis.NtupleAnalysis.pileupWeight import pileupWeight

process = Process(outputPrefix="metLegEfficiency")

# Example of adding a dataset which has its files defined in data/<dataset_name>.txt file
#process.addDatasets(["TTbar_HBWB_HToTauNu_M_160_13TeV_pythia6"])

# Example of adding datasets from a multicrab directory
import sys
if len(sys.argv) != 2:
    print "Usage: ./exampleAnalysis.py <path-to-multicrab-directory>"
    sys.exit(0)
process.addDatasetsFromMulticrab(sys.argv[1])

leg     = "metlegSelection"
binning = [20, 30, 40, 50, 60, 70, 80, 100, 120, 140, 160, 180, 200]
xLabel  = "Type1 MET (GeV)"
yLabel  = "Level-1 + HLT MET efficiency"

## Example of adding an analyzer
#process.addAnalyzer("test", Analyzer("TriggerEfficiency",
#    offlineSelection = "metlegSelection",
#    binning = [20, 30, 40, 50, 60, 70, 80, 100, 120, 140, 160, 180, 200],
#    xLabel = "Type1 MET (GeV)",
#    yLabel = "Level-1 + HLT MET efficiency" 
#))

import HiggsAnalysis.HeavyChHiggsToTauNu.tools.aux as aux

def runRange(era):
    lumi   = 0
    runmin = 0
    runmax = 0
    if era == "2012ABCD":
        lumi   =  887.501000+4440.000000+6843.000000+281.454000+7318.000000
        runmin = 190456
        runmax = 208686

    if era == "2012D":
        lumi   = 7318
        runmin = 203777
        runmax = 208686

    if era == "2015A":
        lumi = 100
        runmin = 0
        runmax = 999999

    if lumi == 0:
        print "Unknown era",era,"exiting.."
        sys.exit()

    return lumi,runmin,runmax

def createAnalyzer(dataVersion,era,onlineSelection = "MET80"):
    useCaloMET = False
    if "CaloMET" in era:
        useCaloMET = True
        era = era[:-8]

    a = Analyzer("TriggerEfficiency",
        name = era,
        Trigger = PSet(
            triggerOR  = [],
            triggerOR2 = []
        ),
        PileupWeight = pileupWeight(enabled=False),
        onlineSelection = onlineSelection,
        offlineSelection = leg,
        TauSelection = PSet(
            discriminators = ["byLooseCombinedIsolationDeltaBetaCorr3Hits",
                             "againstMuonTight2",
                             "againstElectronMediumMVA5"],
        ),
        binning = binning,
        xLabel  = xLabel,
        yLabel  = yLabel,
    )

    if dataVersion.isData():
        a.Trigger.triggerOR = ["HLT_LooseIsoPFTau35_Trk20_Prong1_v2",
                               "HLT_LooseIsoPFTau35_Trk20_Prong1_v3",
                               "HLT_LooseIsoPFTau35_Trk20_Prong1_v4",
                               "HLT_LooseIsoPFTau35_Trk20_Prong1_v6",
                               "HLT_LooseIsoPFTau35_Trk20_Prong1_v7",
                               "HLT_LooseIsoPFTau35_Trk20_Prong1_v9",
                               "HLT_LooseIsoPFTau35_Trk20_Prong1_v10"]
        a.Trigger.triggerOR2 = ["HLT_LooseIsoPFTau35_Trk20_Prong1_MET70_v2",
                                "HLT_LooseIsoPFTau35_Trk20_Prong1_MET70_v3",
                                "HLT_LooseIsoPFTau35_Trk20_Prong1_MET70_v4",
                                "HLT_LooseIsoPFTau35_Trk20_Prong1_MET70_v6",
                                "HLT_LooseIsoPFTau35_Trk20_Prong1_MET70_v7",
                                "HLT_LooseIsoPFTau35_Trk20_Prong1_MET70_v9",
                                "HLT_LooseIsoPFTau35_Trk20_Prong1_MET70_v10"]
        if era == "2015A":
            a.Trigger.triggerOR = ["HLT_LooseIsoPFTau50_Trk30_eta2p1_v1"]
            a.Trigger.triggerOR2 = ["HLT_LooseIsoPFTau50_Trk30_eta2p1_"+onlineSelection+"_v1"]

        lumi,runmin,runmax = runRange(era)
        a.lumi    = lumi
        a.runMin  = runmin
        a.runMax  = runmax
    else:
        a.Trigger.triggerOR = ["HLT_LooseIsoPFTau35_Trk20_Prong1_v6"]
        a.Trigger.triggerOR2 = ["HLT_LooseIsoPFTau35_Trk20_Prong1_MET70_v6"]
        if era == "2015A":
            a.Trigger.triggerOR = ["HLT_LooseIsoPFTau50_Trk30_eta2p1_v1"]
            a.Trigger.triggerOR2 = ["HLT_LooseIsoPFTau50_Trk30_eta2p1_"+onlineSelection+"_v1"]

        a.PileupWeight = pileupWeight(
#            data = era,
            data = "2012ABCD", # FIXME
            mc   = "Summer12_S10" # FIXME
        )

    if useCaloMET:
        a.Trigger.triggerOR2 = []

    return a

def addAnalyzer(era,onlineSelection):
    dv = ["53Xdata22Jan2013","53mcS10"]
    if era == "2015A":
        dv = ["74Xdata","74Xmc"]
    process.addAnalyzer("METLeg_"+era+"_"+onlineSelection, lambda dv: createAnalyzer(dv, era, onlineSelection))

#addAnalyzer("2012ABCD")
#addAnalyzer("2012D")
#addAnalyzer("2012ABCD_CaloMET")
addAnalyzer("2015A","MET80")
addAnalyzer("2015A","MET120")
addAnalyzer("2015A_CaloMET","MET80")
addAnalyzer("2015A_CaloMET","MET120")

# Pick events
#process.addOptions(EventSaver = PSet(enabled = True, pickEvents = True))

# Run the analysis
process.run()

# Run the analysis with PROOF
# By default it uses all cores, but you can give proofWorkers=<N> as a parameter
#process.run(proof=True)
