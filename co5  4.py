import csv
with open('student.csv','r')as csvfile1:
    data=csv.DictReader(csvfile1)
    print("NAME")
    print("----")
    for i in data:
        print(i['NAME'])
