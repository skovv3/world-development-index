import csv
import sys
import os
from time import gmtime, strftime
import numpy as np


def tally():
    with open('Indicators.csv') as csvsc:
        rdsc = csv.DictReader(csvsc)
        #data = ['"m"', ",", '"f"', "\n"]
        data = []
        for row in rdsc:
            if row['CountryCode'] == 'IND' and row['IndicatorCode'] == 'SP.DYN.AMRT.FE':
                fe = row['Value']
                ffe = fe.split('.')
                ff = int(ffe[0]) / 100
            if row['CountryCode'] == 'IND' and row['IndicatorCode'] == 'SP.DYN.AMRT.MA':
                ml = row['Value']
                fml = ml.split('.')
                fm = int(fml[0]) / 100
                pdt = ff, ",", fm, "\n"
                print pdt
                data.append(pdt)
        f = open('data.csv', 'w')
        f.write(np.hstack(data))  # python will convert \n to os.linesep
        f.close()  # you can omit in most cases as the destructor will call it
 
tally()
# print out
