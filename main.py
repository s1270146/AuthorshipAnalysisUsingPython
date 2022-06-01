from Analyse import UserAnalyse 
import getTweets as gt
import processData as pd

# Read katy's Tweets
FirstAuthorTweets = gt.getAllTweetsBy2Authors(1)
FirstAuthorList = pd.processDatasets(FirstAuthorTweets['content'])

# Read taylor's Tweets
SecondAuthorTweets = gt.getAllTweetsBy2Authors(2)
SecondAuthorList = pd.processDatasets(SecondAuthorTweets['content'])

# generate katy's object
FirstAuthor = UserAnalyse(FirstAuthorList, FirstAuthorTweets['authorName'])
# generate taylor's object
SecondAuthor = UserAnalyse(SecondAuthorList, SecondAuthorTweets['authorName'])

"""
do uni-gram and analyze
"""
# doBiGram
FirstAuthor.doNGram(1)
SecondAuthor.doNGram(1)

# FS --> Compare FirstAuthor and SecondAuthor
FF = FirstAuthor.execute(FirstAuthor.questionedDict)
FS = FirstAuthor.execute(SecondAuthor.questionedDict)
SS = SecondAuthor.execute(SecondAuthor.questionedDict)
SF = SecondAuthor.execute(FirstAuthor.questionedDict)

print("=======================Result of Uni-Gram==========================")
print("known = {} , questioned = {} ".format(FirstAuthor.name, FirstAuthor.name) + FF)
print("known = {} , questioned = {} ".format(FirstAuthor.name, SecondAuthor.name) + FS)
print("known = {} , questioned = {} ".format(SecondAuthor.name, SecondAuthor.name) + SS)
print("known = {} , questioned = {} ".format(SecondAuthor.name, FirstAuthor.name) + SF)

"""
do bi-gram and analyze
"""
# doBiGram
FirstAuthor.doNGram(2)
SecondAuthor.doNGram(2)

# FS --> Compare FirstAuthor and SecondAuthor
FF = FirstAuthor.execute(FirstAuthor.questionedDict)
FS = FirstAuthor.execute(SecondAuthor.questionedDict)
SS = SecondAuthor.execute(SecondAuthor.questionedDict)
SF = SecondAuthor.execute(FirstAuthor.questionedDict)

print("=======================Result of Bi-Gram==========================")
print("known = {} , questioned = {} ".format(FirstAuthor.name, FirstAuthor.name) + FF)
print("known = {} , questioned = {} ".format(FirstAuthor.name, SecondAuthor.name) + FS)
print("known = {} , questioned = {} ".format(SecondAuthor.name, SecondAuthor.name) + SS)
print("known = {} , questioned = {} ".format(SecondAuthor.name, FirstAuthor.name) + SF)

"""
do tri-gram and analyze
"""
# doTriiGram
FirstAuthor.doNGram(2)
SecondAuthor.doNGram(2)

# FS --> Compare FirstAuthor and SecondAuthor
FF = FirstAuthor.execute(FirstAuthor.questionedDict)
FS = FirstAuthor.execute(SecondAuthor.questionedDict)
SS = SecondAuthor.execute(SecondAuthor.questionedDict)
SF = SecondAuthor.execute(FirstAuthor.questionedDict)

print("=======================Result of Bi-Gram==========================")
print("known = {} , questioned = {} ".format(FirstAuthor.name, FirstAuthor.name) + FF)
print("known = {} , questioned = {} ".format(FirstAuthor.name, SecondAuthor.name) + FS)
print("known = {} , questioned = {} ".format(SecondAuthor.name, SecondAuthor.name) + SS)
print("known = {} , questioned = {} ".format(SecondAuthor.name, FirstAuthor.name) + SF)
