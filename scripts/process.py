import openpyxl
import csv
from datapackage import Package

def data_package():
    package = Package()
    package.infer(r'data/schools.csv')
    package.commit()
    package.save(r"datapackage.json")

workbook = openpyxl.load_workbook('archive/schools.xlsx')
worksheet = workbook.active
desired_columns = [1, 24]
new_values = ["region","schools","year"]
with open('data/schools.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(new_values)
    for row in worksheet.iter_rows(min_row=10, max_row=29):
        values = [cell.value for cell in row if cell.column in desired_columns]
        if row[0].row > 9:
            values.append("2022-2023")
        writer.writerow(values)

data_package()