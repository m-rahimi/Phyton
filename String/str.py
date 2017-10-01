a = "this is a string"
a = a.split(" ") # a is converted to a list of strings. 
print a
# ['this', 'is', 'a', 'string']

a = "-".join(a)
print a
#this-is-a-string 

#Mutation
string = "abracadabra"
l = list(string)
l[5] = 'k'
string = ''.join(l)
print string
# abrackdabra

string = string[:5] + "k" + string[6:]
