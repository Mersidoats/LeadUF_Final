# LeadUF_Final
 LeadUF Jaccard Similarity Matrix
 
 This program was designed to take input data from a Qualtrics-based application and determine which coaches would be the best matches for the participants who applied to the program. It uses the Jaccard similiarity algorithm to match sets of text (called shingles) between the applicants and the coaches. It is currently being used by the LeadUF program at UFL. 
 
 The data in this set is strictly test data. In practice, I pull the data from qualtrics using the qualtRics package (ropensci/qualtRics).
 
 Run LeadUF_get_data.r to access data from Qualtrics.
 Run clean_csv.py to clean data files for aapplicants and coaches.
 Run JaccardSim.r to create a matrix of the top three coach matches for each applicant.
