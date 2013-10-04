# Description: Calculates QCD factorised result (works for both ABCD and traditional method)
# Makes also the shape histograms in phase space bins and the final shape
# Note: Systematic uncertainties need to be treated separately (since they should be taken from variation modules)
#
# Authors: LAW

from HiggsAnalysis.HeavyChHiggsToTauNu.tools.ShellStyles import *
import HiggsAnalysis.HeavyChHiggsToTauNu.tools.systematics as systematics
from HiggsAnalysis.HeavyChHiggsToTauNu.qcdCommon.dataDrivenQCDCount import *
from HiggsAnalysis.HeavyChHiggsToTauNu.tools.extendedCount import *
from HiggsAnalysis.HeavyChHiggsToTauNu.qcdCommon.systematicsForMetShapeDifference import *
from HiggsAnalysis.HeavyChHiggsToTauNu.tools.errorPropagation import *
import HiggsAnalysis.HeavyChHiggsToTauNu.tools.aux as aux
import math
import time

## Class for calculating the QCD factorised results
class QCDFactorisedResult:
    def __init__(self, basicShape, leg1Shape, leg2Shape, moduleInfoString, createBinHistos=False, displayPurityBreakdown=False):
        self._resultCountObject = None # ExtendedCount object which contains the result
        self._resultShape = None # TH1F which contains the final shape histogram
        self._nQCDHistogramsList = [] # List of TH1F histograms
        self._displayPurityBreakdown = displayPurityBreakdown
        self._createBinHistos = createBinHistos
        self._doCalculate(basicShape, leg1Shape, leg2Shape, moduleInfoString)

    ## Delete the histograms
    def delete(self):
        ROOT.gDirectory.Delete(self._resultShape.GetName())
        for h in self._nQCDHistogramsList:
            ROOT.gDirectory.Delete(h.GetName())
        self._nQCDHistogramsList = None

    ## Returns the ExtendedCountObject with the result
    def getResultCountObject(self):
        return self._resultCountObject

    ## Returns the final shape histogram
    def getResultShape(self):
        return self._resultShape

    ## Returns the list of shape histograms (one for each split phase space bin)
    def getNQCDHistograms(self):
        return self._nQCDHistogramsList

    ## Calculates the result
    def _doCalculate(self, basicShape, leg1Shape, leg2Shape, moduleInfoString):
        # Calculate final shape in signal region (leg1 * leg2 / basic)
        # Note that the calculation of the result is exactly the same for both the ABCD method and the traditional method
        nSplitBins = basicShape.getNumberOfPhaseSpaceSplitBins()
        # Initialize result containers
        self._resultShape = aux.Clone(leg1Shape.getDataDrivenQCDHistoForSplittedBin(0))
        self._resultShape.Reset()
        self._resultShape.SetTitle("NQCDFinal_Total_%s"%moduleInfoString)
        self._resultShape.SetName("NQCDFinal_Total_%s"%moduleInfoString)
        self._nQCDHistogramsList = []
        myUncertaintyLabels = ["statData", "statEWK"]
        self._resultCountObject = ExtendedCount(0.0, [0.0, 0.0], myUncertaintyLabels)
        if self._createBinHistos:
            for i in range(0, nSplitBins):
                hBin = aux.Clone(self._resultShape)
                hBin.SetTitle("NQCDFinal_%s_%s"%(basicShape.getPhaseSpaceBinFileFriendlyTitle(i).replace(" ",""), moduleInfoString))
                hBin.SetName("NQCDFinal_%s_%s"%(basicShape.getPhaseSpaceBinFileFriendlyTitle(i).replace(" ",""), moduleInfoString))
                self._nQCDHistogramsList.append(hBin)
        # Calculate efficiency
        myEfficiency = DataDrivenQCDEfficiency(numerator=leg2Shape, denominator=basicShape, histoSpecs=None)
        # Intialize counters for purity calculation in final shape binning
        myShapeDataSum = []
        myShapeDataSumUncert = []
        myShapeEwkSum = []
        myShapeEwkSumUncert = []
        for j in range(1,self._resultShape.GetNbinsX()+1):
            myShapeDataSum.append(0.0)
            myShapeDataSumUncert.append(0.0)
            myShapeEwkSum.append(0.0)
            myShapeEwkSumUncert.append(0.0)
        # Calculate results separately for each phase space bin and combine
        for i in range(0, nSplitBins):
            # Obtain efficiency for the split bin
            myEffObject = myEfficiency.getEfficiencyForSplitBin(i)
            # Get data-driven QCD, data, and MC EWK shape histogram for the phase space bin
            hLeg1 = leg1Shape.getDataDrivenQCDHistoForSplittedBin(i)
            hLeg1Data = leg1Shape.getDataHistoForSplittedBin(i)
            hLeg1Ewk = leg1Shape.getEwkHistoForSplittedBin(i)
            # Loop over bins in the shape histogram
            for j in range(1,hLeg1.GetNbinsX()+1):
                myResult = 0.0
                myStatDataUncert = 0.0
                myStatEwkUncert = 0.0
                if abs(hLeg1.GetBinContent(j)) > 0.00001: # Ignore zero bins
                    # Calculate result
                    myResult = abs(hLeg1.GetBinContent(j) * myEffObject.value())
                    # Treat negative numbers
                    if hLeg1.GetBinContent(j) < 0.0 or myEffObject.value() < 0.0:
                        myResult = -myResult;
                    # Calculate abs. stat. uncert. for data and for MC EWK
                    myStatDataUncert = errorPropagationForProduct(hLeg1.GetBinContent(j), hLeg1Data.GetBinError(j), myEffObject.value(), myEffObject.uncertainty("statData"))
                    myStatEwkUncert = errorPropagationForProduct(hLeg1.GetBinContent(j), hLeg1Ewk.GetBinError(j), myEffObject.value(), myEffObject.uncertainty("statEWK"))
                    # Do not calculate here MC EWK syst.
                myCountObject = ExtendedCount(myResult, [myStatDataUncert, myStatEwkUncert], myUncertaintyLabels)
                self._resultCountObject.add(myCountObject)
                if self._createBinHistos:
                    self._nQCDHistogramsList[i].SetBinContent(j, myCountObject.value())
                    self._nQCDHistogramsList[i].SetBinError(j, myCountObject.statUncertainty())
                self._resultShape.SetBinContent(j, self._resultShape.GetBinContent(j) + myCountObject.value())
                self._resultShape.SetBinError(j, self._resultShape.GetBinError(j) + myCountObject.statUncertainty()**2) # Sum squared
                # Sum items for purity calculation
                myShapeDataSum[j-1] += hLeg1Data.GetBinContent(j)*myEffObject.value()
                myShapeDataSumUncert[j-1] += errorPropagationForProduct(hLeg1Data.GetBinContent(j), hLeg1Data.GetBinError(j), myEffObject.value(), myEffObject.statUncertainty())**2
                myShapeEwkSum[j-1] += hLeg1Ewk.GetBinContent(j)*myEffObject.value()
                myShapeEwkSumUncert[j-1] += errorPropagationForProduct(hLeg1Ewk.GetBinContent(j), hLeg1Ewk.GetBinError(j), myEffObject.value(), myEffObject.statUncertainty())**2
            ROOT.gDirectory.Delete(hLeg1.GetName())
            ROOT.gDirectory.Delete(hLeg1Data.GetName())
            ROOT.gDirectory.Delete(hLeg1Ewk.GetName())
        # Take square root of uncertainties
        for j in range(1,self._resultShape.GetNbinsX()+1):
            self._resultShape.SetBinError(j, math.sqrt(self._resultShape.GetBinError(j)))
        # Print result
        print "NQCD = %s "%(self._resultCountObject.getResultStringFull("%.1f"))
        # Print purity as function of final shape bins
        if self._displayPurityBreakdown:
            print "Purity as function of final shape"
            print "shapeBin purity purityUncert"
            for j in range (1,hLeg1.GetNbinsX()+1):
                myPurity = 0.0
                myPurityUncert = 0.0
                if abs(myShapeDataSum[j-1]) > 0.000001:
                    myPurity = 1.0 - myShapeEwkSum[j-1] / myShapeDataSum[j-1]
                    myPurityUncert = errorPropagationForDivision(myShapeEwkSum[j-1], myShapeEwkSumUncert[j-1], myShapeDataSum[j-1], myShapeDataSumUncert[j-1])
                # Print purity info of final shape
                myString = ""
                if j < hLeg1.GetNbinsX():
                    myString = "%d..%d"%(hLeg1.GetXaxis().GetBinLowEdge(j),hLeg1.GetXaxis().GetBinUpEdge(j))
                else:
                    myString = ">%d"%(hLeg1.GetXaxis().GetBinLowEdge(j))
                myString += " %.3f %.3f"%(myPurity, myPurityUncert)
                print myString

