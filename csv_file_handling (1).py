import csv
import os

files = os.listdir(r'C:\Users\Shree\Desktop\student_data')
student_data_files = []

for file in files:
    if file.endswith('.csv'):
        student_data_files.append(file)

print(student_data_files)


def read_csv_data(path):

    f = open(path, 'r')
    rows = csv.reader(f)
    header = next(rows)
    header.append('Total')
    header.append('Percentage')
    new_row = []

    for row in rows:
        total = float(row[4]) + float(row[5]) + float(row[6])
        per = total / 3
        row.append(total)
        row.append(per)
        new_row.append(row)
    # print(new_row)
    return new_row, header


def write_data_to_csv(data):
    try:
        f = open('result.csv', 'a', newline='')
        w = csv.writer(f)
        w.writerows(data)
        print("Result stored successfully!!")
    except Exception as e:
        print("Error occured while processing file")




for i,file in enumerate(student_data_files):
    path = r'C:\Users\Shree\Desktop\Student_data'
    file_name = path + '\\' + file
    data, header = read_csv_data(file_name)
    all_data = []
    if i == 0:

        all_data.append(header)
        print(data)
        all_data.extend(data)
        print(all_data)
        write_data_to_csv(all_data)
    else:
        write_data_to_csv(data)









