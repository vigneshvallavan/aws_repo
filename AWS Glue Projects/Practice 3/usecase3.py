import pandas as pd

dataFrame = pd.read_csv('C:\\Users\\US\Desktop\\aws_usecase\\usecase_3.csv')

dataFrame['producer_dt'] = pd.to_datetime(dataFrame['producer_dt'])  #convert producer_dt column datatype into date datatype

print(dataFrame)

result = dataFrame

i = 0

for x in result['producer_dt']:

    a = pd.to_datetime(x)
    date = '01/01/2009'
    b = pd.to_datetime(date)

    if a > b:

        dataFrame.loc[i,'producer_status'] = "APPLICABLE"

    else:

        dataFrame.loc[i,'producer_status'] = "NOT APPLICABLE"

    i+=1
print(dataFrame)

