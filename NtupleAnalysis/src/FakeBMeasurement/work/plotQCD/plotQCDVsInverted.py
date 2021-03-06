#!/usr/bin/env python
'''
This scipt creates all histograms for comparing 
QCD MC and Inverted distributions of key variables, like
the leading trijet mass, and its properties.

For the definition of the counter class see:
HiggsAnalysis/NtupleAnalysis/scripts

For more counter tricks and options see also:
HiggsAnalysis/NtupleAnalysis/scripts/hplusPrintCounters.py

Usage:
./plotQCDVsInverted.py -m <pseudo_mcrab_directory> [opts]

Examples:
/plotQCDVsInverted.py -m FakeBMeasurement_170619_020728_BJetsGE2_TopChiSqrVar_AllSamples/ -o OptChiSqrCutValue140 -e "QCD_HT50to100|QCD_HT100to200|QCD_HT200to300|QCD-b"
./plotQCDVsInverted.py -m FakeBMeasurement_170621_150419_BJetsGE2_TopChiSqrVar_AllSamples/ -e "QCD_HT50to100|QCD_HT100to200|QCD_HT200to300|Charged|QCD-b"
'''

#================================================================================================ 
# Imports
#================================================================================================ 
import sys
import math
import copy
import os
from optparse import OptionParser

import ROOT
ROOT.gROOT.SetBatch(True)
from ROOT import *

import HiggsAnalysis.NtupleAnalysis.tools.dataset as dataset
import HiggsAnalysis.NtupleAnalysis.tools.histograms as histograms
import HiggsAnalysis.NtupleAnalysis.tools.counter as counter
import HiggsAnalysis.NtupleAnalysis.tools.tdrstyle as tdrstyle
import HiggsAnalysis.NtupleAnalysis.tools.styles as styles
import HiggsAnalysis.NtupleAnalysis.tools.plots as plots
import HiggsAnalysis.NtupleAnalysis.tools.crosssection as xsect
import HiggsAnalysis.NtupleAnalysis.tools.multicrabConsistencyCheck as consistencyCheck

#================================================================================================ 
# Function Definition
#================================================================================================ 
def Print(msg, printHeader=False):
    fName = __file__.split("/")[-1]
    if printHeader==True:
        print "=== ", fName
        print "\t", msg
    else:
        print "\t", msg
    return


def Verbose(msg, printHeader=True, verbose=False):
    if not opts.verbose:
        return
    Print(msg, printHeader)
    return


def GetLumi(datasetsMgr):
    Verbose("Determininig Integrated Luminosity")
    
    lumi = 0.0
    for d in datasetsMgr.getAllDatasets():
        if d.isMC():
            continue
        else:
            lumi += d.getLuminosity()
    Verbose("Luminosity = %s (pb)" % (lumi), True)
    return lumi


def GetListOfEwkDatasets():
    Verbose("Getting list of EWK datasets")
    return ["TT", "WJetsToQQ_HT_600ToInf", "DYJetsToQQHT", "SingleTop", "TTWJetsToQQ", "TTZToQQ", "Diboson", "TTTT"]

def GetListOfQcdDatasets():
    Verbose("Getting list of QCD datasets")
    samples = ["QCD_HT50to100",
               "QCD_HT100to200",
               "QCD_HT200to300",
               "QCD_HT300to500",
               "QCD_HT500to700",
               "QCD_HT700to1000",
               "QCD_HT1000to1500",
               "QCD_HT1500to2000",
               "QCD_HT2000toInf"]
    return samples


