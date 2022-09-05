# TODO: Create a letter using starting_letter.txt

# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("../Mail Merge Project Start/Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

new_names = []
for name in names:
    new = name.strip("\n")
    new_names.append(new)

with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter:
    let = letter.read()
    for name in new_names:
        new_letter = let.replace("[name]", name)
        with open(f"../Mail Merge Project Start/Output/ReadyToSend/{name}Letter.txt", mode="w") as fresh_letter:
            fresh_letter.write(new_letter)
