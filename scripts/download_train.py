from urllib.request import urlretrieve
import os

# Output Directory Path
output_relative_dir = '/mnt/c/GitHub/titanic/data/landing/'

# check if it exists as it makedir will raise an error if it does exist
if not os.path.exists(output_relative_dir):
    os.makedirs(output_relative_dir)
    
TRAIN_URL = "https://storage.googleapis.com/kagglesdsdata/competitions/3136/26502/train.csv?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1697435418&Signature=1EH9Ihd0EdYMqWFWleYiJwXaoySFUVR2fyqN3I1FQP7pPazzr2bKD7SKcp9XJj148ry2swDuRdWqPUYhIIMxL5OhLVVHPqMbsCDBKQil8c68%2Bjt00g7evfdrWhdjOvkvmH2x5YwfACUQMKiWJQ3zZyKc4kPpvJJ9tyJ02D21xYSihVqrP7RMVDUr%2BNRKYRhgIPjBS8EcUCSODrRhTbzxOleGKJyhfPzlbrWXKDxr19eSUwwaz6cru7Lb7c48Tdy7mm9ORsuy%2FIBqGecee4VcsiTxulD0jkVb0%2FdvFijdxbxh%2FH49q8GHU1117pg9DmqeLNkVQ94BRJ12cUADXPVyog%3D%3D&response-content-disposition=attachment%3B+filename%3Dtrain.csv"
output_dir = f"{output_relative_dir}train.csv"
urlretrieve(TRAIN_URL, output_dir) 