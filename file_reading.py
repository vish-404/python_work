location = input("Give the location of file : ")
# 'w' also makes file if it doesn't exists
hifile = open(location, 'w')  # this one writes in file from starting 
hifile.write("fuck off!\n")
hifile.close()


hifile = open(location , 'r')  # second input define the aim of opening 
# second input 'r' is for reading , 'a' is for append

#print(hifile.readline())  #  reads a single line
print(hifile.readlines()) # reads lines as element of list
#print(hifile.read()) # read file just as they are
hifile.close()

hifile = open(location, 'a')
hifile.write("chala ja sbdk")
hifile.close()


hifile = open(location, 'r')
print(hifile.read())
hifile.close

