import ure

morse_trans = {
'a':[0,1],
'b':[1,0,0,0],
'c':[1,0,1,0],
'd':[1,0,0],
'e':[0],
'f':[0,0,1,0],
'g':[1,1,0],
'h':[0,0,0,0],
'i':[0,0],
'j':[0,1,1,1],
'k':[1,0,1],
'l':[0,1,0,0],
'm':[1,1],
'n':[1,0],
'o':[1,1,1],
'p':[0,1,1,0],
'q':[1,1,0,1],
'r':[0,1,0],
's':[0,0,0],
't':[1],
'u':[0,0,1],
'v':[0,0,0,1],
'w':[0,1,1],
'x':[1,0,0,1],
'y':[1,0,1,1],
'z':[1,1,0,0],
'0':[1,1,1,1,1],
'1':[0,1,1,1,1],
'2':[0,0,1,1,1],
'3':[0,0,0,1,1],
'4':[0,0,0,0,1],
'5':[0,0,0,0,0],
'6':[1,0,0,0,0],
'7':[1,1,0,0,0],
'8':[1,1,1,0,0],
'9':[1,1,1,1,0]
}

def validate_input(response):
  return ure.match("^[a-zA-Z0-9]+$", response)
  
def get_morse_char(character):
  char = character.lower()
  if char not in morse_trans:
    return None
   
  return morse_trans[char]
   
