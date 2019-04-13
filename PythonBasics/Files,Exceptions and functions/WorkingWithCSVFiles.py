"""
........................Creating a CSV File...............
"""
import csv
try:
    with open("MyFile.csv",mode='w') as f:
        a=csv.writer(f,delimiter=',')
        data=[['STOCK','SALES','PRICE'],
              ['100','40','40$'],
              ['300','240','240$'],
              ['40','100','100$']]
        a.writerows(data)
        print("WriteSuccessful")
except IOError:
    print("ExceptionCaught")    
    
    