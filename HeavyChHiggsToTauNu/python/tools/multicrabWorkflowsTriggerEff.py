## \package multicrabDatasetsTriggerEff
# Functions for trigger efficiency workflow definitions

from multicrabWorkflowsTools import Dataset, Workflow, Data, Source, updatePublishName, TaskDef, updateTaskDefinitions
from multicrabWorkflowsPattuple import constructProcessingWorkflow_53X

import multicrabDatasetsCommon as common

def addMetLegSkim_53X(version, datasets, updateDefinitions, skim=None):
    mcTriggerMETLeg = "HLT_LooseIsoPFTau35_Trk20_Prong1_v6"
    mcTriggers = [
        mcTriggerMETLeg,
        ]
    def TaskDefMC(**kwargs):
        return TaskDef(triggerOR=mcTriggers, **kwargs)

    defaultDefinitions = {                                                                                                                                             
        # njobsOut is just a guess                                                                                                                                     
        "Tau_190456-190738_2012A_Jul13":  TaskDef(njobsIn=  35, njobsOut=  1, triggerOR=["HLT_LooseIsoPFTau35_Trk20_Prong1_v2"]),
        "Tau_190782-190949_2012A_Aug06":  TaskDef(njobsIn=  10, njobsOut=  1, triggerOR=["HLT_LooseIsoPFTau35_Trk20_Prong1_v3"]),
        "Tau_191043-193621_2012A_Jul13":  TaskDef(njobsIn= 150, njobsOut=  3, triggerOR=[                                                                              
                                                      "HLT_LooseIsoPFTau35_Trk20_Prong1_v3", # 191043-191411                                                     
                                                      "HLT_LooseIsoPFTau35_Trk20_Prong1_v4", # 191691-191491 (193621)                                            
                                                  ], triggerThrow=False),                                                                                              
                                                                                                                                                                       
        "Tau_193834-196531_2012B_Jul13":  TaskDef(njobsIn=2000, njobsOut= 20, triggerOR=["HLT_LooseIsoPFTau35_Trk20_Prong1_v6"]),                                
        "Tau_198022-198523_2012C_Aug24":  TaskDef(njobsIn= 200, njobsOut=  2, triggerOR=["HLT_LooseIsoPFTau35_Trk20_Prong1_v7"]),                                
        # FIXME: the following three could be combined in the subsequent pattuple processings                                                                          
        "Tau_198941-200601_2012C_Prompt": TaskDef(njobsIn=1500, njobsOut= 10, triggerOR=[                                                                              
                                                     "HLT_LooseIsoPFTau35_Trk20_Prong1_v7",  # 198941-199608                                                     
                                                     "HLT_LooseIsoPFTau35_Trk20_Prong1_v9",  # 199698-200161                                                     
                                                 ], triggerThrow=False),                                                                                               
        "Tau_200961-202504_2012C_Prompt": TaskDef(njobsIn=1500, njobsOut= 12, triggerOR=["HLT_LooseIsoPFTau35_Trk20_Prong1_v9"]),
        "Tau_202792-203742_2012C_Prompt": TaskDef(njobsIn= 150, njobsOut=  1, triggerOR=["HLT_LooseIsoPFTau35_Trk20_Prong1_v10"]),
	"Tau_203777-208686_2012D_Prompt": TaskDef(njobsIn=3600, njobsOut= 360, triggerOR=["HLT_LooseIsoPFTau35_Trk20_Prong1_v10"]),
                                                                                                                                                                       
        "QCD_Pt30to50_TuneZ2star_Summer12":       TaskDefMC(njobsIn= 20, njobsOut=1),                                                                                  
        "QCD_Pt50to80_TuneZ2star_Summer12":       TaskDefMC(njobsIn= 20, njobsOut=1),                                                                                  
        "QCD_Pt80to120_TuneZ2star_Summer12":      TaskDefMC(njobsIn= 20, njobsOut=1),                                                                                  
        "QCD_Pt120to170_TuneZ2star_Summer12":     TaskDefMC(njobsIn= 40, njobsOut=1),                                                                                  
        "QCD_Pt170to300_TuneZ2star_Summer12":     TaskDefMC(njobsIn= 80, njobsOut=2),                                                                                  
        "QCD_Pt170to300_TuneZ2star_v2_Summer12":  TaskDefMC(njobsIn=300, njobsOut=6),                                                                                  
        "QCD_Pt300to470_TuneZ2star_Summer12":     TaskDefMC(njobsIn=250, njobsOut=4),                                                                                  
        "QCD_Pt300to470_TuneZ2star_v2_Summer12":  TaskDefMC(njobsIn=150, njobsOut=3),                                                                                  
        "QCD_Pt300to470_TuneZ2star_v3_Summer12":  TaskDefMC(njobsIn=850, njobsOut=14),                                                                                 
                                                                                                                                                                       
        "WW_TuneZ2star_Summer12":                 TaskDefMC(njobsIn=150, njobsOut= 8),                                                                                 
        "WZ_TuneZ2star_Summer12":                 TaskDefMC(njobsIn=150, njobsOut= 8),                                                                                 
        "ZZ_TuneZ2star_Summer12":                 TaskDefMC(njobsIn=150, njobsOut= 8),                                                                                 
        "TTJets_TuneZ2star_Summer12":             TaskDefMC(njobsIn=700, njobsOut=30),                                                                                 
        "WJets_TuneZ2star_v1_Summer12":           TaskDefMC(njobsIn=100, njobsOut= 4, args={"wjetsWeighting": 1, "wjetBin": -1}),                                      
        "WJets_TuneZ2star_v2_Summer12":           TaskDefMC(njobsIn=250, njobsOut= 8, args={"wjetsWeighting": 1, "wjetBin": -1}),                                      
        "W1Jets_TuneZ2star_Summer12":             TaskDefMC(njobsIn=150, njobsOut= 8, args={"wjetsWeighting": 1, "wjetBin": 1}),                                       
        "W2Jets_TuneZ2star_Summer12":             TaskDefMC(njobsIn=400, njobsOut=20, args={"wjetsWeighting": 1, "wjetBin": 2}),                                       
        "W3Jets_TuneZ2star_Summer12":             TaskDefMC(njobsIn=490, njobsOut=20, args={"wjetsWeighting": 1, "wjetBin": 3}),                                       
        "W4Jets_TuneZ2star_Summer12":             TaskDefMC(njobsIn=550, njobsOut=30, args={"wjetsWeighting": 1, "wjetBin": 4}),                                       
        "DYJetsToLL_M50_TuneZ2star_Summer12":     TaskDefMC(njobsIn=350, njobsOut= 6),                                                                                 
        "DYJetsToLL_M10to50_TuneZ2star_Summer12": TaskDefMC(njobsIn= 40, njobsOut= 1),                                                                                 
        "T_t-channel_TuneZ2star_Summer12":        TaskDefMC(njobsIn= 50, njobsOut= 2),                                                                                 
        "Tbar_t-channel_TuneZ2star_Summer12":     TaskDefMC(njobsIn= 50, njobsOut= 1),                                                                                 
        "T_tW-channel_TuneZ2star_Summer12":       TaskDefMC(njobsIn= 20, njobsOut= 2),                                                                                 
        "Tbar_tW-channel_TuneZ2star_Summer12":    TaskDefMC(njobsIn= 20, njobsOut= 2),                                                                                 
        "T_s-channel_TuneZ2star_Summer12":        TaskDefMC(njobsIn= 10, njobsOut= 1),                                                                                 
        "Tbar_s-channel_TuneZ2star_Summer12":     TaskDefMC(njobsIn= 10, njobsOut= 1),                                                                                 
        }

    workflowName = "triggerMetLeg_skim_"+version

    # Update the default definitions from the argument                                                                                                                 
    updateTaskDefinitions(defaultDefinitions, updateDefinitions)                                                                                                       
                                                                                                                                                                       
    # Add pattuple Workflow for each dataset                                                                                                                           
    for datasetName, taskDef in defaultDefinitions.iteritems():                                                                                                        
        dataset = datasets.getDataset(datasetName)                                                                                                                     
                                                                                                                                                                       
        # Construct processing workflow                                                                                                                                
        wf = constructProcessingWorkflow_53X(dataset, taskDef, sourceWorkflow="AOD", workflowName=workflowName, skimConfig=skim)

        # Setup the publish name                                                                                                                                       
        name = updatePublishName(dataset, wf.source.getDataForDataset(dataset).getDatasetPath(), "analysis_metleg_"+version)                                                  
        wf.addCrabLine("USER.publish_data_name = "+name)                                                                                                               
                                                                                                                                                                       
        # For MC, split by events, for data, split by lumi                                                                                                             
        if dataset.isMC():                                                                                                                                             
            wf.addCrabLine("CMSSW.total_number_of_events = -1")                                                                                                        
        else:                                                                                                                                                          
            wf.addCrabLine("CMSSW.total_number_of_lumis = -1")                                                                                                         
                                                                                                                                                                       
        # Add the pattuple Workflow to Dataset                                                                                                                         
        dataset.addWorkflow(wf)                                                                                                                                        
        # If DBS-dataset of the pattuple has been specified, add also analysis Workflow to Dataset                                                                     
        if wf.output != None:                                                                                                                                          
            commonArgs = {                                                                                                                                             
                "source": Source(workflowName),                                                                                                                 
                "args": wf.args,                                                                                                                                       
                "skimConfig": skim                                                                                                                                     
                }

            if dataset.isData():                                                                                                                                       
                # For data, construct one analysis workflow per trigger type                                                                                           
                pd = datasetName.split("_")[0]                                                                                                                         
                if pd == "Tau":                                                                                                                                        
                    dataset.addWorkflow(Workflow("triggerMetLeg_analysis_"+version, triggerOR=wf.triggerOR, **commonArgs))                                                    
                elif pd == "MultiJet":                                                                                                                                 
                    if datasetName in quadJetTriggers:                                                                                                                 
                        dataset.addWorkflow(Workflow("analysis_quadjet_"+version, triggerOR=quadJetTriggers[datasetName], **commonArgs))                               
                    if datasetName in quadJetBTagTriggers:                                                                                                             
                        dataset.addWorkflow(Workflow("analysis_quadjetbtag_"+version, triggerOR=quadJetBTagTriggers[datasetName], **commonArgs))                       
                    if datasetName in quadPFJetBTagTriggers:                                                                                                           
                        dataset.addWorkflow(Workflow("analysis_quadpfjetbtag_"+version, triggerOR=quadPFJetBTagTriggers[datasetName], **commonArgs))                   
                else:                                                                                                                                                  
                    raise Exception("Unsupported PD name %s" % pd)                                                                                                     
            else:                                                                                                                                                      
                # For MC, also construct one analysis workflow per trigger type                                                                                        
                dataset.addWorkflow(Workflow("triggerMetLeg_analysis_"+version, triggerOR=[mcTriggerMETLeg], **commonArgs))

