# import nltk
import nltk
from nltk.corpus import stopwords

# storing all stopwords 
stop_words = stopwords.words("english")

# defining functions for the above
def remove_stopwords(text):
    new_word=[]
    for word in text.split():
        if word.lower() in stop_words:
            new_word.append('')
        else :
            new_word.append(word)
    return " ".join(new_word)

# example for the above
text = "He is very nice and handsome"
print(remove_stopwords(text)) 

