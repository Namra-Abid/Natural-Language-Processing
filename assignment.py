import pandas as pd
from nltk.tokenize import word_tokenize
import re
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk import FreqDist
#to remove different kind of emojis
def cleanstring(raw_text):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_text)
  return cleantext
#to remove emojis
def remove_emoji(string):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"

                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

#reading csv file
csv_tweet=pd.read_csv('tweets.csv',header=None,engine='python')
print(csv_tweet)

print("QUESTION 1 : TOKENIZATION")
arrayoftweets=list(csv_tweet[1])
#print(arrayoftweets)
#making list a string using join method to tokenize it
tweets="".join(arrayoftweets)
#print(tweets)
tokenzietweets=word_tokenize(tweets)

print(tokenzietweets)
print("Convert all the text in tweets.cvs to lower case letters")
print("QUESTION 2 : TEXT NORMALISATION (TEXT PRE-PROCESSING)")
#coverting tweets.csv to lower case
print("----LOWERCASED----")
print("Convert all the text in tweets.cvs to lower case letters")
lowercasetweets = csv_tweet[1].str.lower()
print(lowercasetweets)
print("==============")
#print(lowercasetweets)
# converting and overwriting values in column
# display
print("----------WITHOUT EMOTICONS AND SLANG WORDS----")
print("removing all the emoticons and slang words")
ltweets=list(lowercasetweets)
withoutemojis=[]
#print(ltweets)
print(len(ltweets))

for tw in ltweets:
    r=(remove_emoji(tw)).strip()
    withoutemojis.append((cleanstring(r)))
print(withoutemojis)
print("-----------WITHOUT STOP WORDS---------")
#generating stopwords of english
englishstopwords =stopwords.words("english")
print("==============")

print("removing stopwords")
withoutStopWords=[]
for sentences in withoutemojis:
    querywords = sentences.split()
    resultwords  = [word for word in querywords if word.lower() not in englishstopwords]
    result=' '.join(resultwords)

    withoutStopWords.append(result)
print(withoutStopWords)
print(len(withoutStopWords))

#following code is written to show how unnecessary punctuation is removed
print("REMOVING UNNECESSARY PUNCTUATION")
print("==============")
withoutpuncA=[]
patterna = ['[^!);&#$â€,%""’…]+ ']
#function to remove punctuation
def remove_punctuation(pattern, phrase):
    for pat in pattern:
        return (re.findall(pat, phrase))
        return ('\n')

for words in withoutStopWords:
     withoutpunc=("".join(remove_punctuation(patterna,words)))
     withoutpuncA.append(withoutpunc)
print(withoutpuncA)
#Following lines of code are written to remove numbers
print("REMOVING NUMBERS")
print("==============")
withoutNumber=[]
for words in withoutpuncA:
    #code to remove number from 0 to 9 and @ sign
    withoutnum=re.sub('[0-9@]+', '', words)
    withoutNumber.append(withoutnum)
print(withoutNumber)

print("REMOVING URLS")
print("==============")
withoutURL=[]
#following code is written to remove url from tweets
for sentences in withoutNumber:
    e = r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*'
    URLless_string = re.sub(e, '', sentences)
    withoutURL.append(URLless_string)
print(withoutURL)

CorrectedList=withoutURL
df=pd.DataFrame({"Corrected Tweets":CorrectedList})
df.to_csv("corrected_tweets.csv")

print("-QUESTION 3 : STEMMING WORDS")
#tokenize the words first
wordtokens=word_tokenize("".join(CorrectedList))
#print(wordtokens)
print("--------------------------------------------------------")
stemmed=[]
#making potterstammer object
ps=PorterStemmer()
for words in wordtokens:
    #passing words to get them stemmed
    stemmed.append(ps.stem(words))
print(stemmed)
print("-QUESTION 4 : FREQUENCY DISTRIBUTION")
#applying frequency distribution on unstemmed words
print("-------find and print the top 20 most frequent (unique words) from unstemmed words ")
frequent=FreqDist(wordtokens)
print(frequent.most_common(20))

#applying frequency distribution on stemmed words
print("-----find and print the top 20 most frequent (unique words) from stemmed words")
frequent1=FreqDist(stemmed)
print(frequent.most_common(20))
frequent.plot(20,title='Frequency Distribution Unstemmed Words')
frequent1.plot(20,title='Frequency Distribution stemmed Words')
