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
    
    # --- logic ---
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
            print(self.generateSprite(i) + "\n")
            
    def generateSprite(self, boneSide):
        space = random.randint(1,76)
        spaces = ""
        for i in range(space): spaces += " "        
        if boneSide == 1: return spaces + "###\n" + spaces +"#0#\n" + spaces +"###"
        elif boneSide == 2: return spaces + "0##\n" + spaces +"###\n" + spaces +"##0"
        elif boneSide == 3: return spaces + "0##\n" + spaces +"#0#\n" + spaces +"##0"
        elif boneSide == 4: return spaces + "0#0\n" + spaces +"###\n" + spaces +"0#0"
        elif boneSide == 5: return spaces + "0#0\n" + spaces +"#0#\n" + spaces +"0#0"
        elif boneSide == 6: return spaces + "000\n" + spaces +"###\n" + spaces +"000"
    
    def throw(self):
        if self.currentMove == 1:
            self.throwBones()
            self.setPCScores(sum(self.Bones))
        else:
            self.sayPlayerTurn()
            self.throwBones()
            self.setPlScores(sum(self.Bones))
        
        self.storeScores()
        self.showCurThrowScores()
        self.showOverallScores()
    
    def gameCycle(self):
        pass
    
    # --- interface ---
    def sayPlayerTurn(self):
        pass
    
    def showCurThrowScores(self):
        pass
    
    def showOverallScores(self):
        pass
    
    def showResultTable(self):
        pass
    
    def showActionsMenu(self):
        pass
    
    # --- configuration ---
    def askPlayerName(self):
        pass
    
    def askThrowsCount(self):
        pass
    
    def askBonesCount(self):
        pass
    
game = Game()

game.setBonesCount(3)
game.throwBones()
game.showBones()







