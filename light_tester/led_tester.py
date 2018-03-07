import re

class LEDtester:
    
    lights = None
    
    def __init__(self, N, instructions):
        self.lights = [[False]*N for _ in range(N)]
        self.instructions = instructions
        self.operations(self)
        
    def operations(self, instructions):
        for i in self.instructions:
            cmd, start, end = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*") 
            self.apply(self, cmd, start, end)
        
    def apply(self, cmd, start, end):
        if cmd == "turn on":
            self.turnon(self, start, end)
            
        elif cmd == 'turn off':
            self.turnoff(self, start, end)
            
        elif cmd == 'switch':
            self.switch(self, start, end)
            
    def turnon(self,start, end):
        for i in range (len(self.lights)):
            for j in range (len(self.lights)):
                if self.lights[i][j] == False:
                    self.lights[i][j] = True
                           
    def turnoff(self, start, end):
        for i in range (len(self.lights)):
            for j in range (len(self.lights)):
                if self.lights[i][j] == True:
                    self.lights[i][j] = False
                           
    def switch(self, start, end):
        for i in range (len(self.lights)):
            for j in range (len(self.lights)):
                if self.lights[i][j] == False:
                    self.lights[i][j] = True       
                else:
                    self.lights[i][j] == True
                    self.lights[i][j] = False

    def countOccupied(self, T):
        self.T = 0
        
        for i in range (len(self.lights)):
            for j in range (len(self.lights)):
                if self.lights[i][j] == True:
                    T += 1
        return self.T

    
        
    