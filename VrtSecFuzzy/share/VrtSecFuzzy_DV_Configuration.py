# File for feeding Reco_tf.py vertexing options for the searches 
# looking for displaced vertices in the SUSY and Exotics groups.
# The options here are needed both when running on RAW and ESD inputs.
# Must run after the large-radius tracking to use large-d0 tracks.

## get a handle on the top sequence of algorithms -import AlgSequence
from AthenaCommon.AlgSequence import AlgSequence
topSequence = AlgSequence()

# instantiate the vertexing alg
from VrtSecFuzzy.VrtSecFuzzy import VrtSecFuzzy
VrtSecFuzzy_InDet = VrtSecFuzzy("VrtSecFuzzy_InDet")
VrtSecFuzzy_leptons  = VrtSecFuzzy("VrtSecFuzzy_leptons")

try:
    end_idx = [_.getName() for _ in topSequence].index('StreamESD')
except ValueError:
    try:
        end_idx = [_.getName() for _ in topSequence].index('StreamAOD')
    except ValueError:
        local_logger = logging.getLogger('VrtSecFuzzy_DV_Configuration')
        local_logger.warning('Neither StreamESD nor StreamAOD found, VrtSecFuzzy algs will be scheduled one before end of topSequence. Probably wrong!')
        end_idx = -1
        del local_logger
topSequence.insert(end_idx, VrtSecFuzzy_InDet)
#topSequence.insert(end_idx, VrtSecFuzzy_leptons)
del end_idx

# set options for vertexing
VrtSecFuzzy_InDet.do_PVvetoCut                           = True
VrtSecFuzzy_InDet.do_d0Cut                               = False
VrtSecFuzzy_InDet.do_z0Cut                               = False
VrtSecFuzzy_InDet.do_d0errCut                            = False
VrtSecFuzzy_InDet.do_z0errCut                            = False
VrtSecFuzzy_InDet.do_d0signifCut                         = False
VrtSecFuzzy_InDet.do_z0signifCut                         = False
VrtSecFuzzy_InDet.doTRTPixCut                            = True
VrtSecFuzzy_InDet.DoSAloneTRT                            = False
VrtSecFuzzy_InDet.ImpactWrtBL                            = True
VrtSecFuzzy_InDet.doPVcompatibilityCut                   = False # maybe default True  
VrtSecFuzzy_InDet.RemoveFake2TrkVrt                      = False # default True
VrtSecFuzzy_InDet.CheckHitPatternStrategy                = 'ExtrapolationAssist' # Either 'Classical', 'Extrapolation' or 'ExtrapolationAssist'
VrtSecFuzzy_InDet.doReassembleVertices                   = False #default True
VrtSecFuzzy_InDet.doMergeByShuffling                     = False #default True
VrtSecFuzzy_InDet.doMergeFinalVerticesDistance           = False #default True
VrtSecFuzzy_InDet.doAssociateNonSelectedTracks           = False #default True
VrtSecFuzzy_InDet.doFinalImproveChi2                     = False
VrtSecFuzzy_InDet.DoTruth                                = (globalflags.DataSource == 'geant4' and globalflags.InputFormat == "pool")
VrtSecFuzzy_InDet.FillHist                               = True
VrtSecFuzzy_InDet.FillIntermediateVertices               = True
VrtSecFuzzy_InDet.CutPixelHits                           = 0
VrtSecFuzzy_InDet.CutSctHits                             = 0 # default 2
VrtSecFuzzy_InDet.TrkA0ErrCut                            = 200000
VrtSecFuzzy_InDet.TrkZErrCut                             = 200000
VrtSecFuzzy_InDet.a0TrkPVDstMinCut                       = 0.0    # track d0 min: default is 2.0
VrtSecFuzzy_InDet.a0TrkPVDstMaxCut                       = 300.0  # track d0 max: default is 1000.0
VrtSecFuzzy_InDet.zTrkPVDstMinCut                        = 0.0    # track z0 min: default is 0.0, just for clarification
VrtSecFuzzy_InDet.zTrkPVDstMaxCut                        = 1500.0 # track z0 max: default is 1000.0
VrtSecFuzzy_InDet.twoTrkVtxFormingD0Cut                  = 0.0 # default 2.0
VrtSecFuzzy_InDet.TrkPtCut                               = 500 # default 1000
VrtSecFuzzy_InDet.SelVrtChi2Cut                          = 50. # default 5.0
VrtSecFuzzy_InDet.CutSharedHits                          = 2 
VrtSecFuzzy_InDet.TrkChi2Cut                             = 50
VrtSecFuzzy_InDet.TruthTrkLen                            = 1
VrtSecFuzzy_InDet.SelTrkMaxCutoff                        = 6000
VrtSecFuzzy_InDet.mergeByShufflingAllowance              = 10.
VrtSecFuzzy_InDet.associatePtCut                         = 1000.
VrtSecFuzzy_InDet.associateMinDistanceToPV               = 2.
VrtSecFuzzy_InDet.associateMaxD0Signif                   = 5.
VrtSecFuzzy_InDet.associateMaxZ0Signif                   = 5.
VrtSecFuzzy_InDet.MergeFinalVerticesDist                 = 1.
VrtSecFuzzy_InDet.MergeFinalVerticesScaling              = 0.
VrtSecFuzzy_InDet.improveChi2ProbThreshold               = 0.0001
VrtSecFuzzy_InDet.doAugmentDVimpactParametersToMuons     = True
VrtSecFuzzy_InDet.doAugmentDVimpactParametersToElectrons = True
VrtSecFuzzy_InDet.BDTFilesName                           = ["TMVAClassification_BDT.weights_1ns.root", "TMVAClassification_BDT.weights_p1ns.root", "TMVAClassification_BDT.weights_p01ns.root"]
VrtSecFuzzy_InDet.BDTMins                                = [-0.05, -0.05, -0.05]

