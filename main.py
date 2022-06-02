import Weight
import Analyse
import getTweets as gt
import processData as pd
from tqdm import tqdm

# Read first author Tweets
FirstAuthorTweets = gt.getAllTweetsBy2Authors(1)
FirstAuthorList = pd.processDatasets(FirstAuthorTweets['content'])

# Read second author Tweets
SecondAuthorTweets = gt.getAllTweetsBy2Authors(2)
SecondAuthorList = pd.processDatasets(SecondAuthorTweets['content'])

# generate weights
AllTweetsWeight = Weight.IDF()
AsplitIdx = int(len(FirstAuthorList)*0.9)
FirstAuthorWeight = Weight.TF(FirstAuthorList[0 : AsplitIdx] , AsplitIdx)
BsplitIdx = int(len(SecondAuthorList)*0.9)
SecondAuthorWeight = Weight.TF(SecondAuthorList[0 : BsplitIdx] , BsplitIdx)

# generate first author object
FirstAuthor = Analyse.UserAnalyse(FirstAuthorList, FirstAuthorTweets['authorName'])
# generate second auther object
SecondAuthor = Analyse.UserAnalyse(SecondAuthorList, SecondAuthorTweets['authorName'])

def getN(N) :
    if N == 1: return 'Uni'
    elif N == 2 : return 'Bi'
    elif N == 3 : return 'Tri'

for N in range(1,4) : 
    
    if N == 1:
        """
        do N-gram and analyze using weight
        """
        FF = str(round(Analyse.analise(AllTweetsWeight , FirstAuthorWeight , FirstAuthorList[AsplitIdx : len(FirstAuthorList)] , 1) , 3))
        FS = str(round(Analyse.analise(AllTweetsWeight , FirstAuthorWeight , SecondAuthorList[BsplitIdx : len(SecondAuthorList)] , 1) , 3))
        SF = str(round(Analyse.analise(AllTweetsWeight , SecondAuthorWeight , FirstAuthorList[AsplitIdx : len(FirstAuthorList)] , 1) , 3))
        SS = str(round(Analyse.analise(AllTweetsWeight , SecondAuthorWeight , SecondAuthorList[BsplitIdx : len(SecondAuthorList)] , 1) , 3))

    else:
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
#>>>>>>> ea7a52b549438add5846865a8ab3cce0e501776a
