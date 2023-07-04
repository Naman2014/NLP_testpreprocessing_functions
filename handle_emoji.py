# import RegEx
import re

# function for removing emojis
def remove_emoji(string):  # method to remove emoji
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F" # emoticons
                           u"\U0001F300-\U0001F5FF" # symbols & pictographs
                           u"\U0001F680-\U0001F6FF" # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF" # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

# example
print(remove_emoji("Hilarious 😂! The feeling of making a sale 😎, The feeling of actually fulfilling orders 😒"))


# functiomn for giving emoji its meaning
import emoji
def replace_emoji_with_meaning(text):  # method to replace emoji with its meaning
  return emoji.demojize(text).replace(':','').replace('_',' ')  # We have replaced the ':', and '_' characters as these are the by-products of emoji-text conversion

print(replace_emoji_with_meaning("Hilarious 😂! The feeling of making a sale 😎, The feeling of actually fulfilling orders 😒"))
     
