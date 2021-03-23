import json
import difflib
from difflib import get_close_matches # -> gets "close enough" matches to a word. This is in case the user mistypes a word -> "rainn" when looking for "rain" -> Could this be used for an auto-correct type function

data = json.load(open("data.json"))

def translate(w): # -> Define a function to run all the code below when called
    if w in data:
        return data[w] # -> If the word the user enters is in the JSON file. Return the definition
    elif len(get_close_matches(w, data.keys())) > 0: # -> If the user mistypes, find the closest match and ask if the user meant that word. If 'Y' return the definition. If 'N' say the word doesn't exist
        yes_no = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0]).upper()

        if yes_no == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yes_no == "N":
            return "The word doesn't exist. Please double check it." # -> If the user enters a word that doesn't exist in the JSON return a message telling them so
    else:
        return "We didn't understand your entry." # -> If the user gets to this point, tell them we didn't understand their entry

word = input("Enter a word: ").lower() # -> Convert word to lower in case user entered in all caps or title case
output = translate(word)

if type(output) == list: # -> If the user enters a word that we don't understand, make sure the output is printed properly. 
    for item in output:
        print(item)
else:
    print(output)