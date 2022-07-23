#regular expresion
# in computing a regular exoreison, also referred to as "regex" or "regexp" 
#provides a concise and flexible means for matching string of text, such as
#particular characters, words , or patterns of characters. A regular expression is 
#writen in a formal languaje that can be interpreted by a regular expression processor 



#Undestanding Regular Expresssion 
#Very powerful and quite crytic
#Fun Once you understan them
#Regular expressions are a languaje unto thenselves
#A languaje of "marker characters"- programming with 
#it is kind of an "ol school" languaje - compact
#(lenguaje de vieja escuela muy poderoso y divertido)

#Rhe regular expression module 

#using re.search() like startswith()

#we fine-tune whats is matched by adding special characters to the sstring
import re
from xml.dom.pulldom import CHARACTERS
hand = open('filetext.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From:') :
        print(line)

hand = open('filetext.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line) :
        print(line)

#wild-card CHARACTERS-
#the dot characters matches any characters
# if you add the asterisk character, the characters is "any number of times" 

#X.*  /////CUAL QUIER CANTIDAD DE N VECES


#Depending on how "clean" your data is and the porpuse of your 
#application , you ,ay want to narrow your match down a bit 


#X-\S+  reducir la councidencia, match any non- whiteespace character
#       coincide con cualquier caracter que no sea un esoacio en blanco






