# ########################################################################################################################
# # info: taskAccuracy
# ########################################################################################################################
# # Monthly evaluation of task performance for individual participant. Training effect plot shows change of pefromance over
# # the whole data collection period.


# ########################################################################################################################
# # Import necessary libraries and modules
# ########################################################################################################################
import os
import pandas as pd
import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=FutureWarning)


########################################################################################################################
# TaskAccuracy
########################################################################################################################
# Participant list

participant_dir = 'W:\\group_csp\\analyses\\oliver.frank\\Data\\'
participantList = os.listdir(participant_dir)

participant = participantList[2] # choose which particpant to analyze
month = '11' # choose which month to analyze

percentCorrect_DM, count_DM = 0, 0
percentCorrect_DM_Anti, count_DM_Anti = 0, 0
percentCorrect_EF, count_EF = 0, 0
percentCorrect_EF_Anti, count_EF_Anti = 0, 0
percentCorrect_RP, count_RP = 0, 0
percentCorrect_RP_Anti, count_RP_Anti = 0, 0
percentCorrect_RP_Ctx1, count_RP_Ctx1 = 0, 0
percentCorrect_RP_Ctx2, count_RP_Ctx2 = 0, 0
percentCorrect_WM, count_WM = 0, 0
percentCorrect_WM_Anti, count_WM_Anti = 0, 0
percentCorrect_WM_Ctx1, count_WM_Ctx1 = 0, 0
percentCorrect_WM_Ctx2, count_WM_Ctx2 = 0, 0

