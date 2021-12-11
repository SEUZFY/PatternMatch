import numpy as np
import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt  
from sklearn.metrics import classification_report # report

path = r"D:\AlbertQ2\GEO1003\PatternMatch\knn.csv"
data = pd.read_csv(path, header=None)

x, y = data[1].values.reshape(-1,1), data[0].values.reshape(-1,1) #数据后2列为特征列，第1列为标签列
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)


# KNN
clf = KNeighborsClassifier(n_neighbors = 3 , weights='distance')
clf.fit(x_train, y_train.ravel()) #拟合数据

#分类结果评估
y_predict = clf.predict(x_test) # y_predict为预测值
print(len(y_predict))
print(clf.score(x_test, y_test))
print('测试集准确率：', accuracy_score(y_test, clf.predict(x_test)))
print(classification_report(y_test, y_predict)) # 分类结果统计

#data_target = clf.predict(x_test)
#model = TSNE(n_components=2, early_exaggeration = 20,init='pca',learning_rate=1000,method='barnes_hut')

##fitting model
#transformed = model.fit_transform(x_test)

#x_axis = transformed[:,0]
#y_axis = transformed[:,1]

#plt.scatter(x_axis,y_axis,c=data_target,marker='.')
#plt.show()