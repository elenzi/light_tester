class LEDtester:
    
    lights = 0
    count = 0
    
    def __init__(self, N):
        size = 0
        lights = 0
        self.lights = [[False]*size for _ in range(size)]
        
    def apply(self, cmd):
        lights = 0
        if cmd == 'turn on':
            lights.on()
        elif cmd == 'turn off':
            lights.off()
        elif cmd == 'switch':
            lights.toggle()
    
    def count(self):
        return count
    
        
    