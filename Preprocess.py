import numpy as np
import pandas as pd

# open file
file_object = open(r"D:\AlbertQ2\GEO1003\PatternMatch\loc4.txt", encoding='utf-8')
try:
    file_content = file_object.readlines() # not very huge file, use readlines() to speed up
finally:
    file_object.close()

splitor = '\t'
mac = []
signal = []
for each in file_content:
    mac.append(each.split(splitor)[1]) # mac address
    signal.append(float(each.split(splitor)[4])) # signal strength

pd.DataFrame(signal).to_csv(r"D:\AlbertQ2\GEO1003\PatternMatch\loc4signal.csv")
pd.DataFrame(mac).to_csv(r"D:\AlbertQ2\GEO1003\PatternMatch\loc4mac.csv")
