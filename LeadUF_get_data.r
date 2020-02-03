install.packages("qualtRics")
registerOptions(api_token="API_TOKEN", root_url="root_URL")
readRenviron("~/.Renviron")
Sys.getenv("QUALTRICS_API_KEY")

library(qualtRics)

# Variables and File Paths

setwd("/LeadUF/2019-2020")
workingDirectory<-getwd()
LeadUFYearFolder <- gsub('/Analysis/',"",workingDirectory)

Data <- paste(LeadUFYearFolder, "/Data/", sep = "")
LeadUFCoachPath <- paste(Data,"/LeadUF COACH Application/",sep = "")
LeadUFParticipantPath <- paste(Data, "/LeadUF Participant Application/", sep = "")
SelectTextPath <- paste(LeadUFYearFolder, "/selecttext/", sep = "")


## Data
surveys <- getSurveys()
surveyName <- "LeadUF PARTICIPANT Application"
id <- surveys$id[surveys$name == surveyName] 
PartApplication <- fetch_survey(surveyID = id)

surveyName2 <- "LeadUF Confirmation Form"
id2 <- surveys$id[surveys$name == surveyName2]
PartPairing <- getSurvey(surveyID = id2)

surveyName3 <-"LeadUF COACH Application / Pairing"
id3 <- surveys$id[surveys$name == surveyName3]
CoachPairing <- getSurvey(surveyID = id3)


PartApplicationDate <- c(format(as.Date(PartApplication$EndDate, "%m/%d/%Y")))
PartPairingDate <- c(format(as.Date(PartPairing$EndDate, "%m/%d/%Y")))
CoachPairingDate <- c(format(as.Date(CoachPairing$EndDate, "%m/%d/%Y")))


write.csv(CoachPairing, paste(LeadUFCoachPath,'CoachPairing.csv', sep = ''))
write.csv(PartPairing, paste(LeadUFParticipantPath, 'PartPairing.csv', sep = ''))
write.csv(PartApplication, paste(Data, 'PartApplication.csv', sep = ''))


