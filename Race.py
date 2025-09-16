from Dice import *
from graphics import *

class Horse():
    def __init__(self, speed,  y_pos, image, win):
        self.speed = Dice(speed)
        self.x_pos = 0
        self.y_pos = y_pos
        self.image = image
        self.win = win

    def move(self):
        roll = self.speed.roll()
        self.x_pos += roll

    def draw(self):
        self.image.draw_at_pos(self.win, self.x,self.y)

    def crossed_finish_line(self, crossline_x_pos):
        return self.x_pos >= crossline_x_pos

def main():
    #draw canvas
    win = GraphWin('Drawing', 700, 350, autoflush=False )

    #creating and drawing horses
    horse1 = Horse(6, 250, Image(Point(100,200),'horse1.gif'),win)
    
    horse2 = Horse(6, 75, Image(Point(0,100), 'DOOM.gif'), win)
    
    horse1.draw()
    horse2.draw()

    #drawing a line
    line = Line(Point(600,0),Point(600,350))
    line.draw(win)

    #start race
    win.getMouse()

    #race
    while(True):
        #clear window and redraw elements
        win.clear_win()
        line.draw(win)
        horse1.draw()
        horse2.draw()

        #check if any horses won and close the window if anything did
        if(horse1.crossed_finish_line(600) and horse2.crossed_finish_line(600)):
            #tie
            print("Tie")

            break
        elif(horse1.crossed_finish_line(600)):
            #horse 1 won
            print("Horse 1 is the winner")
            break
        elif(horse2.crossed_finish_line(600)):
            #horse 2 won
            print("Horse 2 is the winner")
            break
        else:

            #if nobody won keep moving
            horse1.move()
            horse2.move()
            
        
        #update
        win.update()

    #closing windows when clicked
    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()