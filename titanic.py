import pandas as pd
from matplotlib import pyplot as plt

train = pd.read_csv("/Users/wiktoriatwarog/Documents/Kaggle/Titanic/train.csv")

print(train.info())
print(train.isnull().sum())

survived = train[train["Survived"] == 1]
not_survived = train[train["Survived"] == 0]


#Age of Men and Women who survived/not survived
male_survived = train[train["Sex"] == "male"]
male_not_survived = train[train["Sex"] == "male"]
fig, ax = plt.subplots()
rects1 = ax.hist(male_survived["Age"], label='Male Survived', histtype = 'step')
rects2 = ax.hist(male_not_survived["Age"], label='Male Not Survived', histtype = 'step')
ax.legend()
plt.show()

print(male_survived)

#features = ["Pclass", "Sex", "SibSp", "Parch"]
