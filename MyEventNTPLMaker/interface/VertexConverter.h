// -*- C++ -*-
#ifndef HiggsAnalysis_MyEventNTPLMaker_VertexConverter_h
#define HiggsAnalysis_MyEventNTPLMaker_VertexConverter_h

#include "HiggsAnalysis/MyEventNTPLMaker/interface/MyVertex.h"

#include<vector>

class TransientVertex;
namespace reco { 
  class Vertex;
  class TransientTrack;
}
namespace edm {
  class Event;
  class InputTag;
}

class VertexConverter {
public:
  static bool findPrimaryVertex(const edm::Event&, const edm::InputTag&, reco::Vertex*);

  static MyVertex convert(const reco::Vertex&);
  static MyVertex convert(const TransientVertex&);
  static void addSecondaryVertices(const std::vector<reco::TransientTrack>&, std::vector<MyVertex>&);

};

#endif