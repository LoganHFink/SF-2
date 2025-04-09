# Logan Fink
# 2435373

def toCelcius(temperature):
    return round((temperature -32) * (5/9),2)

def avgTempYear(dict,year):
    try:
        year_temps = dict[year]
    except KeyError:
        print('Invalid year, not in provided data')
        return
    else:
        return round(sum(year_temps)/len(year_temps),2)

def topThreeYears(dict):
    avgs = set()
    top_three_list = []
    for year in dict.keys():
        avgs.add(avgTempYear(dict,year))
    for i in range(3):
        top = max(avgs)
        avgs.remove(top)
        top_three_list.append(top)
    return top_three_list

def avgTempMonth(dict,month):
    month_dict = {'JAN':0,'FEB':1,'MAR':2,'APR':3,'MAY':4,'JUN':5,'JUL':6,'AUG':7,'SEP':8,'OCT':9,'NOV':10,'DEC':11}
    month_list = []
    index = month_dict[month]
    for year_list in dict.values():
        month_list.append(year_list[index])
    return round(sum(month_list)/len(month_list),2)

def belowFreezing(dict):
    month_dict = {0:'JAN',1:'FEB',2:'MAR',3:'APR',4:'MAY',5:'JUN',6:'JUL',7:'AUG',8:'SEP',9:'OCT',10:'NOV',11:'DEC'}
    months_under_zero = set()
    for year_list in dict.values():
        for i in range(len(year_list)):
            if year_list[i] < 0:
                months_under_zero.add(month_dict[i])
    return months_under_zero

temp_dict = {}
input_file = open('data.txt','r')
for line in input_file:
    if line[0].isdigit():
        year = int(line[0:4])
        fahrenheit_list = line[5:].rstrip().split('    ')
        celcius_list = []
        for fahrenheit_temp in fahrenheit_list:
            celcius_list.append(toCelcius(float(fahrenheit_temp)))
        temp_dict[year] = celcius_list

output_file = open('data_celcius.txt','w')
input_file.seek(0)
for line in input_file:
    if not line[0].isdigit():
        output_file.write(line)

for year,temp_list in temp_dict.items():
    temp_line = ''
    for temp in temp_list:
        temp = str(round(temp,1))
        if temp[0] != '-':
            temp = ' ' + temp
        while len(temp) < 5:
            temp += ' '
        # chose not to use '\t' here so that the - signs are one to the left of the months, used three spaces instead 
        temp_line += f'{temp}   '
    output_file.write(f'{year}   {temp_line[:-4]}\n')

input_file.close()
output_file.close()