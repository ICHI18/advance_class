import csv

reader_cp = []

with open ('04data.csv' , 'r' , encoding = 'cp932') as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        reader_cp.append(row) #2次元配列

#print(reader_cp)


i = 0
b = 0
hour = 0

for a in reader_cp:
    b += 1
#print(b)
#print(reader_cp[0][2])

for j in range(24):
    sum_temperture_1 = 0
    sum_temperture_2 = 0
    k = 0
    if j < 10:
        hour = str(0) + str(j) + ":00"
    else:
        hour = str(j) + ":00"
    #print(hour)

    for i in range(b):
        if reader_cp[i][2] == hour:
            #print(reader_cp[i][2],reader_cp[i][3])
            k += 1
            sum_temperture_1 += (int(reader_cp[i][3])-32)/1.8
            sum_temperture_2 += (int(reader_cp[i][4])-32)/1.8
    print(str(j) + "時の平均気温 ① :" + str(round(sum_temperture_1/k)) + "℃" + "  ② :" + str(round(sum_temperture_2/k)) + "℃")
    
