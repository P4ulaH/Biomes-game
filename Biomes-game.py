'''
story idea:
- you can move south, east, or west
- where you move you generate a biome
- biomes have different items in them
- you can pick them up

biomes:
- meadow
- forest
- desert
- ocean
- mountain

'''
import tkinter
import random
import time
canvas = tkinter.Canvas(width=700, height=700, bg='white')
canvas.pack()


def meadow(x, y):
    x = x*100
    y = y*100
    canvas.create_rectangle(x+0, y+0, x+100, y+100, fill='#83b85a', outline='#54753b')
    canvas.create_rectangle(x+10, y+10, x+35, y+35, fill='#548739', outline='')
    canvas.create_rectangle(x+15, y+15, x+30, y+30, fill='#376729', outline='')
    canvas.create_rectangle(x+50, y+30, x+90, y+75, fill='#548739', outline='')
    canvas.create_rectangle(x+60, y+40, x+80, y+65, fill='#376729', outline='')
    canvas.create_rectangle(x+10, y+50, x+40, y+90, fill='#80BCBD', outline='beige', width=2)
    
def forest(x, y):
    x = x*100
    y = y*100
    canvas.create_rectangle(x+0, y+0, x+100, y+100, fill='#416b55', outline='#233b2e')
    canvas.create_rectangle(x+70, y+70, x+95, y+95, fill='#2a4233', outline='')#
    canvas.create_rectangle(x+75, y+75, x+90, y+90, fill='#172b1f', outline='')
    canvas.create_rectangle(x+10, y+15, x+40, y+45, fill='#2a4233', outline='')#
    canvas.create_rectangle(x+15, y+20, x+35, y+40, fill='#172b1f', outline='')
    canvas.create_rectangle(x+20, y+25, x+30, y+35, fill='#0c1710', outline='')
    canvas.create_rectangle(x+65, y+10, x+95, y+40, fill='#2a4233', outline='')#
    canvas.create_rectangle(x+70, y+15, x+90, y+35, fill='#172b1f', outline='')
    canvas.create_rectangle(x+75, y+20, x+85, y+30, fill='#0c1710', outline='')
    canvas.create_rectangle(x+40, y+50, x+65, y+75, fill='#2a4233', outline='')#
    canvas.create_rectangle(x+45, y+55, x+60, y+70, fill='#172b1f', outline='')
    canvas.create_rectangle(x+5, y+65, x+35, y+95, fill='#2a4233', outline='')#
    canvas.create_rectangle(x+10, y+70, x+30, y+90, fill='#172b1f', outline='')
    canvas.create_rectangle(x+15, y+75, x+25, y+85, fill='#0c1710', outline='')
    
     
def desert(x, y):
    x = x*100
    y = y*100
    
    canvas.create_rectangle(x+0, y+0, x+100, y+100, fill='#e4c29c', outline='#c29d74')
    
    canvas.create_rectangle(x+0, y+60, x+35, y+100, fill='#CAA67E', outline='')#
    canvas.create_rectangle(x+0, y+70, x+60, y+100, fill='#CAA67E', outline='')
    canvas.create_rectangle(x+0, y+85, x+80, y+100, fill='#CAA67E', outline='')
    canvas.create_rectangle(x+0, y+70, x+25, y+100, fill='#BD986F', outline='')#
    canvas.create_rectangle(x+0, y+80, x+50, y+100, fill='#BD986F', outline='')
    canvas.create_rectangle(x+0, y+95, x+70, y+100, fill='#BD986F', outline='')
    
    canvas.create_rectangle(x+60, y+0, x+100, y+45, fill='#CAA67E', outline='')#
    canvas.create_rectangle(x+20, y+0, x+100, y+30, fill='#CAA67E', outline='')
    canvas.create_rectangle(x+10, y+0, x+100, y+15, fill='#CAA67E', outline='')
    canvas.create_rectangle(x+70, y+0, x+100, y+35, fill='#BD986F', outline='')#
    canvas.create_rectangle(x+30, y+0, x+100, y+20, fill='#BD986F', outline='')
    canvas.create_rectangle(x+20, y+0, x+100, y+5, fill='#BD986F', outline='')
    canvas.create_rectangle(x+80, y+0, x+100, y+25, fill='#BD986F', outline='')#
    canvas.create_rectangle(x+40, y+0, x+100, y+10, fill='#BD986F', outline='')
    
    canvas.create_rectangle(x+15, y+40, x+25, y+50, fill='#58763a', outline='')#
    canvas.create_rectangle(x+85, y+75, x+95, y+85, fill='#58763a', outline='')
    canvas.create_rectangle(x+70, y+25, x+80, y+35, fill='#58763a', outline='')
    
