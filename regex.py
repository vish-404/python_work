import re

# search a string that starts with "You" And ends with "Python"

st = "You are learning Python"
st2 = "You are learning pyhton now"
x = re.search("^You.*Python$", st)
x2 = re.search("^You.*Python$", st2)

if x:
    print("Ohh")
else :
    print("G T H")

if x2:
    print("Ohh")
else :
    print("G T H")

# metacharacters

# "[]"   for a set of character  like  [a-m]  or [a - zA - Z]
#  Example -- [arn]  returns a match where any one character of them is present
#  [0-5][0-9] return match for any no. between (0, 59)
# 

# "\A"   Returns a string which starts with a specified characters  like "\AThe"
# "\Z"   Returns a string which ends with a specified characters   like  "Spine\Z"
# "\b"   Returns a string which starts with a given charecter
# "\B"   return a string which does not starts with a given character
# "\d"   for intergers (0 - 9)
# "\D"   for not an integer
# "\w"   Any letter/numeric digit/underscore character.(Think of this as matching “word” characters.)
# "\W"   Any character that is not a letter, numeric digit, or the underscore character
# "\s"   Any space, tab, or newline character.
# "\S"   Any character that is not a space, tab, or newline.
# "."   for any character like  "he..o"
# "^"   starts with
# "$"   ends with
# "*"   zero or more ouccurrence
# "+"   one or more occurrence
# "{}"  exactly the specified no. of occurrence
# "|"  either or signal
# "()"  capture and group

st = "Python is a very very easy language"
print(re.findall("very", st))
print(re.findall("place", st))

print(re.split("\s", st))
print(re.split("\d", st))
print(re.split("\s", st, 2)) # this the set maxlimit of splits
print(st.find("very"), "\n\n" ) # position of the word..

print(re.sub("\s", "$" , st))  # to replace all the whitespace to dollar sign
print(re.sub("\s", "$" , st, 2), "\n\n")  # to replace first 2 whitespace to dollar sign

print(re.search("rain", st))
print(re.search("very", st))

x = re.search("\s", st)
print("First whitespace is at: ", x.start())


x = re.search(r"\bv\w+", st)
print(x.span())  # gives the position span of first very
print(x.string)
print(x.group()) #  gives the whole worl of the match
