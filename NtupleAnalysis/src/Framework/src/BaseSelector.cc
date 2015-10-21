#include "Framework/interface/BaseSelector.h"

BaseSelector::BaseSelector(const ParameterSet& config):
  fEvent(config),
  fEventCounter(fEventWeight),
  fHistoWrapper(fEventWeight, config.getParameter<std::string>("histogramAmbientLevel", "Vital")),
  fPileupWeight(config),
  fIsMC(config.isMC())
{}
BaseSelector::~BaseSelector() {
  fEventCounter.serialize();
}

void BaseSelector::processInternal(Long64_t entry) {
    fEventWeight.beginEvent();
    // Set event weight as negative is generator weight is negative
    if (fEvent.isMC()) {
      if (fEvent.genWeight().weight() < 0.0) {
        fEventWeight.multiplyWeight(-1.0);
      }
      //fEventWeight.multiplyWeight(fPileupWeight.getWeight(fEvent)); //FIXME: temporary disabled before MC pileup histograms is updated
    }
    // Set prescale event weight // FIXME missing code
    
    process(entry);
  }