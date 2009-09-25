#include "HiggsAnalysis/HeavyChHiggsToTauNu/interface/MyEventConverter.h"
#include "HiggsAnalysis/HeavyChHiggsToTauNu/interface/VertexConverter.h"

void MyEventConverter::convert(const edm::Event& iEvent,const edm::EventSetup& iSetup){

	allEvents++;

//        tauMETTriggerAnalysis->analyse(iEvent);

//	if(!triggerDecision(iEvent)) return;
	triggeredEvents++;

        if(!primaryVertexFound(iEvent)) return;
	eventsWithPrimaryVertex++;

	getCaloHits(iEvent); // needed if calohits are to be stored
        getTracks(iEvent); // needed if tracks inside jet cones are to be stored
////	getTrajectories(iEvent); // needed if tracker hits are to be stored
        getEcalClusters(iEvent); // needed if ecal clusters for taus are to be stored

	MyEvent* saveEvent = new MyEvent;
	saveEvent->eventNumber          = iEvent.id().event();
	saveEvent->runNumber		= iEvent.run();
	saveEvent->lumiNumber		= iEvent.luminosityBlock();

	saveEvent->triggerResults       = getTriggerResults(iEvent);
	saveEvent->primaryVertex        = VertexConverter::convert(primaryVertex);
//	saveEvent->L1objects            = getL1objects(iEvent);
//	saveEvent->HLTobjects           = getHLTObjects(iEvent);

	saveEvent->addCollection("electrons",getElectrons(iEvent,iSetup));
//	saveEvent->photons              = getPhotons(iEvent);

	saveEvent->addCollection("muons",getMuons(iEvent));
	saveEvent->addCollection("calotaus",getTaus(iEvent));
	saveEvent->addCollection("fixedConePFTaus",getPFTaus(iEvent,"fixedConePFTauProducer"));
	saveEvent->addCollection("fixedConeHighEffPFTaus",getPFTaus(iEvent,"fixedConeHighEffPFTauProducer"));
        saveEvent->addCollection("shrinkingConePFTaus",getPFTaus(iEvent,"shrinkingConePFTauProducer"));
	saveEvent->addCollection("icone05jets",getJets(iEvent));

	saveEvent->mets			= getMET(iEvent);
//	saveEvent->addMET("pfMET",getPFMET(iEvent));
//	saveEvent->addMET("tcMET",getTCMET(iEvent));

        saveEvent->hasMCdata            = true;
        saveEvent->mcParticles          = getMCParticles(iEvent);
	saveEvent->mcMET                = getMCMET();
	saveEvent->mcPrimaryVertex      = getMCPrimaryVertex(iEvent);
        saveEvent->simTracks            = getSimTracks(iEvent,saveEvent);

	saveEvent->addCollection("removedMuons",getExtraObjects(iEvent));
////	saveEvent->addExtraObjects("",getExtraObjects(iEvent));

	userRootTree->fillTree(saveEvent);
	savedEvents++;

	delete saveEvent;

//	tauResolutionAnalysis->analyse(iEvent);
}
