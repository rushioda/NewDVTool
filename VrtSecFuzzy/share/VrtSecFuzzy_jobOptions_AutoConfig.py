# This uses AutoConfiguration
# Vivek Jain - Mar 2010
# Modified: VJ, Dec 2011 - Use AthAlgorithm instead of CBNT_AthenaAwareBase


# to run on data at BNL may need to set HOTDISK externally

from AthenaCommon.AthenaCommonFlags import jobproperties as jp

#jp.AthenaCommonFlags.FilesInput = ['/usatlas/u/vj/vj_bnl_local/datafile/mc10_7TeV.105001.pythia_minbias.recon.AOD.e574_s932_s946_r1649_tid191045_00/AOD.191045._001937.pool.root.1']

#jp.AthenaCommonFlags.FilesInput = [ '/afs/cern.ch/atlas/maxidisk/d49/AOD.191045._001937.pool.root.1']
jp.AthenaCommonFlags.FilesInput = [
'/afs/cern.ch/work/v/vkost/vkdata/valid2.110401.PowhegPythia_P2012_ttbar_nonallhad.recon.AOD.e3099_s1982_s1964_r6024_tid04652558_00/AOD.04652558._000029.pool.root.1',
]
################################################################
# more single input files to test on
#
#jp.AthenaCommonFlags.FilesInput = [ '/usatlas/u/vj/MyTest/15.5.2/run/InDetRecAOD_new_Z400.root']
#
########## if running on multiple files
#
#DATAPATH = '/usatlas/u/vj/vj_bnl_local/datafile/mc10_7TeV.105001.pythia_minbias.recon.AOD.e574_s932_s946_r1649_tid191045_00/'

#from glob import glob
#INPUT = glob(DATAPATH + 'AOD*.root*')
##INPUT = glob(DATAPATH + 'ESD*.root*')
#print INPUT
#jp.AthenaCommonFlags.FilesInput = INPUT

# from david R.

from RecExConfig.RecFlags import rec

# get inputFileSummary - will use it to extract info for MC/DATA
from RecExConfig.InputFilePeeker import inputFileSummary

# import the data types 
import EventKernel.ParticleDataType

# get a handle on the ServiceManager which holds all the services
from AthenaCommon.AppMgr import ServiceMgr

include ("RecExCond/RecExCommon_flags.py")

include( "RecExCond/AllDet_detDescr.py" )
include( "AthenaPoolCnvSvc/ReadAthenaPool_jobOptions.py" )

from AthenaCommon.AppMgr import ToolSvc

from AthenaCommon.AlgSequence import AlgSequence 
topSequence = AlgSequence()

# write out a summary of the time spent
theApp.AuditAlgorithms=True
theAuditorSvc.Auditors  += [ "ChronoAuditor"]


#----------------------------------------------------------
#  VrtSecFuzzy creates also TrackSummary tool.
#   TrackSummary tool creates InDetExtrapolator and AtlasMagneticFieldTool
#
from VrtSecFuzzy.VrtSecFuzzy import VrtSecFuzzy
topSequence += VrtSecFuzzy()

#topSequence.VrtSecFuzzy.OutputLevel = DEBUG
topSequence.VrtSecFuzzy.OutputLevel = INFO
#topSequence.VrtSecFuzzy.CutBLayHits = 1
#topSequence.VrtSecFuzzy.CutPixelHits = 1
topSequence.VrtSecFuzzy.CutSctHits = 1
topSequence.VrtSecFuzzy.TrkA0ErrCut = 200000
topSequence.VrtSecFuzzy.TrkZErrCut = 200000
topSequence.VrtSecFuzzy.a0TrkPVDstMinCut = 5.0
topSequence.VrtSecFuzzy.TrkPtCut = 300
topSequence.VrtSecFuzzy.SelVrtChi2Cut=4.5
topSequence.VrtSecFuzzy.CutSharedHits=5
topSequence.VrtSecFuzzy.TrkChi2Cut=5.0
topSequence.VrtSecFuzzy.TruthTrkLen=1
topSequence.VrtSecFuzzy.DoSAloneTRT=False
topSequence.VrtSecFuzzy.DoTruth = False
# following is when there is no GEN_AOD in input file,
# e.g., when I run on output of InDetRecExample or on a ESD file
# when running on AOD output of InDetRecEx, explicitly uncomment the next line and comment out rec.readESD
#     topSequence.VrtSecFuzzy.MCEventContainer = "TruthEvent"

if rec.readESD():
    topSequence.VrtSecFuzzy.MCEventContainer = "TruthEvent"

if 'IS_SIMULATION' in inputFileSummary['evt_type']:
    topSequence.VrtSecFuzzy.DoTruth=True


from TrkVKalVrtFitter.TrkVKalVrtFitterConf import Trk__TrkVKalVrtFitter
FuzzyVxFitterTool = Trk__TrkVKalVrtFitter(name                = "FuzzyVxFitter",
	                                      Extrapolator        = ToolSvc.AtlasExtrapolator,
	                                      IterationNumber     = 30
					     )
ToolSvc +=  FuzzyVxFitterTool;
FuzzyVxFitterTool.OutputLevel = INFO
topSequence.VrtSecFuzzy.VertexFitterTool=FuzzyVxFitterTool
topSequence.VrtSecFuzzy.Extrapolator = ToolSvc.AtlasExtrapolator

print VrtSecFuzzy

# The input file
ServiceMgr.EventSelector.InputCollections = jp.AthenaCommonFlags.FilesInput()


##########################################
# setup TTree registration Service
# save ROOT histograms and NTuple
from GaudiSvc.GaudiSvcConf import THistSvc
ServiceMgr += THistSvc()
ServiceMgr.THistSvc.Output = ["AANT DATAFILE='vert.root' OPT='RECREATE'"]
#from AnalysisTools.AthAnalysisToolsConf import AANTupleStream
#topSequence += AANTupleStream()
#topSequence.AANTupleStream.ExtraRefNames = [ "StreamESD","Stream1" ]
#topSequence.AANTupleStream.OutputName = 'vert.root'
#topSequence.AANTupleStream.WriteInputDataHeader = True
#topSequence.AANTupleStream.OutputLevel = INFO

# Number of Events to process
theApp.EvtMax = -1
#theApp.EvtMax = 2
#ServiceMgr.EventSelector.SkipEvents = 2
ServiceMgr.MessageSvc.OutputLevel = INFO
ServiceMgr.MessageSvc.defaultLimit = 9999999 # all messages 

## uncomment following lines to dump truth info

#from TruthExamples.TruthExamplesConf import DumpMC
#topSequence += DumpMC()
# fix this by hand for running on AOD or ESD
#DumpMC.McEventKey = "GEN_AOD"
#DumpMC.McEventKey = "TruthEvent"
