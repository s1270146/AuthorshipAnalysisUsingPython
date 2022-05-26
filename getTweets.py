import pandas as pd

def getAllTweetsBy2Authors(name):

    data = pd.read_csv('tweets.csv',usecols=[0,1])
    data = data[data['author']==name]

    return data['content'].astype(str)

# fName = input("Input 1th author's name:")
# sName = input("Input 2nd author's name:")
# fContents = getAllTweetsBy2Authors(fName)
# sContents = getAllTweetsBy2Authors(sName)
# print(fContents)
# print(sContents)