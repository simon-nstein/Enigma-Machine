from pgl import GCompound, GOval, GWindow, GLabel, GRect
from EnigmaConstants import ROTOR_BGCOLOR, ROTOR_WIDTH,ROTOR_HEIGHT,ROTOR_COLOR,ROTOR_LABEL_DY,ROTOR_FONT, ALPHABET

class EnigmaRotor(GCompound):
    """ represents one of the keys on the keyboard"""
    def __init__(self, i, permutation):
        GCompound.__init__(self)

        self.permutation = permutation
        self.offset = 0

        self.rotor = GRect(-ROTOR_WIDTH/2, -ROTOR_HEIGHT/2, ROTOR_WIDTH,ROTOR_HEIGHT)
        self.rotor.set_color(ROTOR_BGCOLOR)
        self.rotor.set_filled(True)

        self.letter = GLabel("A", 0, ROTOR_LABEL_DY)
        self.letter.set_font(ROTOR_FONT)
        self.letter.move(-1*self.letter.get_width()/2, 0)

        self.add(self.rotor)
        self.add(self.letter)

    def click_action(self, enigma):
        carry = self.advance()

    def advance(self):
        if self.offset < 25:
            self.offset += 1
            self.letter.set_label(ALPHABET[self.offset])
            return False
        else:
            self.offset = 0
            self.letter.set_label(ALPHABET[self.offset])
            return True
    
    def get_offset(self):
        return self.offset
    
def apply_permutation(index, permutation, offset):
    """computes the index of the letter after shifting it by the offset"""
    letter_index = index + offset
    #wrapping around
    if letter_index > 25:
        letter_index -= 26

    #Look up the character at that index in the permutation string
    new_letter = permutation[letter_index]

    #Return the index of the new character after subtracting the offset
    encrypted_index = ALPHABET.index(new_letter)
    new_index = encrypted_index - offset
    #wrapping around
    if new_index < 0:
        new_index += 26

    return new_index

def invert_key(permutation):
    """take an initial permutation string as input return the inverted keys a string"""
    invert_key = ""
    for i in range(26):
        alphabet_letter = ALPHABET[i]
        permutation_index = permutation.index(alphabet_letter)
        inverted_letter = ALPHABET[permutation_index]
        invert_key += inverted_letter
    return invert_key



    

        