def GetDatasetsFromDir(opts):
    Verbose("Getting datasets")
    
    if (not opts.includeOnlyTasks and not opts.excludeTasks):
        datasets = dataset.getDatasetsFromMulticrabDirs([opts.mcrab],
                                                        dataEra=opts.dataEra,
                                                        searchMode=opts.searchMode, 
                                                        analysisName=opts.analysisName,
                                                        optimizationMode=opts.optMode)
    elif (opts.includeOnlyTasks):
        datasets = dataset.getDatasetsFromMulticrabDirs([opts.mcrab],
                                                        dataEra=opts.dataEra,
                                                        searchMode=opts.searchMode,
                                                        analysisName=opts.analysisName,
                                                        includeOnlyTasks=opts.includeOnlyTasks,
                                                        optimizationMode=opts.optMode)
    elif (opts.excludeTasks):
        datasets = dataset.getDatasetsFromMulticrabDirs([opts.mcrab],
                                                        dataEra=opts.dataEra,
                                                        searchMode=opts.searchMode,
                                                        analysisName=opts.analysisName,
                                                        excludeTasks=opts.excludeTasks,
                                                        optimizationMode=opts.optMode)
    else:
        raise Exception("This should never be reached")
    return datasets
    

def main(opts):
    Verbose("main function")

    comparisonList = ["AfterStdSelections"]

    # Setup & configure the dataset manager 
    datasetsMgr = GetDatasetsFromDir(opts)
    datasetsMgr.updateNAllEventsToPUWeighted()
    datasetsMgr.loadLuminosities() # from lumi.json
    if opts.verbose:
        datasetsMgr.PrintCrossSections()
        datasetsMgr.PrintLuminosities()

    # Custom Filtering of datasets 
    if 1:
         datasetsMgr.remove(filter(lambda name: "HplusTB" in name and not "M_500" in name, datasetsMgr.getAllDatasetNames()))
               
    # Merge histograms (see NtupleAnalysis/python/tools/plots.py) 
    plots.mergeRenameReorderForDataMC(datasetsMgr)    
    datasetsMgr.PrintInfo()

    # Get Integrated Luminosity
    if opts.mcOnly:
        # Determine integrated lumi
        if opts.intLumi < 0.0:
            opts.intLumi = GetLumi(datasetsMgr)
        # Remove data datasets
        datasetsMgr.remove(filter(lambda name: "Data" in name, datasetsMgr.getAllDatasetNames()))

    # Re-order datasets (different for inverted than default=baseline)
    newOrder = ["Data"]
    newOrder.extend(GetListOfEwkDatasets())
    newOrder.extend(["QCD"]) #GetListOfQcdDatasets())
    if opts.mcOnly:
        newOrder.remove("Data")
    datasetsMgr.selectAndReorder(newOrder)

    # Set/Overwrite cross-sections
    for d in datasetsMgr.getAllDatasets():
        if "ChargedHiggs" in d.getName():
            datasetsMgr.getDataset(d.getName()).setCrossSection(1.0)

    # Merge EWK samples
    if opts.mergeEWK:
        datasetsMgr.merge("EWK", GetListOfEwkDatasets())
        plots._plotStyles["EWK"] = styles.getAltEWKStyle()

    # Print dataset information
    datasetsMgr.PrintInfo()

    # Apply TDR style
    style = tdrstyle.TDRStyle()
    style.setOptStat(True)

    # Do the Baseline Vs Inverted histograms
    if opts.mergeEWK:
        for hName in getTopSelectionHistos(opts.histoLevel):
            name = hName.split("/")[-1]
            #if hName.split("/")[-1] not in ["LdgTrijetMass_Before", "LdgTrijetMass_After"]:
            #continue
            if "mass" in name.lower():
                pass
            elif "pt" in name.lower():
                pass
            else:
                continue
            QCDVsInvertedComparison(datasetsMgr, name)
    else:
        Print("Cannot draw the Baseline Vs Inverted histograms without the option --mergeEWK. Exit", True)
    return


