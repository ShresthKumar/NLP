import nltk
nltk.download('nps_chat')
nltk.download('webtext')
nltk.download('popular')
nltk.download('brown')
from nltk.book import *
from nltk.corpus import inaugural
text = inaugural.words(fileids='2009-Obama.txt')
fd = nltk.FreqDist(text)
fd
confd = ConditionalFreqDist((len(word),word) for word in text)
confd[5]
import jieba
seg = jieba.cut("他今天晚上不来参加宴会了，对吗？",cut_all = True)
print(" ".join(seg))
sent = 'Become an expert in NLP'
words = nltk.word_tokenize(sent)
print(words)
text2 = "Cristiano Ronaldo dos Santos Aveiro GOIH ComM (Portuguese pronunciation: [kɾiʃˈtjɐnu ʁɔˈnaɫdu]; born 5 February 1985) is a Portuguese professional footballer who plays as a forward for Saudi Professional League club Al Nassr and captains the Portugal national team."
sentences = nltk.sent_tokenize(text2)
sentences
for sentence in sentences:
 words = nltk.word_tokenize(sentence)
 print(words)
 tagged = nltk.pos_tag(words)
 print(tagged)