# File: EnigmaMachine.py

"""
This module is the starter file for the EnigmaMachine class.
"""

from EnigmaConstants import ALPHABET, KEY_LOCATIONS, LAMP_LOCATIONS, ROTOR_LOCATIONS, ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION
from pgl import GImage
from EnigmaKey import EnigmaKey
from EnigmaLamp import EnigmaLamp
from EnigmaRotor import EnigmaRotor, apply_permutation, invert_key


# Class: EnigmaMachine

class EnigmaMachine():
    """
    This class is responsible for storing the data needed to simulate
    the Enigma machine.  If you need to maintain any state information
    that must be shared among different parts of this implementation,
    you should define that information as part of this class and
    provide the necessary getters, setters, and other methods needed
    to manage that information.
    """

    def __init__(self, gw):
        """
        The constructor for the EnigmaMachine class is responsible for
        initializing the graphics window along with the state variables
        that keep track of the machine's operation.
        """
        image = GImage("images/EnigmaTopView.png")
        gw.add(image)
        for i in range(26):
            key = EnigmaKey(i)
            gw.add(key, KEY_LOCATIONS[i][0],KEY_LOCATIONS[i][1])
        
        self.lamps = []
        for i in range(26):
            lamp = EnigmaLamp(i)
            lamp.set_location(LAMP_LOCATIONS[i][0],LAMP_LOCATIONS[i][1])
            gw.add(lamp)
            self.lamps.append(lamp)

        self.rotors = []
        for i in range(3):
            rotor = EnigmaRotor(i, ROTOR_PERMUTATIONS[i])
            rotor.set_location(ROTOR_LOCATIONS[i][0],ROTOR_LOCATIONS[i][1])
            gw.add(rotor)
            self.rotors.append(rotor)


    def key_pressed(self,letter):
        """Function that runs when the user clicks the key"""
        index = ALPHABET.index(letter)

        carry = self.rotors[2].advance()
        if carry:
            carry = self.rotors[1].advance()
            if carry:
                carry = self.rotors[0].advance()

        #fast rotor
        index = apply_permutation(index, ROTOR_PERMUTATIONS[2], self.rotors[2].get_offset())
        #medium rotor
        index = apply_permutation(index, ROTOR_PERMUTATIONS[1], self.rotors[1].get_offset())
        #slow rotor
        index = apply_permutation(index, ROTOR_PERMUTATIONS[0], self.rotors[0].get_offset())

        #reflector
        index = apply_permutation(index, REFLECTOR_PERMUTATION, 0)
        
        #reverse order for way back
        #slow rotor
        index = apply_permutation(index,invert_key(ROTOR_PERMUTATIONS[0]),self.rotors[0].get_offset())
        #medium rotor
        index = apply_permutation(index,invert_key(ROTOR_PERMUTATIONS[1]),self.rotors[1].get_offset())
        #fast rotor
        index = apply_permutation(index,invert_key(ROTOR_PERMUTATIONS[2]),self.rotors[2].get_offset())
        
        new_key = ALPHABET[index]
        lamp = self.lamps[index]
        lamp.set_state(True)



    def key_released(self,letter):
        """Function that runs when the user releases the key"""
        for i in range(26):
            index = ALPHABET.index(ALPHABET[i])
            lamp = self.lamps[index]
            lamp.set_state(False)


            



