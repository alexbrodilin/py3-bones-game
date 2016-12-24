# -*- coding: UTF-8 -*-

import random, os, time

class Application:
    name = ""
    throwsCount = 0
    bonesCount = 0
    
    throwsLeft = 0
    currentMove = 1 #1 - PC, -1 - Player
    
    curThrowScoresPC = 0
    curThrowScoresPl = 0
    
    Bones = []
    finalScoresTable = []
    
    replayKey = "r"
    backToMenuKey = "b"
    exitKey = "x"
    
    # --- logic ---
    def setName(self, PlayerName):
        self.name = PlayerName
        
    def setThrowsCount(self, Count):
        self.throwsLeft = Count
        
    def setBonesCount(self, Count):
        self.bonesCount = Count
        
    def storeScores(self):
        self.finalScoresTable.append([self.curThrowScoresPC, self.curThrowScoresPl])
        
    def summTable(self):
        summRowsPC = 0
        summRowsPl = 0
        for row in self.finalScoresTable:
            summRowsPC += row[0]
            summRowsPl += row[1]
            
        return [summRowsPC, summRowsPl]
    
    def setPlScores(self, scores):
        self.curThrowScoresPl = scores
        
    def getPlScores(self):
        return self.curThrowScoresPl
        
    def setPCScores(self, scores):
        self.curThrowScoresPC = scores
        
    def getPCScores(self):
        return self.curThrowScoresPC
        
    def coinToss(self):
        self.currentMove = random.choice([-1,1])
        
    def switchTurn(self):
        self.currentMove *= -1
        
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
            
        self.switchTurn()
        self.drawScreen(1)
        if self.currentMove == 1: 
            print("\nPlease wait. I'm preparing to throw...")
            time.sleep(random.randint(3,6))

        
    def makeThrows(self):
        self.throw()
        self.throw()
        self.storeScores()
        self.curThrowScoresPC = 0
        self.curThrowScoresPl = 0
        self.throwsLeft -= 1
    
    def gameCycle(self):
        if self.throwsLeft == self.throwsCount: 
            self.drawScreen(1)
            self.coinToss()
            self.makeThrows()
            self.gameCycle()
        elif self.throwsLeft != 0: 
            self.makeThrows()
            self.gameCycle()
        else: self.drawScreen(2)
        
    
    def drawScreen(self, screenType):
        _ = os.system('cls' if os.name == 'nt' else 'clear')
        if screenType == 1: 
            self.topPanel()
            self.showCurThrowScores()
            self.showBones()
        elif screenType == 2:
            self.topPanel()
            self.endScreen()
    
    def resetState(self):
        self.throwsLeft = self.throwsCount;
        self.finalScoresTable = []   
                
    
    # --- interface ---
    def topPanel(self):
        print("Player name: " + self.name + "   Bones uses: " + str(self.bonesCount) + "    Throws left: " + str(self.throwsLeft))
        print("--------------------------------------------------------------------------------")
    
    def sayPlayerTurn(self):
        print("\n\n\n                    Your turn! Press enter to throw")
        key = input()
    
    def showCurThrowScores(self):
        print("      Current PC: " + str(self.getPCScores()) + " | Player: " + str(self.getPlScores()))
        summ = self.summTable()
        print("      Overall       PC: " + str(summ[0]) + " | Player: " + str(summ[1]))
        print("--------------------------------------------------------------------------------")
        
    def endScreen(self):
        print("  PC       Player  \n-------------------\n")
        for row in self.finalScoresTable:
            print("  " + str(row[0]) + "         " + str(row[1]) + "\n")
        summ = self.summTable()
        print("-------------------\n  " + str(summ[0]) + "         " + str(summ[1]) + "\n")
        print("What's next?\n"+ self.replayKey + ". Replay\n" + self.backToMenuKey + ". Back to setting\n" + self.exitKey + ". Exit")
        
        key = input()
        
        if key == self.replayKey: 
            self.resetState()
            self.gameCycle()
        elif key == self.backToMenuKey: 
            self.resetState()
            self.settingsScreen()
        elif key == self.exitKey: quit()
        else: self.drawScreen(2)   
        
    def settingsScreen(self):
        _ = os.system('cls' if os.name == 'nt' else 'clear')
        print("Welcome, traveller! Let's play some Bones game! Choose your settings. \n\n")
        self.name = input("What's your name? >> ")
        self.bonesCount = self.inputBonesCount()
        inp = self.inputThrowsCount()
        self.throwsCount = inp 
        self.throwsLeft = inp
        self.gameCycle()
        
    def inputBonesCount(self):
        try:
            inp = int(input("How many bones whould you like to use? >> "))    
        except ValueError:
            self.inputBonesCount()
            
        return inp
    
    def inputThrowsCount(self):
        try:
            inp = int(input("How many throws whould you like to make? >> "))
        except ValueError:
            self.inputThrowsCount()
            
        return inp








