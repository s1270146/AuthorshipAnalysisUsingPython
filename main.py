import Analyse
import getTweets as gt
import processData as pd

print("Read katy's Tweets")
katyTweets = gt.getAllTweetsBy2Authors('katyperry')
katyList = pd.processDatasets(katyTweets)
print("Read taylor's Tweets")
taylorTweets = gt.getAllTweetsBy2Authors('taylorswift13')
taylorList = pd.processDatasets(taylorTweets)

print("generate katy's object")
katy = Analyse.Analyse(katyList)
print("generate taylor's object")
taylor = Analyse.Analyse(taylorList)

print("'known = katy , questioned = katy' analysing now")
kk = katy.analyse(katy.questionedDict)
print("'known = katy , questioned = taylor' analysing now")
kt = katy.analyse(taylor.questionedDict)
print("'known =  taylor, questioned = katy' analysing now")
tk = taylor.analyse(katy.questionedDict)
print("'known =  taylor, questioned = taylor' analysing now")
tt = taylor.analyse(taylor.questionedDict)

print("known = katy , questioned = katy " + kk)
print("known = katy , questioned = taylor " + kt)
print("known = taylor , questioned = katy " + tk)
print("known = taylor , questioned = taylor " + tt)

