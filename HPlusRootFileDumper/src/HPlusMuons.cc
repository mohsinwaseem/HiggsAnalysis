#include "HiggsAnalysis/HPlusRootFileDumper/interface/HPlusMuons.h"

#include <iostream>
#include <string>

#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/PatCandidates/interface/Muon.h"


HPlusMuons::HPlusMuons(const edm::ParameterSet& iConfig) :
HPlusAnalysis::HPlusAnalysisBase("Muons"),
HPlusAnalysis::HPlusSelectionBase(iConfig) {
  	// Parse the list of triggers in the config file
  	if (iConfig.exists("CollectionName")) {
    		fCollectionName = iConfig.getParameter<edm::InputTag>("CollectionName");
		vDiscriminators = iConfig.getParameter<std::vector<edm::InputTag> >("Discriminators");
  	} else {
    		throw cms::Exception("Configuration") 
                  << "Muons: InputTag 'CollectionName' is missing in config!" << std::endl;
  	}

  	// Initialize counters  
	fAll      = fCounter->addCounter("all");
	fSelected = fCounter->addCounter("selected");

  	// Declare produced items
        std::string name;
        std::string alias_prefix = iConfig.getParameter<std::string>("@module_label") + "_";

        name = "momentum";
        produces< std::vector<math::XYZVector> >(name).setBranchAlias(alias_prefix+name);
        name = "trackIso";
	produces< std::vector<float> >(name).setBranchAlias(alias_prefix+name);

	for(size_t i = 0; i < vDiscriminators.size(); ++i){
                name = vDiscriminators[i].label();
		produces< std::vector<float> >(name).setBranchAlias(alias_prefix+name);
	}
}

HPlusMuons::~HPlusMuons(){}

void HPlusMuons::beginJob(){}

void HPlusMuons::endJob(){}

bool HPlusMuons::filter(edm::Event& iEvent, const edm::EventSetup& iSetup) {

	fCounter->addCount(fAll);

	edm::Handle<edm::View<pat::Muon> > theHandle;
	iEvent.getByLabel(fCollectionName,theHandle);

        std::auto_ptr< std::vector<math::XYZVector> > momentum(new std::vector<math::XYZVector>);
	std::auto_ptr< std::vector<float> > trIsol(new std::vector<float>);
        for(edm::View<pat::Muon>::const_iterator i = theHandle->begin();
                                                i!= theHandle->end(); ++i){
                momentum->push_back(i->momentum());
		trIsol->push_back(i->trackIso());
	}
	iEvent.put(momentum, "momentum");
	iEvent.put(trIsol, "trackIso");	

	for(size_t ds = 0; ds < vDiscriminators.size(); ++ds){
                //std::cout << vDiscriminators[ds].label() << std::endl;
		std::auto_ptr< std::vector<float> > discr(new std::vector<float>);
		for(edm::View<pat::Muon>::const_iterator i = theHandle->begin();
                                                        i!= theHandle->end(); ++i){
			discr->push_back(i->muonID(vDiscriminators[ds].label()));
		}
		iEvent.put(discr,vDiscriminators[ds].label());
	}

	fCounter->addCount(fSelected);
	return 1;
}

DEFINE_FWK_MODULE(HPlusMuons);

