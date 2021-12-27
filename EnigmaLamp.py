from pgl import GCompound, GOval, GWindow, GLabel
from EnigmaConstants import ALPHABET, LAMP_RADIUS,LAMP_BORDER_COLOR,LAMP_BGCOLOR,LAMP_OFF_COLOR,LAMP_ON_COLOR,LAMP_LABEL_DY,LAMP_FONT

class EnigmaLamp(GCompound):
    """ represents one of the keys on the keyboard"""
    def __init__(self, i):
        GCompound.__init__(self)

        self.lamp = GOval(-LAMP_RADIUS, -LAMP_RADIUS, LAMP_RADIUS*2, LAMP_RADIUS*2)
        self.lamp.set_color(LAMP_BORDER_COLOR)
        self.lamp.set_filled(True)
        self.lamp.set_fill_color(LAMP_BGCOLOR)

        self.letter = GLabel(ALPHABET[i], 0, LAMP_LABEL_DY)
        self.letter.set_font(LAMP_FONT)
        self.letter.move(-1*self.letter.get_width()/2, 0)
        self.letter.set_color(LAMP_OFF_COLOR)

        self.add(self.lamp)
        self.add(self.letter)

    def set_state(self, state):
        """setting the state of the lamp color"""
        self.state = state
        if self.state == True:
            self.letter.set_color(LAMP_ON_COLOR)
        if self.state != True:
            self.letter.set_color(LAMP_OFF_COLOR)