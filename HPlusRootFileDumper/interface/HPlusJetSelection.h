#ifndef HPLUSANALYSISHPLUSJETSELECTION_H
#define HPLUSANALYSISHPLUSJETSELECTION_H

#include "HiggsAnalysis/HPlusRootFileDumper/interface/HPlusAnalysisBase.h"
#include "HiggsAnalysis/HPlusRootFileDumper/interface/HPlusSelectionBase.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"

#include "DataFormats/JetReco/interface/CaloJet.h"
#include <DataFormats/JetReco/interface/JPTJet.h>
#include "TH1F.h"

//*************************************************************************************************************
//   author     : Alexandros Attikis                                                                          *
//   date       : 07 June 2010                                                                                *
//   email      : attikis@cern.ch                                                                             *
//   Description: Class for jet selection: Loop over all jets in Evt, sort them by ascending order wrt their  *
//                Energy, apply selection cuts on their Jet Et, Eta and EMFraction. Return a boolean decision *
//                which is "true" iff there are "fCutMinNJets" jets in the Evt which satisfy the criteria.    *
//   info       : JPT are Jets made from CaloJets corrected for ZSP (Zero Suppression) and tracks.            *
//                JPTJet represents Jets made from CaloTowers and corrected for tracks in addition to generic *
//                Jet parameters it gives reference to the original jet, ZSP scale, associated tracks.        *
//*************************************************************************************************************

namespace HPlusAnalysis {
  
  class HPlusJetSelection : public HPlusAnalysis::HPlusAnalysisBase, public HPlusAnalysis::HPlusSelectionBase {
  public:
    
    /// Default constructor
    HPlusJetSelection(const edm::ParameterSet& iConfig);
    /// Default destructor
    ~HPlusJetSelection();
    
    void beginJob();
    void endJob();
    bool filter(edm::Event& iEvent, const edm::EventSetup& iSetup);
    //  Class-specific functions.
    bool doCaloJets(edm::Event& iEvent, const edm::EventSetup& iSetup);
    std::vector<reco::CaloJet> sortCaloJets(std::vector<reco::CaloJet> CaloJetsToSort, const size_t caloJetSize);
    std::vector<reco::CaloJet> filterCaloJets(std::vector<reco::CaloJet> caloJetsSorted, const size_t caloJetSize);
    std::vector<reco::CaloJet> eraseVectorElement( std::vector<reco::CaloJet> myJetVector, reco::CaloJet test);
    //
    bool doJPTJets(edm::Event& iEvent, const edm::EventSetup& iSetup);
    std::vector<reco::JPTJet> sortJPTJets(std::vector<reco::JPTJet> JPTJetsToSort, const size_t caloJetSize);
    std::vector<reco::JPTJet> filterJPTJets(std::vector<reco::JPTJet> JPTJetsSorted, const size_t caloJetSize);
    std::vector<reco::JPTJet> eraseVectorElement( std::vector<reco::JPTJet> myJetVector, reco::JPTJet test);

  private:
    // Cut values (their values taken from py cfg file)
    edm::InputTag fJetCollectionName; // Name of jet collection to be analyzed
    double fCutMinNJets;              // Min number of jets passing selection criteria on jet Et, Eta and EMFraction
    double fCutMinJetEt;              // One of the jet-selection criteria. Specifically the minimum jet Et
    double fCutMaxAbsJetEta;          // One of the jet-selection criteria. Specifically the maximum jet |Eta|
    double fCutMaxEMFraction;         // One of the jet-selection criteria. Specifically the maximum allowed EM energy fraction 
    // Counters
    int fCounterNEvts;                // Total Number of Evts processes (and for which the jet collection exists!)
    int fCounterNEvtsPassedSelection; // Number of Evts surviving the jet-selection cuts (passed through the config)
    int fCounterError;                // Random "errors" or "warnings" related to the coding of this specific class
    int fCounterJetsPriorSelection;   // Total number of selected jets present in data-sample (after selection cuts)
    int fCounterJetsPostSelection;    // Total number of jets present in data-sample (no selection cuts)
    int fCounterJetCollectionHandleEmpty; // Events whereby the jet collection handle was found to be empty!
    // other
    bool useCaloJets;
    bool useJPTJets;
    bool decision;
    // Validating Histograms
    TH1F* hLdgJetEt; /// LdgJet Et 
    TH1F* hSecondLdgJetEt; 
    TH1F* hThirdLdgJetEt; 
    TH1F* hFourthLdgJetEt; 
    TH1F* hFifthLdgJetEt; 
    TH1F* hLdgJetEta; /// LdgJet Eta
    TH1F* hSecondLdgJetEta;
    TH1F* hThirdLdgJetEta;
    TH1F* hFourthLdgJetEta;
    //  TH1F* hFifthLdgJetEta;
    
  };
  
}

#endif