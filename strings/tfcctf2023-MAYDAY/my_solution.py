message="Whiskey Hotel Four Tango Dash Alpha Romeo Three Dash Yankee Oscar Uniform Dash Sierra One November Kilo India November Golf Dash Four Bravo Zero Uniform Seven"

character_dict = {'dash':'-', 'alpha':'A', 'bravo':'B', 'charlie':'C', 
                  'delta':'D', 'echo':'E', 'foxtrot':'F', 'golf':'G', 
                  'hotel':'H', 'india':'I', 'juliet':'J', 'kilo':'K', 
                  'lima':'L', 'mike':'M', 'november':'N', 'oscar':'O', 
                  'papa':'P', 'quebec':'Q', 'romeo':'R', 'sierra':'S', 
                  'tango':'T', 'uniform':'U', 'victor':'V', 'whiskey':'W', 
                  'xray':'X', 'yankee':'Y', 'zulu':'Z', 'zero':'0', 'one':'1',
                  'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6',
                  'seven':'7', 'eight':'8', 'nine':'9'}

my_list = message.split()
answer = []
for i in range(len(my_list)):
    answer.append("*")

for i in range(len(my_list)):
    for j in character_dict:
        if my_list[i].lower() == j:
            answer[i] = (character_dict[j])
            break

def print_string_from_list(s):
    print(''.join(s))
    
print_string_from_list(answer)
