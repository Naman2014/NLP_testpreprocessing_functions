# Importing RegEx
import re

# Importing the list of punctuations
import string
exclude = string.punctuation
# print(exclude)

# defining function for removing punctuations
def remove_punctuation(text):
    return text.translate(str.maketrans('','',exclude))

# example for the above
text = "Hello! How are you?"
print(remove_punctuation(text))

# applying on dataset
# df['column_name'] = df['column_name'].apply(lambda x:remove_punctuation(x)) 