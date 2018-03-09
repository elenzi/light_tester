import re

class LEDTester:
    lights = None
    
    def __init__(self, N, instructions):
        self.N = N
        self.lights = [[False]*self.N for _ in range(self.N)]
        self.instructions = instructions
        self.command = ""
        self.operations()
        self.countLights = self.countOccupied()
        print("Number of lights on: ", self.countLights)
        
        #self.apply(self)
#         print(self.lights)
        
    def operations(self):
        for i in self.instructions:
            pattern = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*") 
            matched = pattern.match(i)
            self.command = matched.group(1)
            self.start = matched.group(2), matched.group(3)
            self.end = matched.group(4), matched.group(5)
            if self.command == 'turn on':
                self.turnon(self.command, self.start, self.end)
            elif self.command == 'turn off':
                self.turnoff(self.command, self.start, self.end)
            elif self.command == 'switch':
                self.switch(self.command, self.start, self.end)

    def turnon(self, command, start, end):
        #self.countTon = 0
        if self.command == "turn on":
            for i in range(int(self.start[0]),int(self.end[0])+1):
                for j in range(int(self.start[1]),int(self.end[1])+1):
                    self.lights[i][j] = True
                    #self.countTon += 1
        #return(self.countTon)
            #return(countTon)
                   
                           
    def turnoff(self, command, start, end):
        if self.command == 'turn off':
            for i in range (int(self.start[0]),int(self.end[0])+1):
                for j in range (int(self.start[1]),int(self.end[1])+1):
                    self.lights[i][j] = False
                           
       
        
    def switch(self, command, start, end):
        if command == 'switch':
            for i in range (int(self.start[0]),int(self.end[0])+1):
                for j in range (int(self.start[1]),int(self.end[1])+1):
                    self.lights[i][j] = not(self.lights[i][j])
                    
    def countOccupied(self):
        T = 0
        for i in range (self.N):
            for j in range (self.N):
                if self.lights[i][j] == True:
                    T +=1
        #self.F = self.N * self.N - self.T                          
        return T

    
# def main():
#     ifile = "/Users/elenalanigan/softeng/data/test.txt"
#     N, instructions = utils.parseFile(ifile)
#     matrix = LEDTester(N, instructions)
#     #matrix.turnon()#
# 
# if __name__=='__main__':
#     main()
    
        
    