class QCDControlPlot:
    def __init__(self, basicShape, leg1Shape, leg2Shape, moduleInfoString, title=""):
        self._resultShape = None # TH1F which contains the final shape histogram
        self._title = title
        if title == "":
            title = "NQCDCtrl_Total_%s"%moduleInfoString
        self._doCalculate(basicShape, leg1Shape, leg2Shape, moduleInfoString)

    def delete(self):
        ROOT.gDirectory.Delete(self._resultShape.GetName())

    ## Returns the final shape histogram
    def getResultShape(self):
        return self._resultShape

    ## Calculates the result
    def _doCalculate(self, basicShape, leg1Shape, leg2Shape, moduleInfoString):
        # Calculate final shape in signal region (leg1 * leg2 / basic)
        # Note that the calculation of the result is exactly the same for both the ABCD method and the traditional method
        nSplitBins = basicShape.getNumberOfPhaseSpaceSplitBins()
        # Initialize result containers
        self._resultShape = aux.Clone(leg1Shape.getDataHistoForSplittedBin(0))
        self._resultShape.Reset()
        self._resultShape.SetTitle(self._title+"tmp")
        self._resultShape.SetName(self._title+"tmp")
        ROOT.SetOwnership(self._resultShape, True)
        myUncertaintyLabels = ["statData", "statEWK"]
        self._resultCountObject = ExtendedCount(0.0, [0.0, 0.0], myUncertaintyLabels)
        # Calculate efficiency
        myEfficiency = DataDrivenQCDEfficiency(numerator=leg2Shape, denominator=basicShape, histoSpecs=None)
        # Calculate results separately for each phase space bin and combine
        for i in range(0, nSplitBins):
            # Obtain efficiency for the split bin
            myEffObject = myEfficiency.getEfficiencyForSplitBin(i)
            # Get data-driven QCD shape histogram for the phase space bin
            hLeg1 = leg1Shape.getDataDrivenQCDHistoForSplittedBin(i)
            ROOT.SetOwnership(hLeg1, True)
            # Loop over bins in the shape histogram
            for j in range(1,hLeg1.GetNbinsX()+1):
                myResult = 0.0
                myResultStatUncert = 0.0
                if abs(hLeg1.GetBinContent(j)) > 0.00001 and abs(myEffObject.value()) > 0.000001: # Ignore zero bins
                    # Calculate result
                    myResult = abs(hLeg1.GetBinContent(j) * myEffObject.value())
                    # Treat negative numbers
                    if hLeg1.GetBinContent(j) < 0.0 or myEffObject.value() < 0.0:
                        myResult = -myResult;
                    # Calculate abs. stat. uncert.
                    myResultStatUncert = errorPropagationForProduct(hLeg1.GetBinContent(j), hLeg1.GetBinError(j), myEffObject.value(), myEffObject.statUncertainty())
                    # Do not calculate here MC EWK syst.
                self._resultShape.SetBinContent(j, self._resultShape.GetBinContent(j) + myResult)
                self._resultShape.SetBinError(j, self._resultShape.GetBinError(j) + myResultStatUncert**2) # Sum squared
            ROOT.gDirectory.Delete(hLeg1.GetName())
        # Take square root of uncertainties
        for i in range(0,self._resultShape.GetNbinsX()+2):
            self._resultShape.SetBinError(i,math.sqrt(self._resultShape.GetBinError(i)))
        myEfficiency.delete()
        print "Control plots integral = %.1f"%self._resultShape.Integral()

