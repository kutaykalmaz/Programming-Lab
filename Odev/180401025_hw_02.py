import csv, sys 
from datetime import datetime

arg1 = sys.argv[1]
path = arg1 + "\\input_hw_2.csv"
arg2 = sys.argv[2]
receiver = arg2 + "\\180401025_hw_02_output.txt"

with open(path, 'r', encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    main_data = [word for word in [row for row in csv_reader]]
    e_dates = [main_data[index][3] for index in range(len(main_data))]
    for index in range(len(e_dates)):
        e_dates[index] = datetime.strptime(
            e_dates[index], "%Y-%m-%d %H:%M:%S.%f")
    months = [e_dates[index].month for index in range(len(e_dates))]


def Median(inlist):
    newInlist = sorted(inlist)
    n = len(newInlist)
    if n % 2 == 1:
        middle = int(n/2)+1
        median = newInlist[middle - 1]
    else:
        middle_1 = int(n/2) - 1
        middle_2 = middle_1 + 1
        median = (newInlist[middle_1] + newInlist[middle_2]) / 2
    return median
    

def Histogram(inlist):
    moth_dict = dict()
    for index in range(len(inlist)):
        if inlist[index] in moth_dict:
            moth_dict[inlist[index]] += 1
        else:
            moth_dict[inlist[index]] = 1
    return moth_dict


def Mean(inlist):
    sum = 0
    count = len(inlist)
    for index in inlist:
        sum += index
        # count += 1
    mean = sum / count
    return mean


months_dict = Histogram(months)
valueList = values = [*months_dict.values()]
median = Median(valueList)
mean = int(Mean(valueList))
output_list = ["Medyan", str(median), "Ortalama", str(mean)]

with open(receiver, "w", encoding="utf-8") as file:
    for i in range(0,len(output_list),2):
        file.write(output_list[i] + " " + output_list[i+1] + "\n")
