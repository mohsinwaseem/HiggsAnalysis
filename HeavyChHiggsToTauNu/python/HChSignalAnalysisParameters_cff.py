import FWCore.ParameterSet.Config as cms

trigger = cms.untracked.PSet(
    src = cms.untracked.InputTag("patTriggerEvent"),
    trigger = cms.untracked.string("HLT_SingleLooseIsoTau20") # in 36X/35X MC and Run2010A data
#    trigger = cms.untracked.string("HLT_SingleIsoTau20_Trk5_MET20") # in 38X MC and Run2010B data
)

tauSelection = cms.untracked.PSet(
    #src = cms.untracked.InputTag("selectedPatTausCaloRecoTau"),
    #src = cms.untracked.InputTag("selectedPatTausFixedConePFTau"), # this doesn't exist in 38X samples
    src = cms.untracked.InputTag("selectedPatTausShrinkingConePFTau"),
    #src = cms.untracked.InputTag("selectedPatTausHpsPFTau"),
    ptCut = cms.untracked.double(40),
    etaCut = cms.untracked.double(2.4), #no change
    leadingTrackPtCut = cms.untracked.double(20),
    rtauCut = cms.untracked.double(0.8), #no change
    invMassCut = cms.untracked.double(1.5) #no change
)

jetSelection = cms.untracked.PSet(
    src = cms.untracked.InputTag("selectedPatJets"),
    #src = cms.untracked.InputTag("selectedPatJetsAK5JPT"),
    cleanTauDR = cms.untracked.double(0.5), #no change
    ptCut = cms.untracked.double(30),
    etaCut = cms.untracked.double(2.4), #no change
    minNumber = cms.untracked.uint32(4)
)

bTagging = cms.untracked.PSet(
    discriminator = cms.untracked.string("trackCountingHighEffBJetTags"),
    discriminatorCut = cms.untracked.double(1.5), #no change
    ptCut = cms.untracked.double(30), #no change
    etaCut = cms.untracked.double(1.5), #no change
    minNumber = cms.untracked.uint32(2)
)

MET = cms.untracked.PSet(
    #src = cms.untracked.InputTag("patMETs"), # calo MET
    src = cms.untracked.InputTag("patMETsPF"), # PF MET
    #src = cms.untracked.InputTag("patMETsTC"), # tc MET
    METCut = cms.untracked.double(60.0)
)
EvtTopology = cms.untracked.PSet(
    #discriminator = cms.untracked.string("test"),
    #discriminatorCut = cms.untracked.double(0.0),
    alphaT = cms.untracked.double(-2.0)
)
