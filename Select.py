import pandas as pd

# open file
file_object = open(r"D:\AlbertQ2\GEO1003\PatternMatch\loc1_eachsecond.txt", encoding='UTF-8')
try:
    file_content = file_object.readlines() # not very huge file, use readlines() to speed up
finally:
    file_object.close()

splitor = ','
time = []
signal = []
for each in file_content:
    time.append(each.split(splitor)[0])
    signal.append(float(each.split(splitor)[1]))

i=0
j=0
sum = 0
count = 0
avg_signal = []
while(j<len(time)):
    if(time[i] == time[j]):
        count += 1
        sum += signal[j]
        j += 1
    else:
        avg_signal.append(sum/count)
        #print(count)
        sum = 0
        count = 0
        i = j

#print(len(avg_signal))
pd.DataFrame(avg_signal).to_csv(r"D:\AlbertQ2\GEO1003\PatternMatch\loc1_each_timestamp.csv")
