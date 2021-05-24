"""
Write python function, sms_encoding() which accepts a sentence and converts it into an abbreviated sentence to be sent as SMS and returns the abbreviated sentence. 

Rules are as follows: 
a. Spaces are to be retained as is 
b. Each word should be encoded separately

If a word has only vowels then retain the word as is

If a word has a consonant (at least 1) then retain only those consonants

Note: Assume that the sentence would begin with a word and there will be only a single space between the words."""
#lex_auth_01269444961482342489

def sms_encoding(data):
    #start writing your code here
    words=data.split()
    final=''
    for word in words:
        lengthofword=len(word)
        if lengthofword>1:
            temp=''
            for char in word:
                if char!='a' and char!='e' and char!='i' and char!='o' and char!='u' and char!='A' and char!='E' and char!='I' and char!='O' and char!='U':
                    temp=temp+char
            final=final+temp+' '
        else:
            final=final+word+' '
    return final.strip()    

data="Have a nice day"
print(sms_encoding(data))