def addMetLegSkim_53X_v1(datasets):
    definitions = {                                                                          
        "Tau_190456-190738_2012A_Jul13":          TaskDef(""),                               
        "Tau_190782-190949_2012A_Aug06":          TaskDef(""),                               
        "Tau_191043-193621_2012A_Jul13":          TaskDef(""),                               
        "Tau_193834-196531_2012B_Jul13":          TaskDef(""),                               
        "Tau_198022-198523_2012C_Aug24":          TaskDef(""),                               
        "Tau_198941-200601_2012C_Prompt":         TaskDef(""),                               
        "Tau_200961-202504_2012C_Prompt":         TaskDef(""),                               
        "Tau_202792-203742_2012C_Prompt":         TaskDef(""),
	"Tau_203777-208686_2012D_Prompt":	  TaskDef(""),

        "QCD_Pt30to50_TuneZ2star_Summer12":       TaskDef(""),                               
        "QCD_Pt50to80_TuneZ2star_Summer12":       TaskDef(""),                               
        "QCD_Pt80to120_TuneZ2star_Summer12":      TaskDef(""),                               
        "QCD_Pt120to170_TuneZ2star_Summer12":     TaskDef(""),                               
        "QCD_Pt170to300_TuneZ2star_Summer12":     TaskDef(""),                               
        "QCD_Pt170to300_TuneZ2star_v2_Summer12":  TaskDef(""),                               
        "QCD_Pt300to470_TuneZ2star_Summer12":     TaskDef(""),                               
        "QCD_Pt300to470_TuneZ2star_v2_Summer12":  TaskDef(""),                               
        "QCD_Pt300to470_TuneZ2star_v3_Summer12":  TaskDef(""),                               
                                                                                             
        "WW_TuneZ2star_Summer12":                 TaskDef(""),                               
        "WZ_TuneZ2star_Summer12":                 TaskDef(""),                               
        "ZZ_TuneZ2star_Summer12":                 TaskDef(""),                               
        "TTJets_TuneZ2star_Summer12":             TaskDef(""),                               
        "WJets_TuneZ2star_v1_Summer12":           TaskDef(""),                               
        "WJets_TuneZ2star_v2_Summer12":           TaskDef(""),                               
        "W1Jets_TuneZ2star_Summer12":             TaskDef(""),                               
        "W2Jets_TuneZ2star_Summer12":             TaskDef(""),                               
        "W3Jets_TuneZ2star_Summer12":             TaskDef(""),                               
        "W4Jets_TuneZ2star_Summer12":             TaskDef(""),                               
        "DYJetsToLL_M50_TuneZ2star_Summer12":     TaskDef(""),                               
        "DYJetsToLL_M10to50_TuneZ2star_Summer12": TaskDef(""),                               
        "T_t-channel_TuneZ2star_Summer12":        TaskDef(""),                               
        "Tbar_t-channel_TuneZ2star_Summer12":     TaskDef(""),                               
        "T_tW-channel_TuneZ2star_Summer12":       TaskDef(""),                               
        "Tbar_tW-channel_TuneZ2star_Summer12":    TaskDef(""),                               
        "T_s-channel_TuneZ2star_Summer12":        TaskDef(""),                               
        "Tbar_s-channel_TuneZ2star_Summer12":     TaskDef(""),                               
        }
                                                                                             
    addMetLegSkim_53X("v53_v1", datasets, definitions)                                        

