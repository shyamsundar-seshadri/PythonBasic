path = input("Enter filename: ")
splitted = path.split("/")
filename = splitted[-1]
ext = splitted[-1].split('.')[-1]
directories = path.split(filename)
directory = directories[0]
print("ext is ",ext,". \nfilename is ",filename,".\ndirectory is ",directory)
