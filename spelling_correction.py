# importing textblob
from textblob import TextBlob 

# function for correcting sentence
def spelling_correction(text):  
    txtblb=TextBlob(text)
    return txtblb.correct().string

# example for the above
text="ceertain things can not be explaned"
print(spelling_correction(text))