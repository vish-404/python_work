import shutil, os , time

source_a = "D:\\vish\\soucre\\Document.rtf" # a file which is to work on
source_b = "D:\\vish\\soucre\\doc.pdf"
destination = "D:\\vish\\desti" # new disered loocation of source... 
shutil.copy(source_a, destination) # to copy any type of files...
# "shutil.copytree(source, destination)" is used to copy all the file of a folder to another

shutil.move(source_b, destination) # works as cut ...

shutil.copy("D:\\vish\\desti\\doc.pdf", "D:\\vish\\soucre\\document.pdf")
# to copy and rename simultaneously .. can be used in shutil.move()
os.rename("D:\\vish\\soucre\\document.pdf", "D:\\vish\\soucre\\doc.pdf")

print(os.listdir(destination), "\n")

time.sleep(5) # to pause the program for some time (in seconds)

for i in os.listdir(destination):
    os.unlink(destination + "\\" + i)  # to delete a perticular file pe permanentaly 

#  shutil.rmtree()  to delete  all the files in target folder(+ its content) permanentaly
#  use os.unlink() 
#  use os.rmdir() to delete a perticular empty folder pe permanentaly 

print(os.listdir(destination), "\n")

