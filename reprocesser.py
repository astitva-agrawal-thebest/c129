import csv
data1=[]
with open("final.csv","r")as f:
    reader=csv.reader(f)
    for row in reader:
        data1.append(row)

data2=[]
with open("archive_dataset1.csv","r")as f:
    reader=csv.reader(f)
    for row in reader:
        data2.append(row)

headers1=data1[0]
planet_data1=data1[1:]

headers2=data2[0]
planet_data2=data2[1:]

headers=headers1+headers2
data=[]
for index, d in enumerate(planet_data1):
    data.append(planet_data1[index]+planet_data2[index])

with open("merged_data.csv","a+")as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(data)