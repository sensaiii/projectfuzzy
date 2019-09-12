import operator
from fuzzywuzzy import process
wordlist=[]
word_count={}
with open('word_search.tsv') as data:       #opning the tsv file as databases
     for x in data:
         word,count=x.split("\t")          #spliting the word and occurence
         wordlist.append(word)
         word_count[word]=int(count.strip()) #removing extra spaces and converting into int type and adding

#checking wheather the word in words
def search(val):
    result=[]
    for word in wordlist:
        if value in word:
            result.append(word)
    return result

#This part sorts the words based on a match with the search keyword.
# 1. Matches at the start of a word ranks higher.
# 2. Common words (those with a higher usage count) ranks higher than rare words.
# 3. Short words ranks higher than long words.
# 4. An exact match always ranks as the first result.
#returns top 25 results based percenrage of matching 100 to be heighest
def sorting(results,incomplete_word,limit=25):
    results=process.extract(incomplete_word,results,limit=limit)
    return results
