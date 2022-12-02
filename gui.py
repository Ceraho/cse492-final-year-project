import PySimpleGUI as sg
import MudekParser as mp
import os


def main_gui():
    sg.theme('Dark Blue 12')

    layout = [
        [sg.Text('Welcome to MUDEK Evaluation Tool!', font=('Times New Roman', 19, 'bold'))],
        [sg.Text('Input Dir Path:', font=('Times New Roman', 17), s=13, justification='r'), sg.Input(default_text='inputs/', key='-IN-'), sg.FolderBrowse(initial_folder='inputs/')],
        [sg.Text('Student IDs Path:', font=('Times New Roman', 17), s=13, justification='r'), sg.Input(default_text='resources/Student-ids-with-names.xlsx', key='-IN_STD-'), sg.FileBrowse(initial_folder='resources/Student-ids-with-names.xlsx', file_types=(("Excel Files", "*.xlsx"),))],
        [sg.Text('Output Dir Path:', font=('Times New Roman', 17), s=13, justification='r'), sg.Input(default_text='outputs/', key='-OUT-'), sg.FolderBrowse(initial_folder='outputs/')],
        [sg.Button('Generate Report', s=51)],
        [sg.Button('List of Students Above 3 Average', s=51)],
        [sg.Button('List All Sub-Outcomes Under 3 Average by Students', s=51)],
        [sg.Button('Min of All Sub-Outcomes by Lectures', s=51)],
        [sg.Button('Average of Program Sub-Outcomes by Lectures', s=51)],
        [sg.Button('Courses with a Sub-Outcome Average Below 3', s=51)],
        [sg.Exit(button_color='tomato', s=51)]
    ]

    window = sg.Window('MUDEK Evaluation Tool', layout, font=('Times New Roman', 15), element_justification='c')

    while True:
        event, values = window.read()
        if values["-IN-"][-1] != "/":
            values["-IN-"] += "/"
        if values["-OUT-"][-1] != "/":
            values["-OUT-"] += "/"

        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        elif event == 'Generate Report':
            for x in os.listdir(values['-OUT-']):
                print(f"Deleting {x} from output folder...")
                os.remove(os.path.join(values['-OUT-'], x))

            mp.assemble_report_file(inputs_path=values['-IN-'], student_ids_excel=values['-IN_STD-'], outputs_path=values['-OUT-'])

            if os.path.exists(f"{values['-OUT-']}error-log.txt"):
                sg.popup_error('Please check \"outputs/error-log.txt\"', font=('Times New Roman', 19, 'bold'))

            sg.popup('Report generated, you can continue with desired query(s).', font=('Times New Roman', 19, 'bold'))

        elif event == 'List of Students Above 3 Average':
            res_1 = mp.list_students_above_3_avg(report_file=f"{values['-OUT-']}output-report.xlsx", student_ids_excel=values['-IN_STD-'], outputs_path=values['-OUT-'])
            sg.popup_scrolled(res_1, title="List of Students Above 3 Average")
            sg.popup(f'\"List of Students Above 3 Average\" process is done. Please check the \"{values["-OUT-"]}\" directory.', font=('Times New Roman', 19, 'bold'), title="")

        elif event == 'List All Sub-Outcomes Under 3 Average by Students':
            res_1 = mp.list_all_sub_outcomes_under_3_avg_by_students(report_file=f"{values['-OUT-']}output-report.xlsx", student_ids_excel=values['-IN_STD-'], outputs_path=values['-OUT-'])
            sg.popup_scrolled(res_1, title="List All Sub-Outcomes Under 3 Average by Students")
            sg.popup(f'\"List All Sub-Outcomes Under 3 Average by Students\" process is done. Please check the \"{values["-OUT-"]}\" directory.', font=('Times New Roman', 19, 'bold'), title="")

        elif event == 'Min of All Sub-Outcomes by Lectures':
            res_1 = mp.min_of_all_sub_outcomes_by_lectures(report_file=f"{values['-OUT-']}output-report.xlsx", outputs_path=values['-OUT-'])
            sg.popup_scrolled(res_1, title="Min of All Sub-Outcomes by Lectures")
            sg.popup(f'\"Min of All Sub-Outcomes by Lectures\" process is done. Please check the \"{values["-OUT-"]}\" directory.', font=('Times New Roman', 19, 'bold'), title="")

        elif event == 'Average of Program Sub-Outcomes by Lectures':
            res_2 = mp.avg_of_all_sub_outcomes_by_lectures(report_file=f"{values['-OUT-']}output-report.xlsx", outputs_path=values['-OUT-'])
            sg.popup_scrolled(res_2, title="Average of Program Sub-Outcomes by Lectures")
            sg.popup(f'\"Average of Program Sub-Outcomes by Lectures\" process is done. Please check the \"{values["-OUT-"]}\" directory.', font=('Times New Roman', 19, 'bold'), title="")

        elif event == 'Courses with a Sub-Outcome Average Below 3':
            res_3 = mp.list_all_lectures_under_3_avg(report_file=f"{values['-OUT-']}output-report.xlsx", outputs_path=values['-OUT-'])
            sg.popup_scrolled(res_3, title="Courses with a Sub-Outcome Average Below 3")
            sg.popup(f'\"Courses with a Sub-Outcome Average Below 3\" process is done. Please check the \"{values["-OUT-"]}\" directory.', font=('Times New Roman', 19, 'bold'), title="")

    window.close()


main_gui()
