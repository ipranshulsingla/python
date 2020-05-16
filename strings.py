# strings are collection of characters eg ram,shyam,user_name,hunter007
# strings representation
# "", '' , """ """-> Multiline String

var1="Ram"
var2='Ram\nShyam'
var3="""Ram
Shyam"""

# for <control_variable> in <sequence/collection>
spaceCount=0
vowelsList=['a','e','i','o','u','A','E','I','O','U']
vowelsCount=0
strCollection='Jai Sethi'
for character in strCollection:
    if(character==' '):
        spaceCount+=1
    elif(character in vowelsList):
        vowelsCount+=1
print("Word Count:",spaceCount+1)
print('Vowels Count:',vowelsCount)