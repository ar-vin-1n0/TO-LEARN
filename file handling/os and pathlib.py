#OS module

#os module interacts with operating system,files,paths,directories,environment variables,processes

import os

print(os.getcwd()) #shows current working directory

os.chdir("C:/Users/aravind/Desktop") #change the current directory to the give directory

print(os.listdir("C:/Users/aravind/Desktop")) #gives a list out of file in the directory

os.mkdir("new_folder") #create new folder/directory

os.makedirs("projects/python/dsa") #creates nested folders/directories

os.rmdir("new_folder") #removes the give folder

os.removedirs("projects/python/dsa") #removes nested folders

os.rename("old.txt", "new.txt") #renames a file

os.remove("data.txt") #delete files

os.path.exists("data.txt") #to check if a file exists or not

os.path.getsize("data.txt")  #give the size of the file

os.path.isfile("data.txt") #check if the given object is a file or not

os.path.isdir("data.txt") #check if the given object is a directory of not

path = os.path.join("folder", "data.txt") #to join a file to a folder'

print(os.path.split(path)) #split a file from a folder

os.path.abspath("data.txt") #returns absolute path

os.getenv("USERNAME") #stores api keys , configs,paths etc

for root, dirs, files in os.walk("project"):

    print(root)
    print(dirs)
    print(files)

#os walk() is used to fetch a directory and know its sub dirs ,files,and root



#PATHLIB MODULE

#pathlib is more simple a advanced module than os it has clearner syntax which makes it more readable and it is object-oriented


from pathlib import Path

path = Path("data.txt") #creates path object rather than strings

path.exists() #check if it exists

path.is_dir()  #check if its a directory

path.is_file()  #check if its a file

path.cwd() #current working directory

path.home() #give home dir path

Path("new_folder").mkdir() #create a new folder/dir

Path("a/b/c").mkdir(parents=True) #creates nested dirs

path = Path("folder") / "data.txt" #join a file or dir to another dir/folder

path.name #gives file name with extension

path.stem #give only name not the extension

path.suffix #give the extension fo the file

path.parent #gives parent dir

path.resolve() #absolute path

path.read_text() #reads the content from the file

path.write_text("hello") #writes to file

path.read_bytes() #reads binary

path.write_bytes() #writes binary to file

#iteration of directory
for item in Path(".").iterdir():
    print(item)

#recursive glob find all need file from a dir even if it is  nested dir
for file in Path(".").rglob("*.py"):
    print(file)




