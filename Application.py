# -*- coding: UTF-8 -*-

import random

class Game:
    name = ""
    throwsLeft = 0
    bonesCount = 0
    currentMove = 1 #1 - PC, -1 - Player
    
    curThrowScoresPC = 0
    curThrowScoresPl = 0
    
    Bones = []
    finalScoresTable = []
    
    replayKey = "r"
    backToMenuKey = "b"
    exiteKey = "x"
    
    maxThrows = 3
    maxBones = 3
    
    bonesSprites = ["###\n#0#\n###", "0##\n###\n##0", "0##\n#0#\n##0", "0#0\n###\n0#0", "0#0\n#0#\n0#0", "000\n###\n000"]
           
    def setName(self, PlayerName):
        self.name = PlayerName
        
    def setThrowsCount(self, Count):
        self.throwsLeft = Count
        
    def setBonesCount(self, Count):
        self.bonesCount = Count
        
    def storeScores(self):
        self.finalScoresTable += [self.curThrowScoresPl, self.curThrowScoresPC]
        
    def setPlScores(self, scores):
        self.curThrowScoresPl = scores
        
    def setPCScores(self, scores):
        self.curThrowScoresPC = scores
        
    def coinToss(self):
        self.currentMove = random.choice([-1,1])
        
    def throwBones(self):
        self.Bones = []
        for i in range(self.bonesCount):
            self.Bones.append(random.randint(1, 6))
        
    def showBones(self):
        for i in self.Bones:
            print("index:" + str(i))
            print("bone side: " + str(self.Bones[i]))
            print(self.bonesSprites[self.Bones[i]])

       
game = Game()

game.setBonesCount(3)
game.throwBones()
game.showBones()




