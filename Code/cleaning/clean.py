'''
  ====================LAM SACH DU LIEU====================
'''
import pandas as pd
import numpy as np
import re
import os

def clean_data_1(path : str) -> pd.DataFrame:
    churn_data = pd.read_csv(path)

    print("Kich thuoc du lieu truoc khi lam sach: ", churn_data.shape)
    '''================xoa cot khong can thiet==================='''
    # xoa cot RowNumber, CustomerId, Surname
    churn_data.drop(['RowNumber','CustomerId', 'Surname'], axis= 1, inplace= True )

    '''====xu ly gia tri khac kieu du lieu trong cot Balance, HasCrCard, EstimatedSalary, Card Type===='''

    # kiem tra gia tri trong cot, neu khong the chuyen qua int, se loc so ra
    def fix_values(value):
        try:
            # chuyen qua float duoc thi qua
            float(value)
            return value
        except:
            # chuyen khong duoc qua float thi ky tu nao la so thi giu lai
            return ''.join([item for item in value if item in (str(i) for i in range(0, 10))])
    # sua lai gia tri trong cot Balance
    churn_data['Balance'] =churn_data['Balance'].apply(fix_values)
    # sua lai gia tri trong cot HasCrCard
    churn_data['HasCrCard'] = churn_data['HasCrCard'].apply(fix_values)
    ## sua lai gia tri trong cot EstimatedSalary
    def fix_EstimatedSalary(values):
        try:
            # chuyen qua duoc float thi qua
            float(values)
            return values
        except:
            # khong chuyen qua duoc thi lay het so ra
            match = re.findall(r"[0-9]+\-[0-9]+\-[0-9]+", str(values))
            # ghep lai va thay "-" thanh rong
            return ''.join(match).replace('-','')

    churn_data['EstimatedSalary'] = churn_data['EstimatedSalary'].apply(fix_EstimatedSalary)
    # sua lai gia tri trong cot Card Type
    def fix_text(value):
        # loc ra chu
        value_change = re.findall(r'[A-Z]+', value)
        for item in value_change:
            # neu ma la list nhieu phan tu thi ghep vao
            if len(value_change) >1:
                return ''.join(value_change)
            else:
                # co 1 phan tu thi lay ra
                return value_change[0]
    churn_data['Card Type']=churn_data['Card Type'].apply(fix_text)
    return churn_data

def clean_missing(data : pd.DataFrame) -> pd.DataFrame:
    '''====xu ly gia tri null===='''

    # thay null trong cot NumofProducts bang median
    data['NumOfProducts']=data['NumOfProducts'].fillna(int(data['NumOfProducts'].median()))
    # thay null trong cot HasCrCard bang mode
    data['HasCrCard']=data['HasCrCard'].fillna(int(data['HasCrCard'].mode()[0]))
    # thay null trong cot IsActiveMember bang mode
    data['IsActiveMember']=data['IsActiveMember'].fillna(int(data['IsActiveMember'].mode()[0]))
    # thay null trong cot CreditScore bang median
    data['CreditScore']=data['CreditScore'].fillna(data['CreditScore'].median())
    # thay null trong cot Age bang median
    data['Age']=data['Age'].fillna(int(data['Age'].median()))
    # thay null trong cot Tenure bang median
    data['Tenure']=data['Tenure'].fillna(int(data['Tenure'].median()))
    return data


def clean_dtype(data : pd.DataFrame) -> pd.DataFrame:
    '''====chuyen kieu du lieu===='''

    # chuyen kieu du lieu cot Balance thanh float
    data['Balance']=data['Balance'].astype('float')
    # chuyen kieu du lieu cot HasCrCard thanh int
    data['HasCrCard']=data['HasCrCard'].astype('int')
    # chuyen kieu du lieu cot Age thanh int
    data['Age']=data['Age'].astype('int')
    # chuyen kieu du lieu cot Tenure thanh int
    data['Tenure']=data['Tenure'].astype('int')
    # chuyen kieu du lieu cot NumOfProducts thanh int
    data['NumOfProducts']=data['NumOfProducts'].astype('int')
    # chuyen kieu du lieu cot IsActiveMember thanh int
    data['IsActiveMember']=data['IsActiveMember'].astype('int')
    # chuyen kieu du lieu cot EstimatedSalary thanh float
    data['EstimatedSalary']=data['EstimatedSalary'].astype('float')
    # chuyen kieu du lieu cot Exited thanh int
    data['Exited']=data['Exited'].astype('int')
    return data

def clean_outliers(data : pd.DataFrame) -> pd.DataFrame:
    '''============================xoa outlier==============================='''

    cols = ['CreditScore', 'Age', 'Balance', 'EstimatedSalary']
    # xoa oulier bang phuong phap IQR
    for col in cols:
        Q1 = data[col].quantile(0.25)
        Q2 = data[col].quantile(0.75)
        IQR = Q2 -Q1
        duoi = Q1 - 1.5*IQR
        tren = Q2 + 1.5* IQR
        data = data[(data[col] >= duoi) & (data[col] <= tren)]

    print("Kich thuoc du lieu sau khi lam sach: ", data.shape)

    return data
if __name__ == "__main__":
    churn_data = clean_data_1(r'..\\banking-customer-churn\\Dataset_before_cleaning\\banking_customer_churn.csv')
    churn_data = clean_missing(churn_data)
    churn_data = clean_missing(churn_data)
    churn_data = clean_dtype(churn_data)
    churn_data = clean_outliers(churn_data)
    '''====================luu du lieu da lam sach======================'''

# kiem tra da co file ..\\banking-customer-churn\\Dataset_cleaned\\banking_customer_churn_cleaned.csv chua
    if os.path.exists(r'..\\banking-customer-churn\\Dataset_cleaned\\banking_customer_churn_cleaned.csv'):
        os.remove(r'..\\banking-customer-churn\\Dataset_cleaned\\banking_customer_churn_cleaned.csv')
    churn_data.to_csv(r'..\\banking-customer-churn\\Dataset_cleaned\\banking_customer_churn_cleaned.csv', index= False)