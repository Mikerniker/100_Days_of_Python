#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# f = open("./Mail Merge Project Start/Names/invited_names.txt", "r")
#
# print(f.readlines())
# import os
#
# path = r"D:/pythonProject/day-24-start/Mail_merge/Mail Merge Project Start/Input/Names"
# assert os.path.isfile(path)
# with open(path, "r") as f:
#     contents = f.read()
#     print(contents)
with open("D:/pythonProject/day-24-start/Mail_merge/Mail Merge Project Start/Input/Names") as file:
    contents = file.read()
    print(contents)