def getTopSelectionHistos(histoLevel="Vital", analysisType="Baseline"):
    '''
    Returns the list of histograms created by
    the TopSelection class
    '''
    
    Verbose("Creating histogram list for %s" % analysisType, True)

    # Entire list
    hList = [        
        "topSelection_%s/ChiSqr_Before" % (analysisType),
        "topSelection_%s/ChiSqr_After" % (analysisType),
        "topSelection_%s/NJetsUsedAsBJetsInFit_Before" % (analysisType),
        "topSelection_%s/NJetsUsedAsBJetsInFit_After" % (analysisType),
        "topSelection_%s/NumberOfFits_Before" % (analysisType),
        "topSelection_%s/NumberOfFits_After" % (analysisType),
        "topSelection_%s/TetrajetBJetPt_Before" % (analysisType),
        "topSelection_%s/TetrajetBJetPt_After" % (analysisType),
        "topSelection_%s/TetrajetBJetEta_Before" % (analysisType),
        "topSelection_%s/TetrajetBJetEta_After" % (analysisType),
        "topSelection_%s/TetrajetBJetBDisc_Before" % (analysisType),
        "topSelection_%s/TetrajetBJetBDisc_After" % (analysisType),
        "topSelection_%s/Tetrajet1Pt_Before" % (analysisType),
        "topSelection_%s/Tetrajet1Mass_Before" % (analysisType),
        "topSelection_%s/Tetrajet1Eta_Before" % (analysisType),
        "topSelection_%s/Tetrajet1Pt_After" % (analysisType),
        "topSelection_%s/Tetrajet1Mass_After" % (analysisType),
        "topSelection_%s/Tetrajet1Eta_After" % (analysisType),
        "topSelection_%s/Tetrajet2Pt_Before" % (analysisType),
        "topSelection_%s/Tetrajet2Mass_Before" % (analysisType),
        "topSelection_%s/Tetrajet2Eta_Before" % (analysisType),
        "topSelection_%s/Tetrajet2Pt_After" % (analysisType),
        "topSelection_%s/Tetrajet2Mass_After" % (analysisType),
        "topSelection_%s/Tetrajet2Eta_After" % (analysisType),
        "topSelection_%s/LdgTetrajetPt_Before" % (analysisType),
        "topSelection_%s/LdgTetrajetMass_Before" % (analysisType),
        "topSelection_%s/LdgTetrajetEta_Before" % (analysisType),
        "topSelection_%s/LdgTetrajetPt_After" % (analysisType),
        "topSelection_%s/LdgTetrajetMass_After" % (analysisType),
        "topSelection_%s/LdgTetrajetEta_After" % (analysisType),
        "topSelection_%s/SubldgTetrajetPt_Before" % (analysisType),
        "topSelection_%s/SubldgTetrajetMass_Before" % (analysisType),
        "topSelection_%s/SubldgTetrajetEta_Before" % (analysisType),
        "topSelection_%s/SubldgTetrajetPt_After" % (analysisType),
        "topSelection_%s/SubldgTetrajetMass_After" % (analysisType),
        "topSelection_%s/SubldgTetrajetEta_After" % (analysisType),
        "topSelection_%s/Trijet1Mass_Before" % (analysisType),
        "topSelection_%s/Trijet2Mass_Before" % (analysisType),
        "topSelection_%s/Trijet1Mass_After" % (analysisType),
        "topSelection_%s/Trijet2Mass_After" % (analysisType),
        "topSelection_%s/Trijet1Pt_Before" % (analysisType),
        "topSelection_%s/Trijet2Pt_Before" % (analysisType),
        "topSelection_%s/Trijet1Pt_After" % (analysisType),
        "topSelection_%s/Trijet2Pt_After" % (analysisType),
        "topSelection_%s/Trijet1DijetMass_Before" % (analysisType),
        "topSelection_%s/Trijet2DijetMass_Before" % (analysisType),
        "topSelection_%s/Trijet1DijetMass_After" % (analysisType),
        "topSelection_%s/Trijet2DijetMass_After" % (analysisType),
        "topSelection_%s/Trijet1DijetPt_Before" % (analysisType),
        "topSelection_%s/Trijet2DijetPt_Before" % (analysisType),
        "topSelection_%s/Trijet1DijetPt_After" % (analysisType),
        "topSelection_%s/Trijet2DijetPt_After" % (analysisType),
        "topSelection_%s/Trijet1DijetDEta_Before" % (analysisType),
        "topSelection_%s/Trijet2DijetDEta_Before" % (analysisType),
        "topSelection_%s/Trijet1DijetDEta_After" % (analysisType),
        "topSelection_%s/Trijet2DijetDEta_After" % (analysisType),
        "topSelection_%s/Trijet1DijetDPhi_Before" % (analysisType),
        "topSelection_%s/Trijet2DijetDPhi_Before" % (analysisType),
        "topSelection_%s/Trijet1DijetDPhi_After" % (analysisType),
        "topSelection_%s/Trijet2DijetDPhi_After" % (analysisType),
        "topSelection_%s/Trijet1DijetDR_Before" % (analysisType),
        "topSelection_%s/Trijet2DijetDR_Before" % (analysisType),
        "topSelection_%s/Trijet1DijetDR_After" % (analysisType),
        "topSelection_%s/Trijet2DijetDR_After" % (analysisType),
        "topSelection_%s/Trijet1DijetBJetDR_Before" % (analysisType),
        "topSelection_%s/Trijet2DijetBJetDR_Before" % (analysisType),
        "topSelection_%s/Trijet1DijetBJetDR_After" % (analysisType),
        "topSelection_%s/Trijet2DijetBJetDR_After" % (analysisType),
        "topSelection_%s/Trijet1DijetBJetDPhi_Before" % (analysisType),
        "topSelection_%s/Trijet2DijetBJetDPhi_Before" % (analysisType),
        "topSelection_%s/Trijet1DijetBJetDPhi_After" % (analysisType),
        "topSelection_%s/Trijet2DijetBJetDPhi_After" % (analysisType),
        "topSelection_%s/Trijet1DijetBJetDEta_Before" % (analysisType),
        "topSelection_%s/Trijet2DijetBJetDEta_Before" % (analysisType),
        "topSelection_%s/Trijet1DijetBJetDEta_After" % (analysisType),
        "topSelection_%s/Trijet2DijetBJetDEta_After" % (analysisType),
        "topSelection_%s/LdgTrijetPt_Before" % (analysisType),
        "topSelection_%s/LdgTrijetPt_After" % (analysisType),
        "topSelection_%s/LdgTrijetMass_Before" % (analysisType),
        "topSelection_%s/LdgTrijetMass_After" % (analysisType),
        "topSelection_%s/LdgTrijetJet1Pt_Before" % (analysisType),
        "topSelection_%s/LdgTrijetJet1Pt_After" % (analysisType),
        "topSelection_%s/LdgTrijetJet1Eta_Before" % (analysisType),
        "topSelection_%s/LdgTrijetJet1Eta_After" % (analysisType),
        "topSelection_%s/LdgTrijetJet1BDisc_Before" % (analysisType),
        "topSelection_%s/LdgTrijetJet1BDisc_After" % (analysisType),
        "topSelection_%s/LdgTrijetJet2Pt_Before" % (analysisType),
        "topSelection_%s/LdgTrijetJet2Pt_After" % (analysisType),
        "topSelection_%s/LdgTrijetJet2Eta_Before" % (analysisType),
        "topSelection_%s/LdgTrijetJet2Eta_After" % (analysisType),
        "topSelection_%s/LdgTrijetJet2BDisc_Before" % (analysisType),
        "topSelection_%s/LdgTrijetJet2BDisc_After" % (analysisType),
        "topSelection_%s/LdgTrijetBJetPt_Before" % (analysisType),
        "topSelection_%s/LdgTrijetBJetPt_After" % (analysisType),
        "topSelection_%s/LdgTrijetBJetEta_Before" % (analysisType),
        "topSelection_%s/LdgTrijetBJetEta_After" % (analysisType),
        "topSelection_%s/LdgTrijetBJetBDisc_Before" % (analysisType),
        "topSelection_%s/LdgTrijetBJetBDisc_After" % (analysisType),
        "topSelection_%s/LdgTrijetDiJetPt_Before" % (analysisType),
        "topSelection_%s/LdgTrijetDiJetPt_After" % (analysisType),
        "topSelection_%s/LdgTrijetDiJetEta_Before" % (analysisType),
        "topSelection_%s/LdgTrijetDiJetEta_After" % (analysisType),
        "topSelection_%s/LdgTrijetDiJetMass_Before" % (analysisType),
        "topSelection_%s/LdgTrijetDiJetMass_After" % (analysisType),
        "topSelection_%s/SubldgTrijetPt_Before" % (analysisType),
        "topSelection_%s/SubldgTrijetPt_After" % (analysisType),
        "topSelection_%s/SubldgTrijetMass_Before" % (analysisType),
        "topSelection_%s/SubldgTrijetMass_After" % (analysisType),
        "topSelection_%s/SubldgTrijetJet1Pt_Before" % (analysisType),
        "topSelection_%s/SubldgTrijetJet1Pt_After" % (analysisType),
        "topSelection_%s/SubldgTrijetJet1Eta_Before" % (analysisType),
        "topSelection_%s/SubldgTrijetJet1Eta_After" % (analysisType),
        "topSelection_%s/SubldgTrijetJet1BDisc_Before" % (analysisType),
        "topSelection_%s/SubldgTrijetJet1BDisc_After" % (analysisType),
        "topSelection_%s/SubldgTrijetJet2Pt_Before" % (analysisType),
        "topSelection_%s/SubldgTrijetJet2Pt_After" % (analysisType),
        "topSelection_%s/SubldgTrijetJet2Eta_Before" % (analysisType),
        "topSelection_%s/SubldgTrijetJet2Eta_After" % (analysisType),
        "topSelection_%s/SubldgTrijetJet2BDisc_Before" % (analysisType),
        "topSelection_%s/SubldgTrijetJet2BDisc_After" % (analysisType),
        "topSelection_%s/SubldgTrijetBJetPt_Before" % (analysisType),
        "topSelection_%s/SubldgTrijetBJetPt_After" % (analysisType),
        "topSelection_%s/SubldgTrijetBJetEta_Before" % (analysisType),
        "topSelection_%s/SubldgTrijetBJetEta_After" % (analysisType),
        "topSelection_%s/SubldgTrijetBJetBDisc_Before" % (analysisType),
        "topSelection_%s/SubldgTrijetBJetBDisc_After" % (analysisType),
        "topSelection_%s/SubldgTrijetDiJetPt_Before" % (analysisType),
        "topSelection_%s/SubldgTrijetDiJetPt_After" % (analysisType),
        "topSelection_%s/SubldgTrijetDiJetEta_Before" % (analysisType),
        "topSelection_%s/SubldgTrijetDiJetEta_After" % (analysisType),
        "topSelection_%s/SubldgTrijetDiJetMass_Before" % (analysisType),
        "topSelection_%s/SubldgTrijetDiJetMass_After" % (analysisType),
        # "topSelection_%s/Trijet1MassVsChiSqr_Before" % (analysisType),
        # "topSelection_%s/Trijet2MassVsChiSqr_Before" % (analysisType),
        # "topSelection_%s/Trijet1MassVsChiSqr_After" % (analysisType),
        # "topSelection_%s/Trijet2MassVsChiSqr_After" % (analysisType),
        # "topSelection_%s/Trijet1DijetPtVsDijetDR_Before" % (analysisType),
        # "topSelection_%s/Trijet2DijetPtVsDijetDR_Before" % (analysisType),
        # "topSelection_%s/Trijet1DijetPtVsDijetDR_After" % (analysisType),
        # "topSelection_%s/Trijet2DijetPtVsDijetDR_After" % (analysisType),
        ]

    hListFilter = []
    if histoLevel == "Vital":
        for h in hList:
            if any(substring in h for substring in ["Eta", "Dijet", "DiJet", "Fit", "Tetrajet1", "Tetrajet2"]):
                continue
            else:
                hListFilter.append(h)
    elif histoLevel == "Informative":
        for h in hList:
            if any(substring in h for substring in ["Eta", "Fit", "Tetrajet1", "Tetrajet2"]):
                continue
            else:
                hListFilter.append(h)
    elif histoLevel == "Debug":
        hListFilter = hList
    return hListFilter


