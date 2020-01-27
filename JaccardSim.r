wd <- setwd("C:/Users/sa-meredith.bogacz/Desktop/LeadUF_Final")
# LeadUFCoach folder file path
LeadUFCoachPath <- paste(wd,"/LeadUF COACH Application/",sep = "")
#LeadUFParticipant folder file path
LeadUFParticipantPath <- paste(wd, "/LeadUF Participant Application/", sep = "")
#SelectText file path
SelectTextPath <- paste(wd, "/selecttext/", sep = "")

if(!("dplyr" %in% rownames(installed.packages()))) install.packages('dplyr')
if(!("stringr" %in% rownames(installed.packages()))) install.packages('stringr')
if(!("data.table" %in% rownames(installed.packages()))) install.packages('data.table')
if(!("tidyr" %in% rownames(installed.packages()))) install.packages('tidyr')
if(!("proxy" %in% rownames(installed.packages()))) install.packages('proxy')

library(dplyr)
library(stringr)
library(data.table)
library(tidyr)
library(proxy)

flsc <- list.files(LeadUFCoachPath, pattern = "^CoachS", full.names = TRUE, ignore.case = TRUE)
flsa <- list.files(LeadUFParticipantPath, pattern = "^AppSel", full.names = TRUE, ignore.case = TRUE)
file.copy(flsc, to = SelectTextPath, recursive = TRUE, overwrite = TRUE, copy.mode = TRUE, copy.date = FALSE)
file.copy(flsa, to = SelectTextPath, recursive = TRUE, overwrite = TRUE, copy.mode = TRUE, copy.date = FALSE)

setwd(SelectTextPath)
list.files(SelectTextPath)

text_f <- lapply(list.files(SelectTextPath), readLines) 

select_text  <- lapply( text_f, function(x)
{
  text <- gsub( "[[:punct:]]", "", x ) %>% tolower()
  text <- gsub( "\\s+", " ", text ) %>% str_trim()	
  word <- strsplit( text, " " ) %>% unlist()
  return(word)
})

## shingle function

Shingling <- function( document, k )
{
  shingles <- character( length = ( length(document) - k + 1 ) )
  
  for( i in 1:( length(document) - k + 1 ) )
    shingles[i] <- paste( document[ i:( i + k - 1 ) ], collapse = " " )
  
  return( unique(shingles) )
}


select_text_shingles3 <- lapply(select_text, function(x){
  Shingling( x, k = 3 )
})

select_text_shingles3[[1]]
#########################JACCARD SIMILARITY#################################
# unique sets on shingles across all documents

select_dict_k3 <-unlist(select_text_shingles3) %>% unique()
S3  <- lapply(select_text_shingles3, function( set, dict )
{
  as.integer( dict %in% set )
}, dict = select_dict_k3 ) %>% data.frame() 

# set the names for both rows and columns
setnames( S3,c("app_aleccarreche", "app_Kperez", "app_mbalta", "app_meredithbogacz", "app_nicholas0330", "app_omasih", "app_belinski", "app_mbogacz", "coach_kcounts", "coach_EGiles", "coach_Aafurh", "coach_Skennedy", "coach_Sforron", "coach_tsiler", "coach_hfarrell") )
rownames(S3) <- select_dict_k3
S3

# How similar is two given document, jaccard similarity 
JaccardSimilarity <- function( x, y )
{
  non_zero <- which( x | y )
  set_intersect <- sum( x[non_zero] & y[non_zero] )
  set_union <- length(non_zero)
  return( set_intersect / set_union ) 
}

# create a new entry in the registry
pr_DB$set_entry( FUN = JaccardSimilarity, names = c("JaccardSimilarity") )

# distance matrix 
select_match <- dist (t(S3), method ="JaccardSimilarity")

# delete entry
pr_DB$delete_entry( "JaccardSimilarity" )
select_match_k3 <- as.data.frame((as.matrix(select_match)))


# select the portions of the dataframe for analysis - matching only applicants with only coaches - edit the rows and columns according to the file

select_matches <-as.data.frame(select_match_k3[1:8, 9:15])

###############EXTRACT TOP 3 COACH MATCHES FOR EACH APPLICANT#######################

if(!("car" %in% rownames(installed.packages()))) install.packages('car')
library(car)
maxn <- function(n) function(x) order(x, decreasing = TRUE)[n]


sel_matches_max1 <- apply(select_matches, 1, maxn(1))
sel_matches_max2 <- apply(select_matches, 1, maxn(2))
sel_matches_max3 <- apply(select_matches, 1, maxn(3))


sel_matches_all <-as.data.frame(cbind(sel_matches_max1, sel_matches_max2, sel_matches_max3))


sel_matches_all <- apply(sel_matches_all, 2, function(x){x <- recode(x, "1='Kcounts'; 2='EGiles'; 3='AaFurh'; 4='SKennedy'; 5='SForron'; 6='HFarrell'"); x})


write.csv(sel_matches_all, file = "matches_based_on_selected_fields.csv")

```