import Weight
import Analyse
import getTweets as gt
import processData as pd
from tqdm import tqdm

# 1人目
# 選択されたアカウントのツイートを抽出
FirstAuthorTweets = gt.getAllTweetsBy2Authors(1)
# 抽出したツイートを単語ごとに区切る(Uni-gram)
FirstAuthorList = pd.processDatasets(FirstAuthorTweets['content'])

# 2人目
# 選択されたアカウントのツイートを抽出
SecondAuthorTweets = gt.getAllTweetsBy2Authors(2)
# 抽出したツイートを単語ごとに区切る(Uni-gram)
SecondAuthorList = pd.processDatasets(SecondAuthorTweets['content'])

# ツイートの重さを作成
AllTweetsWeight = Weight.IDF()

firstMiddle = int(len(FirstAuthorList)*0.9)
FirstAuthorWeight = Weight.TF(FirstAuthorList[0 : firstMiddle] , firstMiddle)

secondMiddle = int(len(SecondAuthorList)*0.9)
SecondAuthorWeight = Weight.TF(SecondAuthorList[0 : secondMiddle] , secondMiddle)

# 著者のオブジェクトを作成
FirstAuthor = Analyse.UserAnalyse(FirstAuthorList, FirstAuthorTweets['authorName'])
SecondAuthor = Analyse.UserAnalyse(SecondAuthorList, SecondAuthorTweets['authorName'])

def getN(N) :
    if N == 1: return 'Uni'
    elif N == 2 : return 'Bi'
    elif N == 3 : return 'Tri'

for N in range(1,4) : 
    
    FF = str(round(Analyse.analyse(AllTweetsWeight , FirstAuthorWeight , FirstAuthorList[firstMiddle : len(FirstAuthorList)] , N) , 3))
    FS = str(round(Analyse.analyse(AllTweetsWeight , FirstAuthorWeight , SecondAuthorList[secondMiddle : len(SecondAuthorList)] , N) , 3))
    SF = str(round(Analyse.analyse(AllTweetsWeight , SecondAuthorWeight , FirstAuthorList[firstMiddle : len(FirstAuthorList)] , N) , 3))
    SS = str(round(Analyse.analyse(AllTweetsWeight , SecondAuthorWeight , SecondAuthorList[secondMiddle : len(SecondAuthorList)] , N) , 3))

    print("=======================Result of {}-Gram==========================".format(getN(N)))
    print("known = {} , questioned = {} ".format(FirstAuthor.name, FirstAuthor.name) + FF)
    print("known = {} , questioned = {} ".format(FirstAuthor.name, SecondAuthor.name) + FS)
    print("known = {} , questioned = {} ".format(SecondAuthor.name, SecondAuthor.name) + SS)
    print("known = {} , questioned = {} ".format(SecondAuthor.name, FirstAuthor.name) + SF)

    FirstAuthor.doNGram(N)
    SecondAuthor.doNGram(N)

    FF = FirstAuthor.execute(FirstAuthor.questionedDict)
    FS = FirstAuthor.execute(SecondAuthor.questionedDict)
    SS = SecondAuthor.execute(SecondAuthor.questionedDict)
    SF = SecondAuthor.execute(FirstAuthor.questionedDict)

    print("=======================Count of {}-Gram==========================".format(getN(N)))
    print("known = {} , questioned = {} ".format(FirstAuthor.name, FirstAuthor.name) + FF)
    print("known = {} , questioned = {} ".format(FirstAuthor.name, SecondAuthor.name) + FS)
    print("known = {} , questioned = {} ".format(SecondAuthor.name, SecondAuthor.name) + SS)
    print("known = {} , questioned = {} ".format(SecondAuthor.name, FirstAuthor.name) + SF)
