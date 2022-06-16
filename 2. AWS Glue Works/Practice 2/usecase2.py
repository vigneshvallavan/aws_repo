import pandas as pd

dataFrame = pd.read_csv('C:\\Users\\US\Desktop\\aws_usecase\\usecase_2.csv')

print(dataFrame)

result = dataFrame

i = 0
for x in result['full_nm']:
    a = str(x)
    b = a.replace(" ","")
    dataFrame.loc[i,'full_nm'] = str(b)  # loc --> location
    i+=1
    
print(dataFrame)