class QCDFactorisedResultManager:
    def __init__(self, specs, dsetMgr, luminosity, moduleInfoString, shapeOnly=False, displayPurityBreakdown=False):
        print HighlightStyle()+"...Obtaining final shape"+NormalStyle()
        # Obtain QCD shapes
        myCtrlRegionShape = DataDrivenQCDShape(dsetMgr, "Data", "EWK", specs["basicName"], luminosity, rebinList=specs["binList"])
        myLeg1Shape = DataDrivenQCDShape(dsetMgr, "Data", "EWK", specs["leg1Name"], luminosity, rebinList=specs["binList"])
        mySignalRegionShape = DataDrivenQCDShape(dsetMgr, "Data", "EWK", specs["leg2Name"], luminosity, rebinList=specs["binList"])
        # Calculate final shape in signal region (leg1 * leg2 / basic)
        myResult = QCDFactorisedResult(myCtrlRegionShape, myLeg1Shape, mySignalRegionShape, moduleInfoString, displayPurityBreakdown=displayPurityBreakdown)
        myLeg1Shape.delete()
        self._hShape = aux.Clone(myResult.getResultShape())
        self._hShape.SetName(self._hShape.GetName()+"finalShapeInManager")
        myResult.delete()
        if not shapeOnly:
            print HighlightStyle()+"...Obtaining region transition systematics"+NormalStyle()
            # Do systematics coming from met shape difference
            myRegionTransitionSyst = SystematicsForMetShapeDifference(mySignalRegionShape, myCtrlRegionShape, self._hShape, moduleInfoString=moduleInfoString)
            self._hRegionSystUp = aux.Clone(myRegionTransitionSyst.getUpHistogram(), "QCDfactMgrQCDSystUp")
            self._hRegionSystDown = aux.Clone(myRegionTransitionSyst.getDownHistogram(), "QCDfactMgrQCDSystDown")
            myRegionTransitionSyst.delete()
            # Obtain data-driven control plots
            self._hCtrlPlotLabels = []
            self._hCtrlPlots = []
            self._hRegionSystUpCtrlPlots = []
            self._hRegionSystDownCtrlPlots = []
            myObjects = dsetMgr.getDataset("Data").getDirectoryContent("ForDataDrivenCtrlPlots")
            i = 0
            for item in myObjects:
                self._hCtrlPlotLabels.append(item)
                i += 1
                print HighlightStyle()+"...Obtaining ctrl plot %d/%d: %s%s"%(i,len(myObjects),item,NormalStyle())
                myRebinList = systematics.getBinningForPlot(item)
                myCtrlShape = DataDrivenQCDShape(dsetMgr, "Data", "EWK", "ForDataDrivenCtrlPlots/%s"%item, luminosity, rebinList=myRebinList)
                myCtrlPlot = QCDControlPlot(myCtrlRegionShape, myCtrlShape, mySignalRegionShape, moduleInfoString, title=item)
                myCtrlShape.delete()
                myCtrlPlotHisto = aux.Clone(myCtrlPlot.getResultShape(), "ctrlPlotShapeInManager")
                myCtrlPlot.delete()
                myCtrlPlotHisto.SetName(item+"%d"%i)
                myCtrlPlotHisto.SetTitle(item)
                self._hCtrlPlots.append(myCtrlPlotHisto)
                # Do systematics coming from met shape difference for control plots
                myCtrlPlotSignalRegionShape = DataDrivenQCDShape(dsetMgr, "Data", "EWK", "%s/%s"%("ForDataDrivenCtrlPlotsQCDNormalizationSignal",item), luminosity, rebinList=myRebinList)
                myCtrlPlotControlRegionShape = DataDrivenQCDShape(dsetMgr, "Data", "EWK", "%s/%s"%("ForDataDrivenCtrlPlotsQCDNormalizationControl",item), luminosity, rebinList=myRebinList)
                myCtrlPlotRegionTransitionSyst = SystematicsForMetShapeDifference(myCtrlPlotSignalRegionShape, myCtrlPlotControlRegionShape, myCtrlPlotHisto, moduleInfoString=moduleInfoString, quietMode=True)
                myCtrlPlotSignalRegionShape.delete()
                myCtrlPlotControlRegionShape.delete()
                hUp = aux.Clone(myCtrlPlotRegionTransitionSyst.getUpHistogram(), "QCDfactMgrSystQCDSystUp%d"%i)
                hUp.SetTitle(item)
                self._hRegionSystUpCtrlPlots.append(hUp)
                hDown = aux.Clone(myCtrlPlotRegionTransitionSyst.getDownHistogram(), "QCDfactMgrSystQCDSystDown%d"%i)
                hDown.SetTitle(item)
                self._hRegionSystDownCtrlPlots.append(hDown)
                myCtrlPlotRegionTransitionSyst.delete()
                #print "\n***** memdebug %d\n"%i
                #if i <= 2:
                #    ROOT.gDirectory.GetList().ls()
        myCtrlRegionShape.delete()
        mySignalRegionShape.delete()

    ## Delete the histograms
    def delete(self):
        ROOT.gDirectory.Delete(self._hShape.GetName())
        ROOT.gDirectory.Delete(self._hRegionSystDown.GetName())
        ROOT.gDirectory.Delete(self._hRegionSystUp.GetName())
        self._hCtrlPlotLabels = None
        for h in self._hCtrlPlots:
            ROOT.gDirectory.Delete(h.GetName())
        for h in self._hRegionSystUpCtrlPlots:
            ROOT.gDirectory.Delete(h.GetName())
        for h in self._hRegionSystDownCtrlPlots:
            ROOT.gDirectory.Delete(h.GetName())
        self._hCtrlPlots = None
        self._hRegionSystUpCtrlPlots = None
        self._hRegionSystDownCtrlPlots = None

    def getShape(self):
        return self._hShape

    def getRegionSystUp(self):
        return self._hRegionSystUp

    def getRegionSystDown(self):
        return self._hRegionSystDown

    def getControlPlotLabels(self):
        return self._hCtrlPlotLabels

    def getControlPlots(self):
        return self._hCtrlPlots

    def getRegionSystUpCtrlPlots(self):
        return self._hRegionSystUpCtrlPlots

    def getRegionSystDownCtrlPlots(self):
        return self._hRegionSystDownCtrlPlots