def addMetLegSkim_44X(version, datasets, updateDefinitions):
    mcTrigger = "HLT_MediumIsoPFTau35_Trk20_v1"
    def TaskDefMC(**kwargs):
        return TaskDef(triggerOR=[mcTrigger], **kwargs)

    # The numbers of jobs are from multicrabDatasetsPattuple, they may have to be adjusted
    defaultDefinitions = {
        "Tau_165970-167913_2011A_Nov08": TaskDef(njobsIn=300, njobsOut=30, triggerOR=[
                                                    "HLT_IsoPFTau35_Trk20_v2", # 165970-166164, 166374-167043
                                                    "HLT_IsoPFTau35_Trk20_v3", # 166346-166346
                                                    "HLT_IsoPFTau35_Trk20_v4", # 167078-167913
                                                ], triggerThrow=False),
        "Tau_170722-173198_2011A_Nov08": TaskDef(njobsIn=70, njobsOut=30, triggerOR=["HLT_IsoPFTau35_Trk20_v6"]),
        "Tau_173236-173692_2011A_Nov08": TaskDef(njobsIn=30, njobsOut=30, triggerOR=["HLT_MediumIsoPFTau35_Trk20_v1"]),
        "Tau_175832-180252_2011B_Nov19": TaskDef(njobsIn=300, njobsOut=30, triggerOR=[
                                                    "HLT_MediumIsoPFTau35_Trk20_v1", #175832-178380
                                                    "HLT_MediumIsoPFTau35_Trk20_v5", #178420-179889
                                                    "HLT_MediumIsoPFTau35_Trk20_v6", #179959-180252
                                              ], triggerThrow=False),

        # MC, triggered with mcTrigger
        "QCD_Pt30to50_TuneZ2_Fall11":       TaskDefMC(njobsIn=10, njobsOut=1),
        "QCD_Pt50to80_TuneZ2_Fall11":       TaskDefMC(njobsIn=10, njobsOut=1),
        "QCD_Pt80to120_TuneZ2_Fall11":      TaskDefMC(njobsIn=10, njobsOut=10),
        "QCD_Pt120to170_TuneZ2_Fall11":     TaskDefMC(njobsIn=20, njobsOut=20),
        "QCD_Pt170to300_TuneZ2_Fall11":     TaskDefMC(njobsIn=40, njobsOut=4),
        "QCD_Pt300to470_TuneZ2_Fall11":     TaskDefMC(njobsIn=40, njobsOut=10),
                                            
        "WW_TuneZ2_Fall11":                 TaskDefMC(njobsIn=50, njobsOut=3),
        "WZ_TuneZ2_Fall11":                 TaskDefMC(njobsIn=50, njobsOut=3),
        "ZZ_TuneZ2_Fall11":                 TaskDefMC(njobsIn=50, njobsOut=3),
        "TTJets_TuneZ2_Fall11":             TaskDefMC(njobsIn=490, njobsOut=250),
        "WJets_TuneZ2_Fall11":              TaskDefMC(njobsIn=490, njobsOut=10),
        "W2Jets_TuneZ2_Fall11":             TaskDefMC(njobsIn=300, njobsOut=20),
        "W3Jets_TuneZ2_Fall11":             TaskDefMC(njobsIn=120, njobsOut=10),
        "W4Jets_TuneZ2_Fall11":             TaskDefMC(njobsIn=200, njobsOut=12),
        "DYJetsToLL_M50_TuneZ2_Fall11":     TaskDefMC(njobsIn=350, njobsOut=35),
        "DYJetsToLL_M10to50_TuneZ2_Fall11": TaskDefMC(njobsIn=300, njobsOut=10),
        "T_t-channel_TuneZ2_Fall11":        TaskDefMC(njobsIn=50, njobsOut=2),
        "Tbar_t-channel_TuneZ2_Fall11":     TaskDefMC(njobsIn=50, njobsOut=1),
        "T_tW-channel_TuneZ2_Fall11":       TaskDefMC(njobsIn=20, njobsOut=1),
        "Tbar_tW-channel_TuneZ2_Fall11":    TaskDefMC(njobsIn=20, njobsOut=1),
        "T_s-channel_TuneZ2_Fall11":        TaskDefMC(njobsIn=10, njobsOut=1),
        "Tbar_s-channel_TuneZ2_Fall11":     TaskDefMC(njobsIn=10, njobsOut=1),

        # Here is an example how to specity number of events/job
        # instead of number of jobs, and how to give dataset-specific
        # arbitrary crab configuration lines
        #"Tbar_s-channel_TuneZ2_Fall11":     TaskDefMC(neventsPerJobIn=10000, neventsPerJobOut=1000000, crabLines=["USER.user_remote_dir=/foo"]),
        }

    # Update the default definitions from the argument
    updateTaskDefinitions(defaultDefinitions, updateDefinitions, workflowName)

    # Add Workflow for each dataset
    for datasetName, taskDef in defaultDefinitions.iteritems():
        dataset = datasets.getDataset(datasetName)

        # Construct processing workflow
        wf = constructProcessingWorkflow_44X(dataset, taskDef, sourceWorkflow="AOD", workflowName=workflowName, inputLumiMaskData="Nov08ReReco", outputLumiMaskData=None)

        # Example of how to set user_remote_dir for this workflow only (but for all datasets)
        #wf.addCrabLine("USER.user_remote_dir = /whatever")

        dataset.addWorkflow(wf)

        # If have skim output, define the workflows which depend on it
        if wf.output != None:
	    wf.output.dbs_url = common.tteff_dbs
            dataset.addWorkflow(Workflow("triggerMetLeg_analysis_"+version, source=Source(workflowName),
                                         triggerOR=taskDef.triggerOR, args=wf.args, output_file="tteffAnalysis-metleg.root"))