def getHistos(datasetsMgr, datasetName, name1, name2):

    h1 = datasetsMgr.getDataset(datasetName).getDatasetRootHisto(name1)
    h1.setName("Baseline" + "-" + datasetName)

    h2 = datasetsMgr.getDataset(datasetName).getDatasetRootHisto(name2)
    h2.setName("Inverted" + "-" + datasetName)
    return [h1, h2]


def QCDVsInvertedComparison(datasetsMgr, histoName):
    
    p1 = plots.ComparisonPlot(*getHistos(datasetsMgr, "Data", "topSelection_Baseline/%s" % histoName, "topSelection_Inverted/%s" % histoName))
    p1.histoMgr.normalizeMCToLuminosity(datasetsMgr.getDataset("Data").getLuminosity())

    p2 = plots.ComparisonPlot(*getHistos(datasetsMgr, "EWK", "topSelection_Baseline/%s" % histoName, "topSelection_Inverted/%s" % histoName) )
    p2.histoMgr.normalizeMCToLuminosity(datasetsMgr.getDataset("Data").getLuminosity())

    p3 = plots.ComparisonPlot(*getHistos(datasetsMgr, "QCD", "topSelection_Baseline/%s" % histoName, "topSelection_Inverted/%s" % histoName))
    p3.histoMgr.normalizeMCToLuminosity(datasetsMgr.getDataset("Data").getLuminosity())

    # Get Data histos    
    baseline_Data = p1.histoMgr.getHisto("Baseline-Data").getRootHisto().Clone("Baseline-Data")
    inverted_Data = p1.histoMgr.getHisto("Inverted-Data").getRootHisto().Clone("Inverted-Data")

    # Get EWK histos
    baseline_EWK = p2.histoMgr.getHisto("Baseline-EWK").getRootHisto().Clone("Baseline-EWK")
    inverted_EWK = p2.histoMgr.getHisto("Inverted-EWK").getRootHisto().Clone("Inverted-EWK")

    # Get QCD (MC) Histos
    baseline_QCDMC = p3.histoMgr.getHisto("Baseline-QCD").getRootHisto().Clone("Baseline-QCDMC")
    inverted_QCDMC = p3.histoMgr.getHisto("Inverted-QCD").getRootHisto().Clone("Inverted-QCDMC")

    # Create QCD histos (QCD = Data-EWK)
    baseline_QCD = p1.histoMgr.getHisto("Baseline-Data").getRootHisto().Clone("Baseline-QCD")
    inverted_QCD = p1.histoMgr.getHisto("Inverted-Data").getRootHisto().Clone("Inverted-QCD")
    baseline_QCD.Add(baseline_EWK, -1)
    inverted_QCD.Add(inverted_EWK, -1)

    # Normalize histograms to unit area
    baseline_QCD.Scale(1.0/baseline_QCD.Integral())
    inverted_QCD.Scale(1.0/inverted_QCD.Integral())
    baseline_QCDMC.Scale(1.0/baseline_QCDMC.Integral())
    inverted_QCDMC.Scale(1.0/inverted_QCDMC.Integral())

    # Create the final plot object
    comparisonList = [baseline_QCDMC, inverted_QCD, inverted_QCDMC]
    p = plots.ComparisonManyPlot(baseline_QCD, comparisonList, saveFormats=[])
    p.setLuminosity(GetLumi(datasetsMgr))
        
    # Apply styles
    p.histoMgr.forHisto("Baseline-QCD"  , styles.getDataStyle() ) #getBaselineStyle()
    p.histoMgr.forHisto("Baseline-QCDMC", styles.getBaselineLineStyle() ) #getBaselineLineStyle()
    p.histoMgr.forHisto("Inverted-QCDMC", styles.getAltQCDStyle() ) #getQCDLineStyle
    p.histoMgr.forHisto("Inverted-QCD"  , styles.getInvertedStyle() )

    # Set draw style
    p.histoMgr.setHistoDrawStyle("Baseline-QCD", "P")
    p.histoMgr.setHistoLegendStyle("Baseline-QCD", "P")
    p.histoMgr.setHistoDrawStyle("Baseline-QCDMC", "HIST")
    p.histoMgr.setHistoLegendStyle("Baseline-QCDMC", "L")
    p.histoMgr.setHistoDrawStyle("Inverted-QCDMC", "HIST")
    p.histoMgr.setHistoLegendStyle("Inverted-QCDMC", "F")
    p.histoMgr.setHistoDrawStyle("Inverted-QCD", "P")
    p.histoMgr.setHistoLegendStyle("Inverted-QCD", "LP")
    # p.histoMgr.setHistoLegendStyleAll("LP")

    # Set legend labels
    p.histoMgr.setHistoLegendLabelMany({
            "Baseline-QCD"  : "Baseline (QCD)",
            "Baseline-QCDMC": "Baseline (QCD MC)",
            "Inverted-QCD"  : "Inverted (QCD)",
            "Inverted-QCDMC": "Inverted (QCD MC)",
            })

    # Draw the histograms
    _rebinX = 1
    _cutBox = None
    _opts   = {"ymin": 1e-6, "ymaxfactor": 2.0}

    if "Pt_" in histoName:
        _format = "%0.f GeV/c"
        _rebinX = 5
        if "tetrajet" in histoName.lower():
            _rebinX = 5
            
    if "ChiSqr" in histoName:
        _format = "%0.1f"
        _rebinX = 10
        if "After" in histoName:
            _rebinX = 1
            _opts["xmax"] = 20.0
    if "Mass" in histoName:
        _format = "%0.0f GeV/c^{2}"
        _rebinX = 5
        _cutBox = {"cutValue": 173.21, "fillColor": 16, "box": False, "line": True, "greaterThan": True}
        if "tetrajet" in histoName.lower():
            _rebinX = 10
            _opts["xmax"] = 3000.0
    if "BDisc" in histoName:
        _format = "%0.2f"
        _rebinX = 2
        _opts["xmax"] = 1.01
    if "Eta" in histoName:
        _format = "%0.2f"
    if "dijetmass" in histoName.lower():
        _cutBox = {"cutValue": 80.399, "fillColor": 16, "box": False, "line": True, "greaterThan": True}
    if "TetrajetMass" in histoName:
        _opts   = {"ymin": 8e-5, "ymaxfactor": 2.0, "xmax": 3000.0}
                
    plots.drawPlot(p, histoName,  
                   ylabel       = "Arbitrary Units / %s" % (_format),
                   log          = True, 
                   rebinX       = _rebinX, cmsExtraText = "Preliminary", 
                   createLegend = {"x1": 0.60, "y1": 0.75, "x2": 0.92, "y2": 0.92},
                   opts         = _opts,
                   opts2        = {"ymin": 0.6, "ymax": 1.4},
                   ratio        = True,
                   ratioInvert  = False, 
                   ratioYlabel  = "Ratio",
                   cutBox       = _cutBox,
                   )
    # Save plot in all formats
    SavePlot(p, histoName, os.path.join(opts.saveDir, "QCDVsInverted") ) 
    return


