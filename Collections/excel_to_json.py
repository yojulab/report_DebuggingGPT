import pandas as pd
import json
import re
import math


def get_matche_columns(columns_name):
    regex_patterns = [r'(작성)\s*([cC]ode|코드)',
                      r'(에러)*\s*([eE]rror|내용)+', r'(해결)\s*([cC]ode|코드)']

    result_columns = []
    # Use a list comprehension to find all column names that match the regular expression
    for index, regex_pattern in enumerate(regex_patterns):
        matches = [col for col in columns_name if re.match(
            regex_pattern, col, re.IGNORECASE)]
        if len(matches) > 0:
            result_columns.append(matches[0])

    return result_columns


# Read Excel file
excel_file = pd.read_excel('Datas/DebugginDairy_Pythons.xlsx', sheet_name=None)

# Create empty list for objects
objects_list = []

# Iterate through each row of Excel sheet
total_rows = 0
for sheet_name in list(excel_file.keys()):
    excel_sheet = excel_file[sheet_name]
    column_list = get_matche_columns(list(excel_sheet.columns))
    for index, row in excel_sheet.iterrows():
        # Create object for each row
        if len(column_list) == 3 and type(row[column_list[0]]) is str:
            object_dict = {
                'sheet_name': sheet_name,
                'debugCode': row[column_list[0]],
                'errorContent': row[column_list[1]],
                'resultCode': row[column_list[2]]
            }
            # Append object to list
            objects_list.append(object_dict)
            total_rows = total_rows + 1

print(f'total_rows : {total_rows}')
# Create JSON file
with open('Datas/output.json', 'w') as output_file:
    json.dump(objects_list, output_file, ensure_ascii=False)
