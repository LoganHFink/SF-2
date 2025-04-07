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
input_file.close()

# these were just for testing
# print(avgTempYear(temp_dict,1965))  
# print(topThreeYears(temp_dict))
# print(avgTempMonth(temp_dict,'JAN'))