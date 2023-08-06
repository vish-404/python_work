import os
a = os.getcwd()  # for current working directory
print(a) 
os.chdir("D:\\books")# for changing the directory
print(os.getcwd()) 
print(os.path.abspath(".\\python") ) # line 13 just to say not to check the existance of file
print(os.path.exists(os.path.abspath(".\\python")),"\n")# to check the existance of file/dir
os.chdir(a)

# os.makedirs(a + "\haramkhor") # to make new directories
print("Main dir .. ", os.path.abspath(".."), "\nWorking dir .. ",  os.path.abspath("."))
print(os.path.isabs(".") , os.path.isabs(a), "\n") # to check the path

a = os.path.abspath(".\\python") # to get absolute path
print(a, "\n" , os.path.basename(a) ,"  ",  os.path.dirname(a))
print(os.path.split(a)) #gives tuple (dirname, basename)
print(a.split(os.path.sep)) #spliting at each level
print(os.path.relpath(a, "D:\pro books"), "\n")  # relative path (directional view)

print(os.path.getsize(a)) # to get the size of dir or file in bytes
print(os.listdir(a))  # to get the content of dir
print(os.path.isdir(a)) # to check whether the string is dir or not (for file i.e. "isfile()"")
c = 0
for b in os.listdir(a):
    c += os.path.getsize(os.path.join(a , b))
print(c, "\n") # to get the joined path of dir and file  -- os.path.join(a, b) 

