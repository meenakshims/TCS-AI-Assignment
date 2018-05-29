import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv('train.csv')
print(dataset.isnull().sum())
dataset.dropna(inplace=True)
print(dataset.isnull().sum())
dataset=dataset.reset_index(drop=True)
dataset.drop('ID',axis=1)
del dataset['ID']

for i in range(len(dataset)):
	if dataset.at[i,'browserid']=='Chrome':
		dataset.at[i,'browserid']='Google Chrome'
	elif  dataset.at[i,'browserid']=='Firefox':
		dataset.at[i,'browserid'] = 'Mozilla Firefox'
	elif  dataset.at[i,'browserid']=='Mozilla':
		dataset.at[i,'browserid'] = 'Mozilla Firefox'
	else:
		if dataset.at[i,'browserid']=='InternetExplorer':
			dataset.at[i,'browserid'] = 'IE'
		elif dataset.at[i,'browserid']=='Internet Explorer':
			dataset.at[i,'browserid'] = 'IE'
    
for i in range(len(dataset)):
        datetime=dataset.iloc[i]['datetime'].split(' ')
        time=datetime[1].split(':')
        hour=int(time[0])
        if hour<=12:
            dataset.at[i, 'datetime'] = 'morning'
        elif hour<18:
            dataset.at[i, 'datetime'] = 'afternoon'
        else:
            dataset.at[i,'datetime']='evening'


#Encoding categorical data
cols_to_transform = [ 'datetime','countrycode','browserid','devid']
df_with_dummies = pd.get_dummies(dataset,columns = cols_to_transform,prefix = 'one')
#dataset = pd.concat([dataset,df_with_dummies],axis = 1,join='inner')
dataset.append(df_with_dummies, ignore_index=True)
dataset.drop(cols_to_transform,axis=1, inplace = True)
dataset.to_csv('dataset.csv')

x = dataset.ix[:, :-1].values 
y = dataset.ix[:, 'click'].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(dataset, y, test_size = 0.3,stratify=y)

#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

#print(X_train)
#print(X_test)

#feature selection
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
# create a base classifier used to evaluate a subset of attributes
model = LogisticRegression()
# create the RFE model and select 3 attributes
rfe = RFE(model)
rfe = rfe.fit(x, y)
# summarize the selection of the attributes
print(rfe.support_)
print(rfe.ranking_)

#split into test and validation
X_train, X_validate, y_train, y_validate = train_test_split(X_train, y_train, test_size=0.2)

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
def naive_b(X_train,y_train):
	from sklearn.naive_bayes import GaussianNB 
	classifier = GaussianNB()
	classifier.fit(X_train,y_train)
	y_pred = classifier.predict(X_test)
	cm = confusion_matrix(y_test,y_pred)
	print("Confusion matrix: Naive Bayes")
	print(cm)
	accuracy=accuracy_score(y_test,y_pred)
	print("accuracy:",accuracy)
	average_precision = average_precision_score(y_test, y_pred)
	print("Average precision score:", average_precision)
	

def Rf(X_train,y_train):
	from sklearn.ensemble import RandomForestClassifier
	classifier= RandomForestClassifier(n_estimators=4, criterion= 'entropy', random_state=0)
	classifier.fit(X_train,y_train)
	y_pred = classifier.predict(X_test)
	cm = confusion_matrix(y_test,y_pred)
	print("Confusion matrix: Random Forest")
	print(cm)
	accuracy=accuracy_score(y_test,y_pred)
	print("accuracy:",accuracy)

def DT(X_train,y_train):
	from sklearn.tree import DecisionTreeClassifier
	classifier= DecisionTreeClassifier(criterion= 'entropy',random_state=0)
	classifier.fit(X_train,y_train)
	y_pred = classifier.predict(X_test)
	cm = confusion_matrix(y_test,y_pred)
	print("Confusion matrix: Decision Tree")
	print(cm)
	accuracy=accuracy_score(y_test,y_pred)
	print("accuracy:",accuracy)

#applying classifer to test set
naive_b(X_train,y_train)
Rf(X_train,y_train)
DT(X_train,y_train)






