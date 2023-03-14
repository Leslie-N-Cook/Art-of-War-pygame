"""
    Author:   Byron Dowling
    Class:    5443 2D Python Gaming
"""

import copy
import os
import pprint
from random import shuffle

"""
    Object definition to hold sprite information

    Is necessary primarily because the sprite functions have a differing
    number of frames such as Idle being 6 frames but attack being 8 etc.
"""
characterSprite = {
    "Name": "",
    "Screen Name": "",
    "Action": {
        "Attack": {
            "imagePath": "",
            "frameCount": .0001
        },

        "Die": {
            "imagePath": "",
            "frameCount": .0001
        },

        "Idle": {
            "imagePath": "",
            "frameCount": .00001
        },

        "Jump": {
            "imagePath": "",
            "frameCount": .0001
        },

        "Move": {
            "imagePath": "",
            "frameCount": .0001
        }
    }
}


## To be used for pseudo-random character selection
class PlayerSelector:

    def __init__ (self):
        self.characters = ["Knight1", "Knight2", "Knight3", "Viking1", "Viking2", "Pirate"]
        self.warriorNames = ["A Holy Crusader Knight", "A Knight from the Feudalism Era", 
        "A Roman Gladiator", "A Norseman", "A Viking Raider", "A 17th Century Pirate Raider"]
        self.characterSprites = []

        self.loadCharacters()

    def loadCharacters(self):
        for i in range(len(self.characters)):
            characterSprite["Name"] = self.characters[i]
            characterSprite["Screen Name"] = self.warriorNames[i]
            characterSprite["Action"]["Attack"]["imagePath"] = fr'Sprites/{self.characters[i]}/Attack'
            characterSprite["Action"]["Attack"]["frameCount"] = len(os.listdir(characterSprite["Action"]["Attack"]["imagePath"]))
            characterSprite["Action"]["Die"]["imagePath"] = fr'Sprites/{self.characters[i]}/Die'
            characterSprite["Action"]["Die"]["frameCount"] = len(os.listdir(characterSprite["Action"]["Die"]["imagePath"]))
            characterSprite["Action"]["Idle"]["imagePath"] = fr'Sprites/{self.characters[i]}/Idle'
            characterSprite["Action"]["Idle"]["frameCount"] = len(os.listdir(characterSprite["Action"]["Idle"]["imagePath"]))
            characterSprite["Action"]["Move"]["imagePath"] = fr'Sprites/{self.characters[i]}/Move'
            characterSprite["Action"]["Move"]["frameCount"] = len(os.listdir(characterSprite["Action"]["Move"]["imagePath"]))

            self.characterSprites.append(copy.deepcopy(characterSprite))

    def sanityCheck(self):
        pp = pprint.PrettyPrinter(depth=4)
        pp.pprint(self.characterSprites)

    def chooseSprites(self):
        shuffle(self.characterSprites)
        selection = []
        selection.append(self.characterSprites[0])
        selection.append(self.characterSprites[1])

        return selection


if __name__ == '__main__':
    
    C4 = PlayerSelector()
    C4.loadCharacters()
    # C4.sanityCheck()

    sprites = C4.chooseSprites()
    player1 = sprites[0]
    player2 = sprites[1]

    pp = pprint.PrettyPrinter(depth=4)
    pp.pprint(sprites)


