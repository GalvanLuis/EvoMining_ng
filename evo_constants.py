#################################################################                        
               ############# DATA BASES #########
#################################################################
    
# Data bases of the precharged example:

#Enzime family DB:
EXMPL_CENTRAL_DB = ("/home/luisyovanny/.evo/dev_Evo/data/data_bases/example/central/")   

# Genome DB:
EXMPL_GENOMES_DB = ("/home/luisyovanny/.evo/dev_Evo/data/data_bases/example/genomes/los17/")

# Rast_ids file:
EXMPL_RAST_IDS = ("/home/luisyovanny/.evo/dev_Evo/data/data_bases/example/genomes/los17Rast.ids")

#Natural products DB(default =MIBiG):
MIBiG_NAT_PRODS_DB = ("/home/luisyovanny/.evo/dev_Evo/data/data_bases/example/mibig/")

##Dictionary with all the paths:
EXMPL_DB = { "central" : EXMPL_CENTRAL_DB,
            "genomes" : EXMPL_GENOMES_DB,
            "rast_ids" : EXMPL_RAST_IDS,
            "nat_prods" : MIBiG_NAT_PRODS_DB}


###################### Path to the genomesDB #######################
###################### in evomining format #########################


EVO_GENOMES_DB = "/home/luisyovanny/.evo/dev_Evo/data/data_bases/evo_genomes_db/"



###################################################################
                ############ Paths to auxiliary files ######
                ############ used by evomining ############
###################################################################


# This directory will contain the auxiliary files 
# to obtain the genomes .faa files with the evomining format:
        
GENOMES_EvoFmt = "/home/luisyovanny/.evo/dev_Evo/data/aux_data/genomes_EvoFmt/" 

## This directory will contain the auxiliary files
# to obtain the central_enzimes.txt and ids_to_names_of_orgs.txt files.

BBH_aux_files = "/home/luisyovanny/.evo/dev_Evo/data/aux_data/bbh_aux_files/"




EXPANDED_FAMS = "/home/luisyovanny/.evo/dev_Evo/data/data_bases/exp_fam/"




###################################################################
###################################################################     
#########################     BLAST     ###########################
###################################################################
###################################################################

## path to the command for makeblastdb:
MAKEBLASTDB_CMD = "/home/luisyovanny/ncbi-blast-2.13.0+/bin/makeblastdb"

## path to the command for blastp:
BLASTp_CMD = "/home/luisyovanny/ncbi-blast-2.13.0+/bin/blastp"


#################### blastdb's path #########################

BLASTDBs_PATH = "/home/luisyovanny/.evo/dev_Evo/data/data_bases/blast_dbs/"

#################### blastp's path #########################

BLASTp_PATH = "/home/luisyovanny/.evo/dev_Evo/data/data_bases/blastp/"






##################### The following are the columns names for ########
##################### the dataframes obtained from blastp ############

BLAST_COLS = ['query', 'subject','pc_identity', 'aln_length', 
              'mismatches', 'gaps_opened','query_start', 
              'query_end', 'subject_start', 'subject_end',
              'e_value', 'bitscore']




################################################################################
##############################  json files path   ###############################
################################################################################

JSON_FILES_PATH = "data/json_files/"

FAMILIES = "/home/luisyovanny/.evo/dev_Evo/data/json_files/families.json"
ORGS_IDS_NMS = "/home/luisyovanny/.evo/dev_Evo/data/json_files/orgs_ids_names.json"
EXP_FAMS_JSON = "/home/luisyovanny/.evo/dev_Evo/data/json_files/Dictio_expanded_fams.json"
BH_BCKWD = "/home/luisyovanny/.evo/dev_Evo/data/json_files/Dictio_bh_vuelta.json"
BBH = "/home/luisyovanny/.evo/dev_Evo/data/json_files/bbh.json"




#################### #################### #################### #################### ####################
#################### ####################       MUSCLE         #################### ####################
#################### #################### #################### #################### ####################

from Bio.Align.Applications import MuscleCommandline

MUSCLE_EXE = "/home/luisyovanny/muscle5.1.linux_intel64"

MUSCLE_OUTPUT = "/home/luisyovanny/.evo/dev_Evo/data/data_bases/tree_files/"

FastTree_EXE = "/home/luisyovanny/FastTree"

####################################################################################################
########################################    ETE   ##################################################

