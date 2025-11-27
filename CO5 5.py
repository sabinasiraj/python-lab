import csv
csv_col=['ROLLNO','NAME','PLACE']
dict_data=[{'ROLLNO':1,'NAME':'SABINA','PLACE':'KUMILY'},
{'ROLLNO':2,'NAME':'SALMAN','PLACE':'THEKKADY'},
{'ROLLNO':3,'NAME': 'SALU','PLACE':'KUMILY'},
{'ROLLNO':4,'NAME':'SINIJA','PLACE':'KUMILY'},
{'ROLLNO':5,'NAME':'SIRAJ','PLACE':'KUMILY'}]
csv_file="STUDENT.csv"
try:
 with open(csv_file,'w')as file1:
   writer=csv.DictWriter(file1,fieldnames=csv_col)
   writer.writeheader()
   for data1 in dict_data:
        writer.writerow(data1)
except IOError:
    print("I/O error")
data1 = csv.DictReader(open(csv_file))
print("CSV file as a dictionary:\n")
for row in data1:
    print(row)
