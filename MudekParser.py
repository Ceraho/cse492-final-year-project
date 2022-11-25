import pandas as pd
import numpy as np
import re
import os

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


def parse_grades_excels(grades_file:str):
    input_file = pd.ExcelFile(grades_file)

    df_list = []
    for current_sheet in input_file.sheet_names:
        if current_sheet == input_file.sheet_names[0]:
            sub_outcome_df = pd.read_excel(input_file, sheet_name=current_sheet).drop(columns='Program Alt-Çıktıları')
            continue
        df_list.append(pd.read_excel(input_file, sheet_name=current_sheet, index_col='Öğrenci No'))
        for col in df_list[-1].columns:
            if not re.search(r'[0-9][a-zA-Z]', col):
                df_list[-1].drop(columns=col, inplace=True)

        df_list[-1].name = current_sheet

    return sub_outcome_df, df_list


def generate_empty_report_df(sub_outcome_df:pd.DataFrame, student_ids_excel:str=None):
    student_id_df = pd.read_excel(student_ids_excel, index_col='Öğrenci No')

    sub_outcome_df['Alt-Çıktı No'] = pd.Series(sub_outcome_df['Alt-Çıktı No']).fillna(method='ffill')
    sub_outcome_df.dropna(how='any', inplace=True)

    sub_outcome_list = []
    for j in range(len(sub_outcome_df.index)):
        sub_outcome_list.append(f'{sub_outcome_df.iat[j,0]}-{sub_outcome_df.iat[j,1]}')

    student_id_df[sub_outcome_list] = np.NAN
    output_df = student_id_df

    return output_df


def fill_report_df(df_list:list=None, output_df:pd.DataFrame=None, outputs_path:str=None):
    for input_df in df_list:
        for student_id in input_df.index:
            for sub_outcome in input_df.columns:
                try:
                    input_value = input_df.at[student_id, sub_outcome]
                    output_outcome = f'{sub_outcome}-{input_df.name}'
                    output_value = output_df.at[student_id, output_outcome]
                    if pd.isnull(output_value):
                        output_df.at[student_id, output_outcome] = input_df.at[student_id, sub_outcome]
                    elif str(output_value).isalpha():
                        continue
                    elif str(output_value).isnumeric:
                        if float(output_value) < float(input_value):
                            output_df.at[student_id, output_outcome] = input_df.at[student_id, sub_outcome]
                except KeyError:
                    with open(f"{outputs_path}error-log.txt", 'a+') as f:
                        f.write(f'Warning: Encountered a KeyError, missing \"{student_id}\"\n')

    print(f"OUTPUT IS AT: {outputs_path}output-report.xlsx")
    output_df.to_excel(f'{outputs_path}output-report.xlsx')
    return output_df


def assemble_report_file(inputs_path:str='inputs/', student_ids_excel:str='resources/Student-ids.xlsx', outputs_path:str="outputs/"):
    final_df = None
    for input_file in os.listdir(inputs_path):
        if input_file.endswith('.xlsx'):
            grades_file = os.path.join(inputs_path, input_file)

            sub_outcome_df, df_list = parse_grades_excels(grades_file=grades_file)

            if os.path.exists(f'{outputs_path}output-report.xlsx'):
                output_df = pd.read_excel(f'{outputs_path}output-report.xlsx', index_col='Öğrenci No')
            else:
                output_df = generate_empty_report_df(sub_outcome_df=sub_outcome_df, student_ids_excel=student_ids_excel)

            final_df = fill_report_df(df_list=df_list, output_df=output_df, outputs_path=outputs_path)

            print(f"+++++++++ {grades_file} WAS PARSED SUCCESSFULLY +++++++++\n")

    if final_df is None:
        return 'Function returned a \"None\" type object, please check your paths!'
    return final_df


def list_students_under_3_avg(report_file:str='outputs/output-report.xlsx', outputs_path:str="outputs/"):
    # TODO: To be continued depending on what exactly the query is !!!
    output_df = pd.read_excel(report_file, index_col='Öğrenci No')
    transposed_output_df = output_df.replace(to_replace='B', value=5.0)

    transposed_output_df = transposed_output_df.T
    transposed_output_df = transposed_output_df.mean().dropna()

    for row in transposed_output_df.index:
        if transposed_output_df[row] > 3:
            transposed_output_df.drop(labels=row, inplace=True)

    transposed_output_df.to_excel(f'{outputs_path}list_of_students_under_3_avg.xlsx')
    return transposed_output_df


def avg_of_all_sub_outcomes_by_lectures(report_file:str='outputs/output-report.xlsx', outputs_path:str="outputs/"):
    output_df = pd.read_excel(report_file, index_col='Öğrenci No')
    output_df = output_df.replace(to_replace='B', value=5.0)

    set_of_lecs = set()
    set_of_outcomes = set()
    lec_oc_val_dict = dict()

    for col in output_df.columns:
        x = re.search(r'([0-9]+[a-z]{1})-(CSE[0-9]{3}|GBE[0-9]{3})', col)
        set_of_lecs.add(x.group(2))
        set_of_outcomes.add(x.group(1))
        lec_oc_val_dict[x.group(0)] = output_df[col].mean()

    result_df = pd.DataFrame(index=list(set_of_outcomes), columns=list(set_of_lecs))

    for i in result_df.index:
        for c in result_df.columns:
            for key, val in lec_oc_val_dict.items():
                if i in key and c in key:
                    result_df.at[i, c] = val

    result_df.to_excel(f'{outputs_path}avg_of_all_lectures.xlsx')
    return result_df


def list_all_lectures_under_3_avg(report_file:str='outputs/output-report.xlsx', outputs_path:str="outputs/"):
    oc_lec_ave_df = avg_of_all_sub_outcomes_by_lectures(report_file)
    final_df = oc_lec_ave_df[oc_lec_ave_df < 3].dropna(how='all', axis=0).dropna(how='all', axis=1)

    final_df.to_excel(f'{outputs_path}list_of_lectures_under_3_avg.xlsx')
    return final_df
