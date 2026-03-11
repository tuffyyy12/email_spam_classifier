import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
df = pd.read_csv('spam.csv',encoding ='latin-1')
print(df.head())
print(df.columns)
df = df[['v1','v2']]
print(df.head())
df.columns=['label','message']
print(df.head())
df['label']=df['label'].map({"ham":0,"spam":1})
print(df.head())
print(df.isnull().sum())
print(df.duplicated().sum())
df = df.drop_duplicates()
print(df.duplicated().sum())
print(df['label'].value_counts())
X=df['message']
y=df['label']
vectorizer = TfidfVectorizer()
X=vectorizer.fit_transform(X)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size = 0.2,random_state=42)
model = MultinomialNB()
model.fit(X_test,y_test)
predictions= model.predict(X_test)
print("Accuracy:", accuracy_score(predictions,y_test))
print(predictions[:10])
print(y_test[:10])
joblib.dump(model, "spam_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
print(df['label'].value_counts())
