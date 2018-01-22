
#Problem 2: String Operations (Weight 1) Create a string that contains the following: “I”, “love”,
#“learning”, “how”, “to”, “code”, and “!”. Use string operators to create a syntactically correct sentence
#(stored in variable text) that yields “I love learning how to code!” when printed to the user. Print the
#content of text.

s = "!edoc ot woh gninrael evol I"
text = s[-1:-(len(s)+1):-1]
print(text)

x = "aIa alaoavaea alaeaaaranaianaga ahaoawa ataoa acaoadaea!"
text = x[1:len(x):2]
print(text)


#More strictly using string operators
text = 'I '+'love '+'learning '+'how '+'to '+'code'+'!'
print(text)