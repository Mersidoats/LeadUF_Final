import os
import pandas as pd


def make_file_app(argv):
    counter = 0
    with open(argv, 'r') as f:
        for i in f:
            newfilename = 'AppSel_{0}'.format(str(counter))
            outfile = open(newfilename + '.txt', 'w')
            outfile.write(i)
            outfile.close()
            counter += 1


if __name__ == '__make_file_app__':
    make_file_app()


def make_file_coach(argv):
    counter = 0
    with open(argv, 'r') as f:
        for i in f:
            newfilename = 'CoachSel_{0}'.format(str(counter))
            outfile = open(newfilename + '.txt', 'w')
            outfile.write(i)
            outfile.close()
            counter += 1


if __name__ == '__make_file_Coach__':
    make_file_coach()


os.chdir('/LeadUF_Final/LeadUF COACH Application')

coachPairings = pd.read_csv('CoachPairing.csv', header=None, delimiter=',', encoding='ISO-8859-1')
CP_data = coachPairings.iloc[1:, ]
CP_Data_columns = coachPairings.iloc[0]
CP_data2 = CP_data.drop(CP_data.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 43, 44, 45]],
                         axis=1)

CP_data2.rename(columns={'Please enter your contact information below: - Title (Ms./Mrs./Mr./Dr.):': 'Prefix',
                         'Please enter your contact information below: - Last Name:': 'Lname',
                         'Please enter your contact information below: - First Name:': 'Fname',
                         'UFL email address: (Example: AlEGator@ufl.edu)': 'UFL email',
                         'Please select your affiliation with UF:': 'UF Affiliation',
                         'What unique perspectives or qualities would you bring to the LeadUF program?\n(1,'
                         '500 character limit)': 'Perspective',
                         'Which factors would you ideally like to have in common with your LeadUF Participants?('
                         'Maximum 2 choices)': 'MatchFactors',
                         'What are you currently involved with or do you have an interest in: \n(Select all that apply)': 'Interests',
                         'Please list the student organizations you currently advise:': 'Orgs Advised',
                         'Please list the organizations you currently volunteer with:': 'Volunteer',
                         'How do you identify?  \n(This could include but is not limited to gender identity, race, '
                         'ethnicity, first-generation college student, veteran, transfer student)': 'Identify Text',
                         'Please rank the following that best describes your mentorship style: \n(Most ideal = 1; '
                         'Least ideal = 4) - Cheerleader (Their biggest fan)': 'Cheerleader',
                         'Please rank the following that best describes your mentorship style: \n(Most ideal = 1; '
                         'Least ideal = 4) - Coach (Helps accomplish goals)': 'Coach',
                         'Please rank the following that best describes your mentorship style: \n(Most ideal = 1; '
                         'Least ideal = 4) - Counselor (Provides moral support)': 'Counselor',
                         'Please rank the following that best describes your mentorship style: \n(Most ideal = 1; '
                         'Least ideal = 4) - Teacher (Helps set plans for the future)': 'Teacher',
                         'For housing purposes, please let us know your gender identity: - Selected Choice': 'Gender '
                                                                                                             'Identity Select',
                         'For housing purposes, please let us know your gender identity: - Prefer to self describe: - '
                         'Text': 'Gender Identity Text',
                         'Do you have any special notes or accommodations?': 'Notes'}, inplace=True)

# strip newlines, replace punctuation with space
CP_data2.replace({r'[^\w\s]+': '', '\n': ' ', '"': ' ', ',': ' '}, regex=True, inplace=True)
CP_data2.replace({'Gender Identity Select': {'1': 'Female', '2': 'Male'}})  # recode gender identity
# recode numeric choices to text selects

CP_data2.replace(
    {'Cheerleader': {'1': 'Cheerleader_1', '2': 'Cheerleader_2', '3': 'Cheerleader_3', '4': 'Cheerleader_4'}},
    inplace=True)
CP_data2.replace({'Coach': {'1': 'Coach_1', '2': 'Coach_2', '3': 'Coach_3', '4': 'Coach_4'}}, inplace=True)
CP_data2.replace({'Counselor': {'1': 'Counselor_1', '2': 'Counselor_2', '3': 'Counselor_3', '4': 'Counselor_4'}},
                 inplace=True)
