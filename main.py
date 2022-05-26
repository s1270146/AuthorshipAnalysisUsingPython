import getTweets as gt
import ngram as ng
import processData as pd

katyTweets = gt.getAllTweetsBy2Authors('katyperry')

# print(ng.n_gram(katyTweets[2], 2))
katyList = pd.processDatasets(katyTweets)
print("analysis katyperry's 10 tweets")
print("----------------------------------------------")
for i in range(10):
    print("Text : ",katyTweets[i])
    print("unigram : ",katyList[i])
    print("bigram : ",ng.doNGram(katyList[i],2))
    print("trigram : ",ng.doNGram(katyList[i],3))
    print("----------------------------------------------")