# co: Download data as .xlsx long format
list_testParticipant_month = os.listdir(os.path.join(participant_dir,participant,month))
for i in list_testParticipant_month:
    if i.split('.')[1] != 'png':
        currentFile = pd.read_excel(os.path.join(participant_dir,participant,month,i), engine='openpyxl')
        # print(currentFile['UTC Date and Time'])
        if currentFile['Task Name'][0] != '000_state_questions' and currentFile['Task Name'][0] != '000_session_completion': # avoid files with state questions and session completion
            # print(currentFile.iloc[0,28].split('_trials_')[0])
            # print('W:/AG_CSP/Projekte/beRNN_v1/02_Daten/BeRNN_main/' + participant + month + i)
            if currentFile['Spreadsheet'][0].split('_trials_')[0] == 'DM':
                # percentCorrect_DM += currentFile['Store: PercentCorrectDM'][len(currentFile['Store: PercentCorrectDM'])-3]
                # count_DM += 1

                filtered_rows = currentFile[currentFile['Event Index'] == 124].copy() # info: every now and then the 125th event is missing
                percentCorrect_DM += sum(filtered_rows['Store: PercentCorrectDM'])
                count_DM += len(filtered_rows)
                print('currentFile processed')

            if currentFile['Spreadsheet'][0].split('_trials_')[0] == 'DM_Anti':
                # percentCorrect_DM_Anti += currentFile['Store: PercentCorrectDMAnti'][len(currentFile['Store: PercentCorrectDMAnti'])-3]
                # count_DM_Anti += 1

                filtered_rows = currentFile[currentFile['Event Index'] == 124].copy()
                percentCorrect_DM_Anti += sum(filtered_rows['Store: PercentCorrectDMAnti'])
                count_DM_Anti += len(filtered_rows)
                print('currentFile processed')

            if currentFile['Spreadsheet'][0].split('_trials_')[0] == 'EF':
                # percentCorrect_EF += currentFile['Store: PercentCorrectEF'][len(currentFile['Store: PercentCorrectEF'])-3]
                # count_EF += 1

                filtered_rows = currentFile[currentFile['Event Index'] == 124].copy()
                percentCorrect_EF += sum(filtered_rows['Store: PercentCorrectEF'])
                count_EF += len(filtered_rows)
                print('currentFile processed')

            if currentFile['Spreadsheet'][0].split('_trials_')[0] == 'EF_Anti':
                # percentCorrect_EF_Anti += currentFile['Store: PercentCorrectEFAnti'][len(currentFile['Store: PercentCorrectEFAnti'])-3] # no extra displays for Anti were made
                # count_EF_Anti += 1

                filtered_rows = currentFile[currentFile['Event Index'] == 124].copy()
                percentCorrect_EF_Anti += sum(filtered_rows['Store: PercentCorrectEFAnti'])
                count_EF_Anti += len(filtered_rows)
                print('currentFile processed')

            if currentFile['Spreadsheet'][0].split('_trials_')[0] == 'RP':
                # percentCorrect_RP += currentFile['Store: PercentCorrectRP'][len(currentFile['Store: PercentCorrectRP'])-3]
                # count_RP += 1

                filtered_rows = currentFile[currentFile['Event Index'] == 124].copy()
                percentCorrect_RP += sum(filtered_rows['Store: PercentCorrectRP'])
                count_RP += len(filtered_rows)
                print('currentFile processed')

            if currentFile['Spreadsheet'][0].split('_trials_')[0] == 'RP_Anti':
                # percentCorrect_RP_Anti += currentFile['Store: PercentCorrectRPAnti'][len(currentFile['Store: PercentCorrectRPAnti'])-3]
                # count_RP_Anti += 1

                filtered_rows = currentFile[currentFile['Event Index'] == 124].copy()
                percentCorrect_RP_Anti += sum(filtered_rows['Store: PercentCorrectRPAnti'])
                count_RP_Anti += len(filtered_rows)
                print('currentFile processed')

            if currentFile['Spreadsheet'][0].split('_trials_')[0] == 'RP_Ctx1':
                # percentCorrect_RP_Ctx1 += currentFile['Store: PercentCorrectRPCtx1'][len(currentFile['Store: PercentCorrectRPCtx1'])-3]
                # count_RP_Ctx1 += 1

                filtered_rows = currentFile[currentFile['Event Index'] == 125].copy()
                percentCorrect_RP_Ctx1 += sum(filtered_rows['Store: PercentCorrectRPCtx1'])
                count_RP_Ctx1 += len(filtered_rows)
                print('currentFile processed')

            if currentFile['Spreadsheet'][0].split('_trials_')[0] == 'RP_Ctx2':
                # percentCorrect_RP_Ctx2 += currentFile['Store: PercentCorrectRPCtx2'][len(currentFile['Store: PercentCorrectRPCtx2'])-3]
                # count_RP_Ctx2 += 1

                filtered_rows = currentFile[currentFile['Event Index'] == 124].copy()
                percentCorrect_RP_Ctx2 += sum(filtered_rows['Store: PercentCorrectRPCtx2'])
                count_RP_Ctx2 += len(filtered_rows)
                print('currentFile processed')

            if currentFile['Spreadsheet'][0].split('_trials_')[0] == 'WM':
                # percentCorrect_WM += currentFile['Store: PercentCorrectWM'][len(currentFile['Store: PercentCorrectWM'])-3]
                # count_WM += 1

                filtered_rows = currentFile[currentFile['Event Index'] == 124].copy()
                percentCorrect_WM += sum(filtered_rows['Store: PercentCorrectWM'])
                count_WM += len(filtered_rows)
                print('currentFile processed')

            if currentFile['Spreadsheet'][0].split('_trials_')[0] == 'WM_Anti':
                # percentCorrect_WM_Anti += currentFile['Store: PercentCorrectWMAnti'][len(currentFile['Store: PercentCorrectWMAnti'])-3]
                # count_WM_Anti += 1

                filtered_rows = currentFile[currentFile['Event Index'] == 124].copy()
                percentCorrect_WM_Anti += sum(filtered_rows['Store: PercentCorrectWMAnti'])
                count_WM_Anti += len(filtered_rows)
                print('currentFile processed')

            if currentFile['Spreadsheet'][0].split('_trials_')[0]  == 'WM_Ctx1':
                # percentCorrect_WM_Ctx1 += currentFile['Store: PercentCorrectWMCtx1'][len(currentFile['Store: PercentCorrectWMCtx1'])-3]
                # count_WM_Ctx1 += 1

                filtered_rows = currentFile[currentFile['Event Index'] == 124].copy()
                percentCorrect_WM_Ctx1 += sum(filtered_rows['Store: PercentCorrectWMCtx1'])
                count_WM_Ctx1 += len(filtered_rows)
                print('currentFile processed')

            if currentFile['Spreadsheet'][0].split('_trials_')[0]  == 'WM_Ctx2': # info: Change to _3stim_trials_ from 8th month again
                # percentCorrect_WM_Ctx2 += currentFile['Store: PercentCorrectWMCtx2'][len(currentFile['Store: PercentCorrectWMCtx2'])-3]
                # count_WM_Ctx2 += 1

                filtered_rows = currentFile[currentFile['Event Index'] == 124].copy()
                percentCorrect_WM_Ctx2 += sum(filtered_rows['Store: PercentCorrectWMCtx2'])
                count_WM_Ctx2 += len(filtered_rows)
                print('currentFile processed')