CP_data2.replace({'Teacher': {'1': 'Teacher_1', '2': 'Teacher_2', '3': 'Teacher_3', '4': 'Teacher_4'}}, inplace=True)
CP_data2['Selects'] = CP_data2[CP_data2.columns[0:]].apply(
    lambda x: ' '.join(x.dropna().astype(str)),
    axis=1
)


CP_data2 = CP_data2.drop(CP_data2.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
                                           22, 23, 24, 25, 26, 27, 28]], axis=1)
CP_data2.to_csv(r'/LeadUF_Final/LeadUF COACH Application/CP_data2.txt', header=False)
make_file_coach('CP_data2.txt')


os.chdir('/LeadUF_Final/LeadUF Participant Application')
ParticipantPairings = pd.read_csv('PartPairing.csv', header=None, delimiter=',', encoding="ISO-8859-1")
P_data = ParticipantPairings.iloc[1:, ]
P_Data_columns = ParticipantPairings.iloc[0]
P_data2 = P_data.drop(P_data.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 38, 39, 40]],
                       axis=1)
P_data2.rename(columns={'Tell us a little bit about yourself: - First Name:': 'Fname',
                         'Tell us a little bit about yourself: - Last Name:': 'Lname',
                         'UFL email address: (Example: AlEGator@ufl.edu)': 'UFL email',
                         'Which factors would you ideally like to have in common with your Leadership Coach?': 'MatchFactors',
                         'What are you currently involved with or do you have an interest in: \n(Select all that apply)': 'Interests',
                         'Please list the student organizations you are a member of currently:': 'Orgs Member',
                         'Please list the organizations you currently volunteer with:': 'Volunteer',
                         'How do you identify?  \n(This could include but is not limited to gender identity, race, '
                         'ethnicity, first-generation college student, veteran, transfer student)': 'Identify',
                         'In order of preference, please rank the following roles you would like your mentor to play: '
                         '\n(Most ideal = 1; Least ideal = 4) - Cheerleader (Your biggest fan)': 'Cheerleader',
                         'In order of preference, please rank the following roles you would like your mentor to play: '
                         '\n(Most ideal = 1; Least ideal = 4) - Coach (Helps you accomplish your goals)': 'Coach',
                         'In order of preference, please rank the following roles you would like your mentor to play: '
                         '\n(Most ideal = 1; Least ideal = 4) - Counselor (Provides moral support)': 'Counselor',
                         'In order of preference, please rank the following roles you would like your mentor to play: '
                         '\n(Most ideal = 1; Least ideal = 4) - Teacher (Helps you set plans for the future)':
                             'Teacher',
                         'For housing purposes, please let us know your gender identity: - Selected Choice': 'Gender '
                                                                                                             'Identity Select',
                         'For housing purposes, please let us know your gender identity: - Prefer to self describe: - '
                         'Text': 'Gender Identity Text',
                         'Do you have any special notes or accommodations?': 'Notes'}, inplace=True)
P_data2.replace({r'[^\w\s]+': '', '\n': ' ', '"': ' ', ',': ' '}, regex=True, inplace=True)
P_data2.replace({'Gender Identity Select': {'1': 'Female', '2': 'Male'}})  # recode gender identity
# recode numeric choices to text selects
P_data2.replace(
    {'Cheerleader': {'1': 'Cheerleader_1', '2': 'Cheerleader_2', '3': 'Cheerleader_3', '4': 'Cheerleader_4'}},
    inplace=True)
P_data2.replace({'Coach': {'1': 'Coach_1', '2': 'Coach_2', '3': 'Coach_3', '4': 'Coach_4'}}, inplace=True)
P_data2.replace({'Counselor': {'1': 'Counselor_1', '2': 'Counselor_2', '3': 'Counselor_3', '4': 'Counselor_4'}},
                inplace=True)
P_data2.replace({'Teacher': {'1': 'Teacher_1', '2': 'Teacher_2', '3': 'Teacher_3', '4': 'Teacher_4'}}, inplace=True)
P_data2['Selects'] = P_data2[P_data2.columns[0:]].apply(
    lambda x: ' '.join(x.dropna().astype(str)),
    axis=1
)
P_data2 = P_data2.drop(P_data2.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                                        20, 21, 22, 23]], axis=1)

P_data2.to_csv(r'/LeadUF_Final/LeadUF Participant Application/P_data2.txt', header=False)
make_file_app('P_data2.txt')
print("All done!")
