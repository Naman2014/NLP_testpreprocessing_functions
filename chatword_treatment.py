# Importing request to access Rishabh Verma's github for chat words list
import requests

# accessing the account and storing them
response=requests.get("https://raw.githubusercontent.com/rishabhverma17/sms_slang_translator/master/slang.txt").text


list_chat_words=response.split("\n")
chat_words_dic={}
for chat_word in list_chat_words:
  if chat_word=="QPSA?	Que Pasa?":
    continue
  chat_words_dic[chat_word.split("=")[0]]=chat_word.split("=")[1]
print(chat_words_dic)

# defining function
def chat_word_conversion(text):  # method to convert the chat words
  new_word=[]
  for word in text.split():
    if word.upper() in chat_words_dic:
      new_word.append(chat_words_dic[word.upper()])
    else:
      new_word.append(word)
  return " ".join(new_word)

# Example for the above
text="Please send this document asap"
print(chat_word_conversion(text))