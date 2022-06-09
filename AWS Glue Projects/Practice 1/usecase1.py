from io import StringIO
import boto3
import pandas as pd

s3 = boto3.client('s3')

csvFile = s3.get_object(Bucket = 'for-usecases-athena', Key = 'usecase_1.csv')

dataFrame = pd.read_csv( csvFile['Body'] )

d = dataFrame.duplicated( subset = ['Key_col'], keep = 'first')

dataFrame2 = dataFrame[~d]

dataFrame3 = dataFrame[d]

dataFrame2["rec_ind"] = "Act"

dataFrame3["rec_ind"] = "Rej"

finalDataFrame = pd.concat([dataFrame2,dataFrame3])

print(finalDataFrame)

csv_buffer = StringIO()

finalDataFrame.to_csv(csv_buffer, index = False)

s3_resource = boto3.resource('s3')

s3_resource.Object('for-usecases-athena', 'pyshellOutput/usecase_1_pythonshell.csv').put(Body = csv_buffer.getvalue())