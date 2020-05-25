#import nltk
import csv

reader = csv.reader(open('untranslatable.csv', 'r', encoding='utf8'))
untranslatable_words = {}
for row in reader:
	k, v = row[:2]
	print(k,v)
	untranslatable_words[k] = v

