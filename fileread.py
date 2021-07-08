"""Using the 'with' statement which automatically closes files.  I have added a try/except block too which adds more checks to it.
"""

try:
    with open("/home/rain/cfolder/file.txt", "r") as file:
        #print out all lines(includes \n):
        #for line in file.readlines():
        #    print(line)

        #Strip away all whitespace:
        #for line in file:
        #    line = line.strip()
        #    print(line)

        #prints contents, as is, ignoring \n:
        contents = file.read()
        print(contents)

except FileNotFoundError:
    print("Error opening file!")
finally:
    if file.closed == False:
        print("File is not closed")
    else:
        print("***File is closed***")

#file.close()

