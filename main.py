import Analyse
import getTweets as gt
import processData as pd

A_NAME = 'BarackObama'
B_NAME = 'YouTube'

print("Read "+A_NAME+"'s Tweets")
ATweets = gt.getAllTweetsBy2Authors(A_NAME)
AList = pd.processDatasets(ATweets)
print("Read "+B_NAME+"'s Tweets")
BTweets = gt.getAllTweetsBy2Authors(B_NAME)
BList = pd.processDatasets(BTweets)

print("generate "+A_NAME+"'s object")
A = Analyse.Analyse(AList)
print("generate "+B_NAME+"'s object")
B = Analyse.Analyse(BList)

print("'known = "+A_NAME+" , questioned = "+A_NAME+"' bi-gram analysing")
aa = A.bigramAnalyse(A.questioned2Dict)
print("'known = "+A_NAME+" , questioned = "+B_NAME+"' bi-gram analysing")
ab = A.bigramAnalyse(B.questioned2Dict)
print("'known = "+B_NAME+" , questioned = "+A_NAME+"' bi-gram analysing")
ba = B.bigramAnalyse(A.questioned2Dict)
print("'known = "+B_NAME+" , questioned = "+B_NAME+"' bi-gram analysing")
bb = B.bigramAnalyse(B.questioned2Dict)

print("'known = "+A_NAME+" , questioned = "+A_NAME+"' tri-gram analysing")
aa += A.trigramAnalyse(A.questioned3Dict)
print("'known = "+A_NAME+" , questioned = "+B_NAME+"' tri-gram analysing")
ab += A.trigramAnalyse(B.questioned3Dict)
print("'known = "+B_NAME+" , questioned = "+A_NAME+"' tri-gram analysing")
ba += B.trigramAnalyse(A.questioned3Dict)
print("'known = "+B_NAME+" , questioned = "+B_NAME+"' tri-gram analysing")
bb += B.trigramAnalyse(B.questioned3Dict)

#50以上で真？
#40以下で偽？
print("known = "+A_NAME+" , questioned = "+A_NAME+" " + str(round(aa * 1000 , 5)))
print("known = "+A_NAME+" , questioned = "+B_NAME+" " + str(round(ab * 1000 , 5)))
print("known = "+B_NAME+" , questioned = "+A_NAME+" " + str(round(ba * 1000 , 5)))
print("known = "+B_NAME+" , questioned = "+B_NAME+" " + str(round(bb * 1000 , 5)))
