import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pickle


uni=pd.read_csv(r"H:\project\uni.csv")

x=uni[["GRE_Score","TOEFL_Score","SOP","Research","CGPA"]]
y=uni['University_Rating']

x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=1,test_size=0.2)

tree = DecisionTreeClassifier()
tree.fit(x_train, y_train)


pickle.dump(tree, open('uni_model.pkl', 'wb'))