acc_DM = percentCorrect_DM/count_DM
acc_DM_Anti = percentCorrect_DM_Anti/count_DM_Anti
acc_EF = percentCorrect_EF/count_EF
acc_EF_Anti = percentCorrect_EF_Anti/count_EF_Anti
acc_WM = percentCorrect_WM/count_WM
acc_WM_Anti = percentCorrect_WM_Anti/count_WM_Anti
acc_WM_Ctx1 = percentCorrect_WM_Ctx1/count_WM_Ctx1
acc_WM_Ctx2 = percentCorrect_WM_Ctx2/count_WM_Ctx2
acc_RP = percentCorrect_RP/count_RP
acc_RP_Anti = percentCorrect_RP_Anti/count_RP_Anti
acc_RP_Ctx1 = percentCorrect_RP_Ctx1/count_RP_Ctx1
acc_RP_Ctx2 = percentCorrect_RP_Ctx2/count_RP_Ctx2


########################################################################################################################
# Plot training effects
########################################################################################################################
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tools import rule_name
# from scipy.stats import linregress
# import matplotlib.dates as mdates

# Participant list
participant_dir = 'C:\\Users\\oliver.frank\\Desktop\\BackUp\\Data'
# participantList = os.listdir(participant_dir)
# participant = participantList[0] # choose which particpant to analyze
months = ['1','2','3','4','5','6','7','8','9','10','11','12'] # choose which month to analyze
strToSave = months[0] + '-' + months[-1]

newParticpantList = ['BeRNN_01'] #

# Assign a color to each task
filename_color_dict = {
    # **DM tasks (Dark Purple - High Contrast)**
    'DM': '#0d0a29',  # Deep Black-Purple
    'DM_Anti': '#271258',  # Dark Blue-Purple

    # **EF tasks (Purple-Pink Family - High Contrast)**
    'EF': '#491078',  # Muted Indigo
    'EF_Anti': '#671b80',  # Dark Magenta-Purple

    # **RP tasks (Pink/Red Family - High Contrast)**
    'RP': '#862781',  # Rich Magenta
    'RP_Anti': '#a6317d',  # Strong Pink
    'RP_Ctx1': '#c53c74',  # Bright Pinkish-Red
    'RP_Ctx2': '#e34e65',  # Vivid Red

    # **WM tasks (Red-Orange/Yellow Family - High Contrast)**
    'WM': '#f66c5c',  # Warm Reddish-Orange
    'WM_Anti': '#fc9065',  # Vibrant Orange
    'WM_Ctx1': '#feb67c',  # Pastel Orange
    'WM_Ctx2': '#fdda9c'  # Light Yellow
}

