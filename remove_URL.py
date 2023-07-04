# Importing RegEx
import re

# function for removing URL
def remove_url(text):
    pattern = re.compile('http://\S+|https://\S+')
    return pattern.sub(r'',text)

# example for the above
text = "check out my github https://github.com/Naman2014"
print(remove_url(text))

# applying on dataset
# df['column_name'] = df['column_name'].apply(lambda x:remove_url(x)) 