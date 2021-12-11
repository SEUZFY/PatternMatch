import numpy as np
import pandas as pd

# open file
file_object = open(r"D:\AlbertQ2\GEO1003\PatternMatch\Geolab.txt", encoding='utf-8')
try:
    file_content = file_object.readlines() # not very huge file, use readlines() to speed up
finally:
    file_object.close()

splitor = '\t'
signal = []
for each in file_content:
    signal.append(float(each.split(splitor)[4])) # signal strength

pd.DataFrame(signal).to_csv(r"D:\AlbertQ2\GEO1003\PatternMatch\Geolab.csv")
