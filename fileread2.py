with open("/home/rain/Testfolder/BBB.txt", "r") as file:

# 'file.read' and 'line in file' are both very similar ##############################
#    contents = file.read()
#    print(contents)
#    for line in file:
#         line = line.strip()# gets rid of the '\n'
#         print(line)

# 'readlines' turns it into a list of sentences that terminate at '\n')##########################
     lines = file.readlines()
     print(lines)

# This splits the 'lines' elements into words #######################
     for w in lines:
         w = w.split()
         print(w)
         




