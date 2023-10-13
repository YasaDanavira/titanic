from urllib.request import urlretrieve
import os

# Output Directory Path
output_relative_dir = '/mnt/c/GitHub/titanic/data/landing/'

# check if it exists as it makedir will raise an error if it does exist
if not os.path.exists(output_relative_dir):
    os.makedirs(output_relative_dir)
    
TEST_URL = "https://storage.googleapis.com/kagglesdsdata/competitions/3136/26502/test.csv?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1697435448&Signature=ONfpEfkCq7DsUw6QYDNel%2BfPo2dFTSu%2FhKTCskV7DKuh4Ktp%2Fj49MkwEl1swqUqnlwcAwcfhYLGhf7Tok7A76xHZApaF%2F1uSp%2F6URYPPLmF2vxCDMohio1JtV7PsizZ9i9AZzg4q06iRhpKjVQ7GMJvT4xD0CCD6zZOEtVS47cvFDQi5M%2Fl2b1jsfSlF3VXWqIOs6xlJ6v8hSEzON7YZTlM9EEV6GlCr2%2FEoddMK8U9fqGAbfYhNubu4Jc4NSrkdUKyCZw0uyS2mVVrIUQyLFony8HNQDiyCmJa%2FjsbvaWzbUBgjkOlLhokPlI3eC9dVVposaPkft1efpRBzmfXVaA%3D%3D&response-content-disposition=attachment%3B+filename%3Dtest.csv"
output_dir = f"{output_relative_dir}test.csv"
urlretrieve(TEST_URL, output_dir) 