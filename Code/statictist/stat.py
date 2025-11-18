
print("==================THONG KE CO BAN ==================")
import pandas as pd

churn_data = pd.read_csv(r'..\\banking-customer-churn\\Dataset_before_cleaning\\banking_customer_churn.csv')

print('''================== Banking Customer Churn Data =================''')
print(churn_data.head(),'\n')

print('kiem tra kich thuoc dataset')
print(churn_data.shape,'\n')

print('kiem tra thong tin')
print(churn_data.info(),'\n')

print('tinh tong gia tri null o cac cot')
print(churn_data.isnull().sum().sort_values(ascending= False),'\n')

print('kiem tra lap dong')
print(churn_data.duplicated().sum(),'\n')

print('Thong ke mo ta')
pd.set_option('display.float_format', '{:.0f}'.format)
print(churn_data.describe(),'\n')