def ocean(x, y):
    x = x*100  
    y = y*100
    canvas.create_rectangle(x+0, y+0, x+100, y+100, fill='#56ced6', outline='#33898f')
    canvas.create_rectangle(x+50, y+20, x+80, y+70, fill='#A6D3C3', outline='') 
    canvas.create_rectangle(x+40, y+30, x+90, y+60, fill='#A6D3C3', outline='')
    canvas.create_rectangle(x+50, y+30, x+80, y+60, fill='#F6D7B0', outline='')
    canvas.create_rectangle(x+65, y+35, x+75, y+45, fill='#58763a', outline='')#
    
def mountain(x, y):
    x = x*100
    y = y*100
    
    canvas.create_rectangle(x+0, y+0, x+100, y+100, fill='#9ab8e6', outline='#7a7a7a')
    canvas.create_rectangle(x+20, y+0, x+100, y+40, fill='#808080', outline='')
    canvas.create_rectangle(x+60, y+0, x+100, y+80, fill='#808080', outline='')
    canvas.create_rectangle(x+40, y+0, x+100, y+60, fill='#808080', outline='')
    canvas.create_rectangle(x+50, y+0, x+100, y+50, fill='#747474', outline='')#
    canvas.create_rectangle(x+75, y+0, x+100, y+65, fill='#747474', outline='')
    canvas.create_rectangle(x+35, y+0, x+100, y+25, fill='#747474', outline='')
    canvas.create_rectangle(x+70, y+0, x+100, y+30, fill='#E1E3E3', outline='')#
    canvas.create_rectangle(x+90, y+0, x+100, y+40, fill='#E1E3E3', outline='')
    canvas.create_rectangle(x+60, y+0, x+100, y+10, fill='#E1E3E3', outline='')
    
    canvas.create_rectangle(x+0, y+70, x+50, y+100, fill='#808080', outline='')#                                
    canvas.create_rectangle(x+0, y+50, x+30, y+100, fill='#808080', outline='')
    canvas.create_rectangle(x+0, y+60, x+20, y+100, fill='#747474', outline='')
    canvas.create_rectangle(x+0, y+80, x+40, y+100, fill='#747474', outline='')

def start(x, y):
    x = x*100
    y = y*100
    canvas.create_rectangle(x+0, y+0, x+100, y+100, fill='#C1773E', outline='#2b5e8f')
    canvas.create_rectangle(x+10, y+10, x+90, y+90, fill='#975D2F', outline='')
    canvas.create_rectangle(x+20, y+20, x+80, y+80, fill='#6C421F', outline='')
    canvas.create_rectangle(x+30, y+30, x+70, y+70, fill='#422710', outline='')
    canvas.create_rectangle(x+40, y+40, x+60, y+60, fill='#170C00', outline='')

def end(x, y):
    x = x*100
    y = y*100
    canvas.create_rectangle(x+0, y+0, x+100, y+100, fill='#3e7fc1', outline='#2b5e8f')
    canvas.create_rectangle(x+10, y+10, x+90, y+90, fill='#2b5e8f', outline='')
    canvas.create_rectangle(x+20, y+20, x+80, y+80, fill='#1a3e5f', outline='')
    canvas.create_rectangle(x+30, y+30, x+70, y+70, fill='#0a1e2f', outline='')
    canvas.create_rectangle(x+40, y+40, x+60, y+60, fill='#000c17', outline='') 

def blank(x, y):
    x = x*100
    y = y*100
    return canvas.create_rectangle(x+0, y+0, x+100, y+100, fill='white', outline='white')

def outline(x, y):
    x = x*100
    y = y*100
    return canvas.create_rectangle(x+0, y+0, x+100, y+100, fill='', outline='black', width=2)


inventory = []
biomes = [meadow, forest, desert, ocean, mountain]

