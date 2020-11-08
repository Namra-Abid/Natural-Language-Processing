import nltk
from nltk.corpus import inaugural
from nltk.corpus import stopwords
import os
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import inaugural
from nltk import FreqDist
#nltk.download('stopwords')
from nltk.tokenize import regexp_tokenize
print("-------WARM UP---------")
print("------TASK 1---------")
#using inaugural fileids to list all the documents
documents =inaugural.fileids()
print("Using the corpus reader class list all the documents in inaugural corpus :")
print(documents)
print("---------------------------------------------------------------------")
print("Find the total number of words in Clinton’s 1993 speech :")
#using .worrds method to count words in clinton speech
clintonwords =(inaugural.words('1993-Clinton.txt'))

print(len(clintonwords))
#.raw method will read the text in raw form
s= inaugural.raw('1789-Washington.txt')
w=set(m.group(0) for m in re.finditer(r"\w+",s))
#print (len(re.findall('\w+', s)))
print("Find the total number of distinct words in the same speech :")
#now we will find length of distinct words
print(len(w))
# average function to calculate average word length
def average(numbers):
    return sum(numbers)/len(numbers)
lengths = [len(word) for word in clintonwords]
print ('Find the average word type length of same speech.:')
print(average(lengths))
print("------TASK 2---------")
print("   Obtain the words from the Clinton’s 1993 speech :")
#using .words method to calculate words in speech
print(clintonwords)
print("  Construct a frequency distribution over the lowercased words in the document  :")
#initializinf list for lowercase
lowercasewords=[]
#for loop is used here to convert lowercase
for words in clintonwords:
    if words.islower()==True:
         lowercasewords.append(words)
    else:
        pass
#print(lowercasewords)
#create frequency Distribution object to calculate frequency
frequencydist=FreqDist(lowercasewords)
#print(frequencydist)
print(frequencydist.most_common())

print("Write a function that finds the 50 most frequently occurring words in the speech that are not stop words  :")
#creating list of stopwords
englishstopwords =stopwords.words("english")
frequentlyOccuring=[]

englishcapitalize=[]
#capitalize first letter of stop words and storing it in english capitalize
for words in englishstopwords:
  englishcap=words.capitalize()
  englishcapitalize.append(englishcap)

punctuations=[",",".",'" "',';','-',':','."','"',"'"]
# here for and if loop are used to filter out punctuation and stop words
for words in clintonwords:
    #to filter stop words
    if words not in englishstopwords :
        #to filter stopwords (first letter capitalzie)
        if words not in englishcapitalize:
            #to filter punctuations
           if words not in punctuations :
              frequentlyOccuring.append(words)

    else:
       pass



#print(frequentlyOccuring)
#create Freuency Distribution Class
frequencydist=FreqDist(frequentlyOccuring)
#print 50 frequent words
print(frequencydist.most_common(50))
print("Plot the top 50 words")
#creating plot
frequencydist.plot(50)
print("Find out how many times the words world and america were used in the speech :")
worldcount=frequencydist.pop("world")
americacount=frequencydist.pop('America')
print("Count of America :", americacount)
print("Count of world   :",worldcount)