def IsBaselineOrInverted(analysisType):
    analysisTypes = ["Baseline", "Inverted"]
    if analysisType not in analysisTypes:
        raise Exception("Invalid analysis type \"%s\". Please select one of the following: %s" % (analysisType, "\"" + "\", \"".join(analysisTypes) + "\"") )
    else:
        pass
    return


def SavePlot(plot, plotName, saveDir, saveFormats = [".png", ".pdf"]):
    Verbose("Saving the plot in %s formats: %s" % (len(saveFormats), ", ".join(saveFormats) ) )

    # Create the name under which plot will be saved
    saveName = os.path.join(saveDir, plotName.replace("/", "_"))

    # For-loop: All save formats
    for i, ext in enumerate(saveFormats):
        saveNameURL = saveName + ext
        saveNameURL = saveNameURL.replace("/publicweb/a/aattikis/", "http://home.fnal.gov/~aattikis/")
        if opts.url:
            Print(saveNameURL, i==0)
        else:
            Print(saveName + ext, i==0)
        plot.saveAs(saveName, formats=saveFormats)
    return


#================================================================================================ 
# Main
#================================================================================================ 
if __name__ == "__main__":
    '''
    https://docs.python.org/3/library/argparse.html
 
    name or flags...: Either a name or a list of option strings, e.g. foo or -f, --foo.
    action..........: The basic type of action to be taken when this argument is encountered at the command line.
    nargs...........: The number of command-line arguments that should be consumed.
    const...........: A constant value required by some action and nargs selections.
    default.........: The value produced if the argument is absent from the command line.
    type............: The type to which the command-line argument should be converted.
    choices.........: A container of the allowable values for the argument.
    required........: Whether or not the command-line option may be omitted (optionals only).
    help............: A brief description of what the argument does.
    metavar.........: A name for the argument in usage messages.
    dest............: The name of the attribute to be added to the object returned by parse_args().
    '''
    
    # Default Settings
    ANALYSISNAME = "FakeBMeasurement"
    SEARCHMODE   = "80to1000"
    DATAERA      = "Run2016"
    OPTMODE      = ""#"OptChiSqrCutValue25"
    BATCHMODE    = True
    PRECISION    = 3
    INTLUMI      = -1.0
    SUBCOUNTERS  = False
    LATEX        = False
    MCONLY       = False
    MERGEEWK     = True
    URL          = False
    NOERROR      = True
    SAVEDIR      = "/publicweb/a/aattikis/FakeBMeasurement/"
    VERBOSE      = False
    HISTOLEVEL   = "Vital" # 'Vital' , 'Informative' , 'Debug'

    # Define the available script options
    parser = OptionParser(usage="Usage: %prog [options]")

    parser.add_option("-m", "--mcrab", dest="mcrab", action="store", 
                      help="Path to the multicrab directory for input")

    parser.add_option("-o", "--optMode", dest="optMode", type="string", default=OPTMODE, 
                      help="The optimization mode when analysis variation is enabled  [default: %s]" % OPTMODE)

    parser.add_option("-b", "--batchMode", dest="batchMode", action="store_false", default=BATCHMODE, 
                      help="Enables batch mode (canvas creation does NOT generate a window) [default: %s]" % BATCHMODE)

    parser.add_option("--analysisName", dest="analysisName", type="string", default=ANALYSISNAME,
                      help="Override default analysisName [default: %s]" % ANALYSISNAME)

    parser.add_option("--mcOnly", dest="mcOnly", action="store_true", default=MCONLY,
                      help="Plot only MC info [default: %s]" % MCONLY)

    parser.add_option("--intLumi", dest="intLumi", type=float, default=INTLUMI,
                      help="Override the integrated lumi [default: %s]" % INTLUMI)

    parser.add_option("--searchMode", dest="searchMode", type="string", default=SEARCHMODE,
                      help="Override default searchMode [default: %s]" % SEARCHMODE)

    parser.add_option("--dataEra", dest="dataEra", type="string", default=DATAERA, 
                      help="Override default dataEra [default: %s]" % DATAERA)

    parser.add_option("--mergeEWK", dest="mergeEWK", action="store_true", default=MERGEEWK, 
                      help="Merge all EWK samples into a single sample called \"EWK\" [default: %s]" % MERGEEWK)

    parser.add_option("--saveDir", dest="saveDir", type="string", default=SAVEDIR, 
                      help="Directory where all pltos will be saved [default: %s]" % SAVEDIR)

    parser.add_option("--url", dest="url", action="store_true", default=URL, 
                      help="Don't print the actual save path the histogram is saved, but print the URL instead [default: %s]" % URL)
    
    parser.add_option("-v", "--verbose", dest="verbose", action="store_true", default=VERBOSE, 
                      help="Enables verbose mode (for debugging purposes) [default: %s]" % VERBOSE)

    parser.add_option("--histoLevel", dest="histoLevel", action="store", default = HISTOLEVEL,
                      help="Histogram ambient level (default: %s)" % (HISTOLEVEL))

    parser.add_option("-i", "--includeOnlyTasks", dest="includeOnlyTasks", action="store", 
                      help="List of datasets in mcrab to include")

    parser.add_option("-e", "--excludeTasks", dest="excludeTasks", action="store", 
                      help="List of datasets in mcrab to exclude")

    (opts, parseArgs) = parser.parse_args()

    # Require at least two arguments (script-name, path to multicrab)
    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(1)

    if opts.mcrab == None:
        Print("Not enough arguments passed to script execution. Printing docstring & EXIT.")
        parser.print_help()
        #print __doc__
        sys.exit(1)

    # Call the main function
    main(opts)

    if not opts.batchMode:
        raw_input("=== plotHistograms.py: Press any key to quit ROOT ...")
