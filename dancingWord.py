'''
Created on 2016. 7. 5.
@author: mulder
'''
    
def makeDancing(strings):
    listed_strings = list(strings)
    cap_flag = 'U'
    
    for key in range(len(listed_strings)):
        if cap_flag == 'U':
            if listed_strings[key] == " ":
                cap_flag = 'U'
            else:
                listed_strings[key] = listed_strings[key].upper()
                cap_flag = 'L'
        elif cap_flag == 'L':
            if listed_strings[key] == " ":
                cap_flag = 'L'
            else:
                listed_strings[key] = listed_strings[key].lower()
                cap_flag = 'U'
    dancing_word = "".join(listed_strings)
    return dancing_word

print(makeDancing('This is a dancing words'))
