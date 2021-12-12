import numpy as np
import pandas as pd

# open file
file_object = open(r"D:\AlbertQ2\GEO1003\PatternMatch\loc1.txt", encoding='UTF-8-sig')
try:
    file_content = file_object.readlines() # not very huge file, use readlines() to speed up
finally:
    file_object.close()

splitor = ';'
timestamp = []
signal = []
for each in file_content:
    timestamp.append(each.split(splitor)[1]) # mac address
    signal.append(float(each.split(splitor)[5])) # signal strength

pd.DataFrame(signal).to_csv(r"D:\AlbertQ2\GEO1003\PatternMatch\group1_loc1_signal.csv")
pd.DataFrame(timestamp).to_csv(r"D:\AlbertQ2\GEO1003\PatternMatch\group1_loc1_time.csv")
