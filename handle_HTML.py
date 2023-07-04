# Importing RegEx
import re

# function for removing HTML
def remove_html_tags(text):
    pattern = re.compile('<.*?>')
    return pattern.sub(r'',text)

# example for the same
text = "This is your url<p>Please check on this </p> <a href ='http://google.com'>Google</a>"
print(remove_html_tags(text))

# applying on dataset
# df['column_name'] = df['column_name'].apply(lambda x:remove_html_tags(x)) 