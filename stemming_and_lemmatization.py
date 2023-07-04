# stemming
from nltk.stem.porter import PorterStemmer
def stem_word(tokens):  # method to convert a token to its stem
  for i in range(0,len(tokens)):
    tokens[i]=PorterStemmer().stem(str(tokens[i]))
  return tokens

# lemmatization
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer=WordNetLemmatizer()
sentence="He was having an amazing game yesterday. He was scoring goals for fun. His dribbling was also amazing."
punctuations=string.punctuation
sentence_words=nltk.word_tokenize(sentence)
for word in sentence_words:
  if word in punctuations:
    sentence_words.remove(word)