VrtSecFuzzy_leptons.doSelectTracksFromMuons                = True
VrtSecFuzzy_leptons.doSelectTracksFromElectrons            = True
VrtSecFuzzy_leptons.AugmentingVersionString                = "_Leptons"
VrtSecFuzzy_leptons.do_PVvetoCut                           = True
VrtSecFuzzy_leptons.do_d0Cut                               = True
VrtSecFuzzy_leptons.do_z0Cut                               = False
VrtSecFuzzy_leptons.do_d0errCut                            = False
VrtSecFuzzy_leptons.do_z0errCut                            = False
VrtSecFuzzy_leptons.do_d0signifCut                         = False
VrtSecFuzzy_leptons.do_z0signifCut                         = False
VrtSecFuzzy_leptons.doTRTPixCut                            = False
VrtSecFuzzy_leptons.DoSAloneTRT                            = False
VrtSecFuzzy_leptons.ImpactWrtBL                            = False
VrtSecFuzzy_leptons.doPVcompatibilityCut                   = False
VrtSecFuzzy_leptons.RemoveFake2TrkVrt                      = True
VrtSecFuzzy_leptons.CheckHitPatternStrategy                = 'ExtrapolationAssist' # Either 'Classical', 'Extrapolation' or 'ExtrapolationAssist'
VrtSecFuzzy_leptons.doReassembleVertices                   = True
VrtSecFuzzy_leptons.doMergeByShuffling                     = True
VrtSecFuzzy_leptons.doMergeFinalVerticesDistance           = True
VrtSecFuzzy_leptons.doAssociateNonSelectedTracks           = False
VrtSecFuzzy_leptons.doFinalImproveChi2                     = False
VrtSecFuzzy_leptons.DoTruth                                = (globalflags.DataSource == 'geant4' and globalflags.InputFormat == "pool")
VrtSecFuzzy_leptons.FillHist                               = True
VrtSecFuzzy_leptons.FillIntermediateVertices               = False
VrtSecFuzzy_leptons.CutPixelHits                           = 0
VrtSecFuzzy_leptons.CutSctHits                             = 2
VrtSecFuzzy_leptons.TrkA0ErrCut                            = 200000
VrtSecFuzzy_leptons.TrkZErrCut                             = 200000
VrtSecFuzzy_leptons.a0TrkPVDstMinCut                       = 0.0    # track d0 min
VrtSecFuzzy_leptons.a0TrkPVDstMaxCut                       = 300.0  # track d0 max: default is 1000.0
VrtSecFuzzy_leptons.zTrkPVDstMinCut                        = 0.0    # track z0 min: default is 0.0, just for clarification
VrtSecFuzzy_leptons.zTrkPVDstMaxCut                        = 1500.0 # track z0 max: default is 1000.0
VrtSecFuzzy_leptons.twoTrkVtxFormingD0Cut                  = 0.0
VrtSecFuzzy_leptons.TrkPtCut                               = 1000
VrtSecFuzzy_leptons.SelVrtChi2Cut                          = 5.
VrtSecFuzzy_leptons.CutSharedHits                          = 2
VrtSecFuzzy_leptons.TrkChi2Cut                             = 50
VrtSecFuzzy_leptons.TruthTrkLen                            = 1
VrtSecFuzzy_leptons.SelTrkMaxCutoff                        = 2000
VrtSecFuzzy_leptons.mergeByShufflingAllowance              = 5.
VrtSecFuzzy_leptons.associatePtCut                         = 1000.
VrtSecFuzzy_leptons.MergeFinalVerticesDist                 = 1.
VrtSecFuzzy_leptons.MergeFinalVerticesScaling              = 0.
VrtSecFuzzy_leptons.improveChi2ProbThreshold               = 0.0001
VrtSecFuzzy_leptons.BDTFilesName                           = ["TMVAClassification_BDT.weights_1ns.root", "TMVAClassification_BDT.weights_p1ns.root", "TMVAClassification_BDT.weights_p01ns.root"]
VrtSecFuzzy_leptons.BDTMins                                = [0.2, 0.2, 0.2]

# set options related to the vertex fitter
from TrkVKalVrtFitter.TrkVKalVrtFitterConf import Trk__TrkVKalVrtFitter
FuzzyVxFitterTool = Trk__TrkVKalVrtFitter(name                = "FuzzyVxFitter",
                                              Extrapolator        = ToolSvc.AtlasExtrapolator,
                                              IterationNumber     = 30,
                                              AtlasMagFieldSvc    = "AtlasFieldSvc"
                                             )
ToolSvc +=  FuzzyVxFitterTool;
FuzzyVxFitterTool.OutputLevel = INFO

VrtSecFuzzy_InDet.VertexFitterTool=FuzzyVxFitterTool
VrtSecFuzzy_InDet.Extrapolator = ToolSvc.AtlasExtrapolator

VrtSecFuzzy_leptons.VertexFitterTool=FuzzyVxFitterTool
VrtSecFuzzy_leptons.Extrapolator = ToolSvc.AtlasExtrapolator

# tell VrtSecFuzzy the interface name for Trk::IVertexMapper
from TrkDetDescrTestTools.TrkDetDescrTestToolsConf import Trk__VertexMapper
HadronicVertexMapper = Trk__VertexMapper("HadronicVertexMapper")
ToolSvc += HadronicVertexMapper

VrtSecFuzzy_InDet.VertexMapper    = HadronicVertexMapper
VrtSecFuzzy_leptons.VertexMapper  = HadronicVertexMapper


include("VrtSecFuzzy/VrtSecFuzzy_DV_postInclude.py")