class Biome:
    
    def __init__(self, x, y, biome):
        self.x = x
        self.y = y
        self.biome = biome
        self.biome(x, y)
        self.items = []
        self.locked = False
       
    def lock(self):
        self.locked = True
        self.b1 = blank(self.x, self.y)
        
    def unlock(self):
        self.locked = False
        canvas.delete(self.b1)
        
        
class Key:
    def __init__(self, x, y):
        self.x = x*100
        self.y = y*100
        
        
    def remove(self):
        canvas.delete(self.p1, self.p2, self.p3, self.p4)
        
    def create(self):
        self.p1 = canvas.create_oval(self.x+35, self.y+20, self.x+65, self.y+50, fill='', outline='gold', width=10)
        self.p2 = canvas.create_rectangle(self.x+45, self.y+50, self.x+55, self.y+90, fill='gold', outline='')
        self.p3 = canvas.create_rectangle(self.x+35, self.y+82, self.x+50, self.y+90, fill='gold', outline='')
        self.p4 = canvas.create_rectangle(self.x+35, self.y+65, self.x+50, self.y+73, fill='gold', outline='')
    


startY = 0
startX = 0

enddY = random.randint(1, 6)
enddX = random.randint(1, 6)

keyY = random.randint(1, 6)
keyX = random.randint(1, 6)

locations = []

#generating biomes
for x in range(7):
  ylist = []
  for y in range(7):
    if(x == startX and y == startY):
        b = Biome(x, y, start)
    elif(x == enddX and y == enddY):
        b = Biome(x, y, end)
        b.lock()
    else:
        rand_biomes = random.choice(biomes)
        b = Biome(x, y, rand_biomes)
        if x == keyX and y == keyY:
            global key
            key = Key(x, y)
            key.create()
            b.items.append(key)
            print(x, y)
        b.lock()

    ylist.append(b)

  locations.append(ylist) 

  
xx = 0
yy = 0

outlinevar = outline(xx, yy)

def collect(event):
    global locations
    global inventory
    global key
    global enddX
    global enddY
    global xx
    global yy
    
    for item in locations[xx][yy].items:
        inventory.append(item)
        item.remove()
        locations[xx][yy].items.remove(item)
        print("item: ",item)
    
    
    if xx == enddX and yy == enddY:
        print("end")
        if key in inventory:
            locations[enddX][enddY].unlock()
            print('You win!')
            exit()

  
def moveRight(event):
    global xx
    if(xx >= 0) and (xx < 6):
        xx += 1
        if locations[xx][yy].locked == True:
            locations[xx][yy].unlock() 
        
        print(xx, yy)
        print(locations[xx][yy].items)

        global outlinevar
        canvas.delete(outlinevar)
        outlinevar = outline(xx, yy)
        
def moveLeft(event):
    global xx
    if(xx > 0) and (xx < 7):
        xx -= 1
        if locations[xx][yy].locked == True:
            locations[xx][yy].unlock() 
        
        print(xx, yy)
        print(locations[xx][yy].items)
        
        global outlinevar
        canvas.delete(outlinevar)
        outlinevar = outline(xx, yy)

def moveUp(event):
    global yy
    if(yy > 0) and (yy < 7):
        yy -= 1
        if locations[xx][yy].locked == True:
            locations[xx][yy].unlock() 
        
        print(xx, yy)
        print(locations[xx][yy].items)

        
        global outlinevar
        canvas.delete(outlinevar)
        outlinevar = outline(xx, yy)

def moveDown(event):
    global yy
    if(yy >= 0) and (yy < 6):
        yy += 1
        if locations[xx][yy].locked == True:
            locations[xx][yy].unlock() 
        
        print(xx, yy)
        print(locations[xx][yy].items)
        
        
        global outlinevar
        canvas.delete(outlinevar)
        outlinevar = outline(xx, yy)
  

canvas.bind_all('<KeyPress-Right>', moveRight)
canvas.bind_all('<KeyPress-Left>', moveLeft)
canvas.bind_all('<KeyPress-Up>', moveUp)
canvas.bind_all('<KeyPress-Down>', moveDown)
canvas.bind_all('<KeyPress-Return>', collect)

     
    
canvas.mainloop()