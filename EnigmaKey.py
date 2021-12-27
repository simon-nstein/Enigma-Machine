from pgl import GCompound, GOval, GWindow, GLabel
from EnigmaConstants import KEY_LOCATIONS, KEY_RADIUS, KEY_BORDER, KEY_BGCOLOR, KEY_BORDER_COLOR, ALPHABET, KEY_FONT, KEY_LABEL_DY, KEY_UP_COLOR, KEY_DOWN_COLOR

class EnigmaKey(GCompound):
    """ represents one of the keys on the keyboard"""
    def __init__(self, i):
        GCompound.__init__(self)
        self.key = GOval(-KEY_RADIUS, -KEY_RADIUS, KEY_RADIUS*2, KEY_RADIUS*2)
        self.key.set_color(KEY_BORDER_COLOR)
        self.key.set_filled(True)
        self.key.set_line_width(KEY_BORDER)
        self.key.set_fill_color(KEY_BGCOLOR)

        self.letter = GLabel(ALPHABET[i], 0, KEY_LABEL_DY)
        self.letter.set_font(KEY_FONT)
        self.letter.move(-1*self.letter.get_width()/2, 0)
        self.letter.set_color(KEY_UP_COLOR)

        self.actual_letter = ALPHABET[i]

        self.add(self.key)
        self.add(self.letter)

    def mousedown_action(self,enigma):
        """If the  key is clicked on, key will turn red"""
        self.letter.set_color(KEY_DOWN_COLOR)
        enigma.key_pressed(self.actual_letter)

    def mouseup_action(self,enigma):
        """If the  key is clicked on, key will turn red"""
        self.letter.set_color(KEY_UP_COLOR)
        enigma.key_released(self.actual_letter)


        
