# -*- coding: utf-8 -*-
"""



"""

import turtle
import time #if we don't import this, the snake will run off the screen even before we could see it.
import random

delay=0.1
#screen
s1=turtle.Screen() #S should always be capital
s1.title("SNAKES....")
s1.bgcolor("blue")
s1.setup(width=600, height= 600)
s1.tracer(0) #turns off screen updates

#snake head
head=turtle.Turtle()
head.speed(0)   #doesn't means the snake's speed
head.shape("square")
head.color("black")
head.penup() #so that it doesn't create tracelines
head.goto(0,0)
head.direction="stop" # ssoit doesn't moves on start

#snake food 
food=turtle.Turtle()
food.speed(0)   #doesn't means the snake's speed
food.shape("circle")
food.color("yellow")
food.penup() #so that it doesn't create tracelines
food.goto(0,100)

score=0
high_score=0

segments=[] #segment for snake body

#scoreboard
pen=turtle.Turtle()
pen.speed(0)
pen.color("yellow")
pen.shape("square")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("SCORE:0   HIGH SCORE:0" , align="center", font=("arial",24,"normal"))



#functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

#keyboard config
s1.listen()
s1.onkeypress(go_up,"w")    
s1.onkeypress(go_down,"s")    
s1.onkeypress(go_left,"a")    
s1.onkeypress(go_right,"d")    

def move():
    if head.direction=="up":
        y=head.ycor()   #assigning y as y co-ordinate
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="right":
        x=head.xcor()
        x=head.setx(x+20)
    if head.direction=="left":
        x=head.xcor()
        x=head.setx(x-20)

while True:   #main game loop to update snake head despite the s1.trace(0) statement
    s1.update()
    
    
    #winning condition -border check
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
       
        for segment in segments:         # resetting body lenghth to zero after restarting game
            segment.goto(1000,1000)
            
        segments.clear()
        
        pen.clear()
        pen.write("TRY AGAIN....krazyy 8",align="center", font=("arial",24,"normal"))
        time.sleep(1)
        pen.clear()
        pen.write("SCORE: {0}, HIGH SCORE:{1}".format(score, high_score),align="center", font=("arial",24,"normal"))

    
           
            
        

    if head.distance(food)<20:   #to check collision and move the food to a random location
        x=random.randint(-290, 290)
        y=random.randint(-290,290)
        food.goto(x,y)

        
        
        
        
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
     
        #score board
        score=score+10
        if score>high_score:
            high_score=score
            
        pen.clear()    
        pen.write("SCORE: {0} HIGH SCORE:{1}".format(score, high_score),align="center", font=("arial",24,"normal"))
       

        
        #segments is a list and segment is an object of turtle
    move()

     #checking for body collisions
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            
 
            for segment in segments:         # resetting body lenghth to zero after restarting game
                segment.goto(1000,1000)
            
            segments.clear()
                    #reset score to 0 after one round
            score=0  #this score is a local variable to reset the score's value

            pen.clear()
            pen.write("TRY AGAIN....krazyy 8",align="center", font=("arial",24,"normal"))
            time.sleep(1)
            pen.clear()
            pen.write("SCORE: {0}, HIGH SCORE:{1}".format(score, high_score),align="center", font=("arial",24,"normal"))
            break
            
            
            
    #adding susequent segments in reverse order        
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
        
        
        
        
    
        # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    time.sleep(delay) #to make the snake go a bit visible and not let it escape before we could even see it.
     
s1.mainloop()