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

def getN(N) :
    if N == 1: return 'Uni'
    elif N == 2 : return 'Bi'
    elif N == 3 : return 'Tri'

for N in range(1,4) : 
    """
    do N-gram and analyze
    """
    # do N-Gram
    FirstAuthor.doNGram(N)
    SecondAuthor.doNGram(N)

    # FS --> Compare FirstAuthor and SecondAuthor
    FF = FirstAuthor.execute(FirstAuthor.questionedDict)
    FS = FirstAuthor.execute(SecondAuthor.questionedDict)
    SS = SecondAuthor.execute(SecondAuthor.questionedDict)
    SF = SecondAuthor.execute(FirstAuthor.questionedDict)

    print("=======================Result of {}-Gram==========================".format(getN(N)))
    print("known = {} , questioned = {} ".format(FirstAuthor.name, FirstAuthor.name) + FF)
    print("known = {} , questioned = {} ".format(FirstAuthor.name, SecondAuthor.name) + FS)
    print("known = {} , questioned = {} ".format(SecondAuthor.name, SecondAuthor.name) + SS)
    print("known = {} , questioned = {} ".format(SecondAuthor.name, FirstAuthor.name) + SF)
