#importing part
import pandas as pd
import numpy as np
from sklearn.model_selection  import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score

class BackEnd:

    def load_dataset(self):
        # load dataset
        global dataset
        dataset= pd.read_csv('diabetes.csv')

    def remove_zeros(self):
        # remove zeros
        remove_zero = ['Glucose', 'BloodPressure', 'SkinThickness', 'BMI', 'Insulin' ]

        for column in remove_zero:
            dataset[column] = dataset[column].replace(0,np.NaN)
            mean= int( dataset[column].mean(skipna=True) )
            dataset[column] = dataset[column].replace(np.NaN, mean)

    def split(self):

        #split dataset
        self.X = dataset.iloc[:,0:8]
        self.Y = dataset.iloc[:, 8]
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(self.X,self.Y, random_state=0, test_size=0.2)

    def Feature_Scaling(self):

        #Feature scaling
        global sc_X
        sc_X = StandardScaler()
        self.X_train = sc_X.fit_transform(self.X_train)
        self.X_test = sc_X.transform(self.X_test)

    def model(self):
        global classifier
        # define the model : Init K-NN
        classifier = KNeighborsClassifier(n_neighbors=42, p=2, metric='euclidean')

        #fit Model
        classifier.fit(self.X_train, self.Y_train)

        # Predict the test set results
        self.Y_pred = classifier.predict(self.X_test)

        #Evaluate the model
        self.cm = confusion_matrix(self.Y_test,self.Y_pred)
        self.cr=classification_report(self.Y_test,self.Y_pred)

    def scores(self):
        print(self.cm)
        print(self.cr)
        print("F1 Score : ", f1_score(self.Y_test, self.Y_pred) )
        print("Accuracy Score : ", accuracy_score(self.Y_test, self.Y_pred) )

    def predictor(b):
        X_test1 = b
        X_test1 = sc_X.transform(X_test1)
        Y_pred1 = classifier.predict(X_test1)
        return Y_pred1

    def knn(self):
        d.load_dataset()
        d.remove_zeros()
        d.split()
        d.Feature_Scaling()
        d.model()
        d.scores()


d = BackEnd()
