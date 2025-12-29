
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
def preprocess(data):
    data=data.copy()
    data['Bathrooms']=data['Bathrooms'].fillna(data['Bathrooms'].mode()[0])
    data['Bedrooms']=data['Bedrooms'].fillna(data['Bedrooms'].mode()[0])
    data['Age_of_house']=data['Age_of_house'].fillna(data['Age_of_house'].median())
    data['Area_sqft']=data['Area_sqft'].fillna(data['Area_sqft'].median())
    return data