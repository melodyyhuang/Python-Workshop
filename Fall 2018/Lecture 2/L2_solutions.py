#Warm up: 
#1.
#Find all such numbers which are divisible by 3 but are not a 
#multiple of 5, between 2032 and 3201 (both included).
#Hint: use range(begin, end) & append for lists 
l=[]
for i in range(2032, 3202):
    if (i%3==0) and (i%5!=0):
        l.append(str(i))


#2. 
#Write a function which accepts a sequence of comma-separated 
#numbers from console and generate a list and a tuple which 
#contains every number.
#i.e. 
#Suppose the following input is supplied to the program: 
#34,67,55,33,12,98
#Then, the output should be: ['34', '67', '55', '33', '12', '98']
#Hint: look up split w/ strings 
def separate_Numbers(values): 
	split_values = values.split(",")
	return(split_values)

#3. 
#Write a function such that the input is a list of items, and you want to 
#return only the unique items within that list. 
def uniqueItems(input): 
	return(set(input))


#Exercise: 
#Take the following stirngs: 
s = "Lorem ipsum dolor sit sit amet, consectetur adipiscing elit, \
     sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \
     Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris \
     nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in \
     reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla \
     pariatur. Excepteur sint occaecat cupidatat non proident, sunt in \
     culpa qui officia deserunt mollit anim id est laborum."

#Create a dictionary that contains each word in the string, 
#and the number of times it appears!
#Parse string into list by every space 
s_parsed=s.split(" ")
print("Total number of words: " + str(len(s_parsed)))
print(s_parsed)

set_strings = set(s_parsed)
dict_words ={x: s_parsed.count(x) for x in set_strings}

