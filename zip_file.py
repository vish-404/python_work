import zipfile, os, time, shutil

a = time.time()

# opening new zip file 
exp = zipfile.ZipFile("D:\\vish\\soucre\\new_zip.zip", "w")
exp.write("D:\\vish\\soucre\\Document.rtf", compress_type=zipfile.ZIP_DEFLATED)
# ZIP_DEFAULT is a specific default compression algorthim
# can be used for all type of files
exp.close()

exp = zipfile.ZipFile("D:\\vish\\soucre\\new_zip.zip", "a") # to append
exp.write("D:\\vish\\soucre\\doc.pdf", compress_type=zipfile.ZIP_DEFLATED)
exp.close()

print(exp.namelist())

# now extracton from a zip file
exp = zipfile.ZipFile("D:\\vish\\soucre\\new_zip.zip")
exp.extractall("D:\\vish\\desti")
# this is how to extract all the files to a location
# leave blank to extract at "c:\\" 

exp.extract(exp.namelist()[0], "D:\\vish\\desti")
# extract a particular file

time.sleep(2)
file_txt = exp.getinfo(exp.namelist()[-1])
print(file_txt.file_size,  file_txt.compress_size, file_txt.compress_type)

exp.close()

shutil.rmtree("D:\\vish\\desti")
time.sleep(2)
os.mkdir("D:\\vish\\desti")

time.sleep(2)
os.remove("D:\\vish\\soucre\\new_zip.zip")
time.sleep(2)

# convert just file into .zip rather than whole path
os.chdir("D:\\vish\\soucre")
exp = zipfile.ZipFile("duhh.zip", "w")
exp.write("doc.pdf", compress_type=zipfile.ZIP_DEFLATED)
exp.close()
time.sleep(2)
os.remove("duhh.zip")

z = time.time()
print(z, z - a)