def addMetLegSkim_cmssw44X_v1(datasets):
    definitions = {

        "Tau_165970-167913_2011A_Nov08":    TaskDef(""),
        "Tau_170722-173198_2011A_Nov08":    TaskDef(""),
        "Tau_173236-173692_2011A_Nov08":    TaskDef(""),
        "Tau_175832-180252_2011B_Nov19":    TaskDef(""),

        "QCD_Pt30to50_TuneZ2_Fall11":       TaskDef(""),
        "QCD_Pt50to80_TuneZ2_Fall11":       TaskDef(""),
        "QCD_Pt80to120_TuneZ2_Fall11":      TaskDef(""),
        "QCD_Pt120to170_TuneZ2_Fall11":     TaskDef(""),
        "QCD_Pt170to300_TuneZ2_Fall11":     TaskDef(""),
        "QCD_Pt300to470_TuneZ2_Fall11":     TaskDef(""),

        "WW_TuneZ2_Fall11":                 TaskDef(""),
        "WZ_TuneZ2_Fall11":                 TaskDef(""),
        "ZZ_TuneZ2_Fall11":                 TaskDef(""),
        "TTJets_TuneZ2_Fall11":             TaskDef(""),
        "WJets_TuneZ2_Fall11":              TaskDef(""),
        "W2Jets_TuneZ2_Fall11":             TaskDef(""),
        "W3Jets_TuneZ2_Fall11":             TaskDef(""),
        "W4Jets_TuneZ2_Fall11":             TaskDef(""),
        "DYJetsToLL_M50_TuneZ2_Fall11":     TaskDef(""),
        "DYJetsToLL_M10to50_TuneZ2_Fall11": TaskDef(""),
        "T_t-channel_TuneZ2_Fall11":        TaskDef(""),
        "Tbar_t-channel_TuneZ2_Fall11":     TaskDef(""),
        "T_tW-channel_TuneZ2_Fall11":       TaskDef(""),
        "Tbar_tW-channel_TuneZ2_Fall11":    TaskDef(""),
        "T_s-channel_TuneZ2_Fall11":        TaskDef(""),
        "Tbar_s-channel_TuneZ2_Fall11":     TaskDef(""),
        }

    addMetLegSkim_44X("cmssw44X_v1", datasets, definitions)
