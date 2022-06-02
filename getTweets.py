import pandas as pd

def getAllTweetsBy2Authors(num):
    data = pd.read_csv('tweets.csv',usecols=[0,1], index_col=False)
    data_clean = data.drop_duplicates(subset=['author'])
    print('Choose author name from the following list : ')
    for author in data_clean['author'].to_list() : 
        print(author)
    fName = input("Input {}th author's name:".format(num))
    data = pd.read_csv('tweets.csv',usecols=[0,1])
    data = data[data['author']==fName]
    result = dict()
    result['content'] = data['content'].astype(str)
    result['authorName'] = fName
    return result

def getAllTweets():
    data = pd.read_csv('tweets.csv',usecols=[0,1])
    return data['content'].astype(str)

# fName = input("Input 1th author's name:")
# sName = input("Input 2nd author's name:")
# fContents = getAllTweetsBy2Authors(fName)
# sContents = getAllTweetsBy2Authors(sName)
# print(fContents)
# print(sContents)


if __name__ == '__main__':
    name1 = 'katyperry'
    name2 = 'taylorswift13'
    print(getAllTweetsBy2Authors(name1))
    print(getAllTweetsBy2Authors(name2))

