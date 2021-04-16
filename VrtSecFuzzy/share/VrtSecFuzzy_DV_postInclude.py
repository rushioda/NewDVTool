StreamESD.ItemList+=["xAOD::TrackParticleContainer#VrtSecFuzzy*"]
StreamESD.ItemList+=["xAOD::VertexContainer#VrtSecFuzzy*"]
StreamESD.ItemList+=["xAOD::VertexAuxContainer#VrtSecFuzzy*"]

# Monitoring histograms writing out
ServiceMgr += THistSvc()
ServiceMgr.THistSvc.Output = ["AANT DATAFILE='HIST.VrtSecFuzzy.root' OPT='RECREATE'"]

from AnalysisTools.AthAnalysisToolsConf import AANTupleStream
topSequence += AANTupleStream()
topSequence.AANTupleStream.ExtraRefNames = [ "StreamESD" ]
topSequence.AANTupleStream.OutputName = 'HIST.VrtSecFuzzy.root'
topSequence.AANTupleStream.WriteInputDataHeader = True
topSequence.AANTupleStream.OutputLevel = INFO


ToolSvc.EGammaAmbiguityTool.minNoSiHits = 2
ToolSvc.EGammaAmbiguityTool.minNoPixHits = 0
ToolSvc.MuonCombinedInDetDetailedTrackSelectorTool.IPd0Max = 9999.
ToolSvc.MuonCombinedInDetDetailedTrackSelectorTool.nHitPix = 0
ToolSvc.MuonCombinedInDetDetailedTrackSelectorTool.nHitSct = 2
ToolSvc.MuonCombinedInDetDetailedTrackSelectorTool.nHitSi = 2
ToolSvc.CaloTrkMuIdAlgTrackSelectorTool.IPd0Max = 9999.
ToolSvc.CaloTrkMuIdAlgTrackSelectorTool.nHitPix = 0
ToolSvc.CaloTrkMuIdAlgTrackSelectorTool.nHitSct = 2
ToolSvc.CaloTrkMuIdAlgTrackSelectorTool.nHitSi = 2