for participant in newParticpantList:
    # Create a list of all files in all defined month folders
    folder_paths = []
    for month in months:
        # Specify the folder containing the .xlsx files
        folder_paths.append(os.path.join(participant_dir, participant, month))

    # Initialize an empty list to hold all file names
    all_files = []
    # Iterate through each folder
    for folder in folder_paths:
        # List all files in the current folder
        for root, dirs, files in os.walk(folder):
            # Append each file to the all_files list
            for file in files:
                all_files.append(os.path.join(root, file))

    # Initialize empty lists to store combined x and y values
    all_x_values = []
    all_y_values = []

    # Set the figure size with increased y-length
    plt.figure(figsize=(15, 6))

    for task in filename_color_dict:
        print(task, filename_color_dict[task])

        # Create right name for ycolumn
        ycolumn = 'Store: PercentCorrect' + ''.join(task.split('_'))

        # Initialize empty lists to store combined x and y values
        all_x_values = []
        all_y_values = []

        # Iterate over all files in the folder
        for filename in all_files:
            if filename.endswith(".xlsx"):
                # file_path = os.path.join(folder_path, filename)
                try:
                    # Load the Excel file into a DataFrame
                    df = pd.read_excel(filename, engine='openpyxl')
                    if isinstance(df.iloc[0, 28], float) == False and df.iloc[0, 28].split('_trials_')[0] == task:
                        # Filter rows where "Event Index" is 125
                        filtered_rows = df[df['Event Index'] == 125].copy()
                        print(filename)

                        # Convert "Date and Time" to datetime format where possible
                        filtered_rows['Local Date and Time'] = pd.to_datetime(filtered_rows['Local Date and Time'], errors='coerce')
                        # Extract values from "Date and Time" and "Accuracy" columns
                        x_values = pd.to_datetime(filtered_rows['Local Date and Time'].dt.strftime('%d-%m-%Y'))
                        y_values = filtered_rows[ycolumn]

                        print('x_values: ', x_values)
                        print('y_values: ', y_values)

                        # Append values to the combined lists
                        all_x_values.extend(x_values)
                        all_y_values.extend(y_values)
                except Exception as e:
                    print(f"Error processing {filename}: {e}")

        # Sort the all_x_values
        all_x_values.sort()

        # Plot the task-related data
        plt.scatter(all_x_values, all_y_values, color=filename_color_dict[task], label=task)

        # Calculate and plot average performance for each task
        if all_y_values:
            avg_performance = np.mean(all_y_values)
            plt.axhline(avg_performance, color=filename_color_dict[task], linestyle='--', linewidth=1,label=f'{task} Avg: {avg_performance:.2f}%')

    plt.ylim(0, 100)
    plt.yticks(range(0, 101, 10), [f'{i}%' for i in range(0, 101, 10)])

    # Set custom x-axis labels
    min_date = min(all_x_values)
    max_date = max(all_x_values)
    date_range = (max_date - min_date) / 11 # info: Add one label for every newly added month - number of months  -1

    x_ticks = [min_date + i * date_range for i in range(12)] # info: Add one label for every newly added month - number of months
    x_labels = ['month 1', 'month 2', 'month 3', 'month 4', 'month 5', 'month 6', 'month 7', 'month 8', 'month 9', 'month 10', 'month 11', 'month 12']

    fs = 18
    plt.legend(loc='center left',fontsize=fs, ncol=2, bbox_to_anchor=(1, 0.5))
    plt.xlabel('Time',fontsize=fs)
    plt.ylabel('Performance',fontsize=fs)
    plt.title(participant, fontsize=18)
    plt.xticks(ticks=x_ticks, labels=x_labels)

    # Let matplotlib autoscale the x-axis
    plt.autoscale(enable=True, axis='x')

    # Save the figure to the folder where the data is from
    figure_path = os.path.join(participant_dir,participant,participant + '_' + strToSave + '_' + 'PerformanceOverTime.png')
    plt.savefig(figure_path, bbox_inches='tight')

    plt.tight_layout()
    plt.show()


