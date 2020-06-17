import turtle
import time
import random


right_bool =  False
left_bool  =  True
down_bool  =  False
up_bool    =  False

wn = turtle.Screen()
wn.title("snake game")
wn.bgcolor("black")
wn.setup(width=800,height=800)
wn.tracer(0)


def paddle_up():
    y_loc=snake_location[0]['y_loc']
    y_loc = y_loc+25 if (y_loc+25)<400 else -400+(y_loc+25)-400
    snake_location[0]['y_loc']=y_loc
    
    global right_bool , left_bool, down_bool, up_bool
    right_bool = left_bool = down_bool = False
    up_bool=True
       


def paddle_down():
    global right_bool , left_bool, down_bool, up_bool
    #if up_bool!=True and down_bool!=True:
    y_loc=snake_location[0]['y_loc']
    y_loc = y_loc-25 if (y_loc-25)>-400 else 400-(y_loc-25)-400
    snake_location[0]['y_loc']=y_loc
    
    right_bool = left_bool = up_bool = False
    down_bool=True

def paddle_right():
    x_loc=snake_location[0]['x_loc']
    x_loc = x_loc+25 if (x_loc+25)<400 else -400+(x_loc+25)-400
    snake_location[0]['x_loc']=x_loc
    
    global right_bool , left_bool, down_bool, up_bool
    up_bool = left_bool = down_bool = False
    right_bool=True
    
def paddle_left():
    x_loc=snake_location[0]['x_loc']
    x_loc = x_loc-25 if (x_loc-25)>-400 else 400-(x_loc-25)-400
    snake_location[0]['x_loc']=x_loc
    
    global right_bool , left_bool, down_bool, up_bool
    right_bool = up_bool = down_bool = False
    left_bool=True
    



snake_location = [{'x_loc' : 0 ,'y_loc' : 0}]
"""snake_location.append({'x_loc' : -25,'y_loc' : 0})
snake_location.append({'x_loc' : -50 ,'y_loc' : 0})
snake_location.append({'x_loc' : -75 ,'y_loc' : 0})
snake_location.append({'x_loc' : -100,'y_loc' : 0})"""


snake=[turtle.Turtle()]
snake[0].speed(0)
snake[0].color("white")
#snake.shapesize(stretch_wid=0.5, stretch_len=0.5)
snake[0].shape("square")
snake[0].penup()
"""
snake.append ( turtle.Turtle() )
snake[1].speed(0)
snake[1].color("white")
#snake.shapesize(stretch_wid=0.5, stretch_len=0.5)
snake[1].shape('square')
snake[1].penup()

snake.append ( turtle.Turtle() )
snake[2].speed(0)
snake[2].color("white")
#snake.shapesize(stretch_wid=0.5, stretch_len=0.5)
snake[2].shape('square')
snake[2].penup()

snake.append ( turtle.Turtle() )
snake[3].speed(0)
snake[3].color("white")
#snake.shapesize(stretch_wid=0.5, stretch_len=0.5)
snake[3].shape('square')
snake[3].penup()

snake.append ( turtle.Turtle() )
snake[4].speed(0)
snake[4].color("white")
#snake.shapesize(stretch_wid=0.5, stretch_len=0.5)
snake[4].shape('square')
snake[4].penup()"""

foodobj= turtle.Turtle()
foodobj.speed(0)
foodobj.color("white")
#snake.shapesize(stretch_wid=0.5, stretch_len=0.5)
foodobj.shape('square')
foodobj.penup()

wn.listen()
wn.onkeypress(paddle_up,"Up")
wn.onkeypress(paddle_left,"Left")
wn.onkeypress(paddle_right,"Right")
wn.onkeypress(paddle_down,"Down")
didnt_bite = True
error_count=0
length_count=0
foodlocation= {'x_loc' : random.randrange(-400,400,25) , 'y_loc' : random.randrange(-400,400,25)}
food = True
while didnt_bite:
    if(not food): 
        foodlocation ['x_loc'] = random.randrange(-375,375,25)
        foodlocation ['y_loc'] = random.randrange(-375,375,25)
        food=True
        
    
    foodobj.goto(foodlocation['x_loc'],foodlocation['y_loc'])
    i=0
    for i in range (len(snake_location)-1,0,-1):
        snake_location[i]['x_loc']=snake_location[i-1]['x_loc']
        snake_location[i]['y_loc']=snake_location[i-1]['y_loc']
    
    for i in range (len(snake_location)-1,1,-1):    
        if snake_location[i]['x_loc']==snake_location[0]['x_loc'] and\
            snake_location[i]['y_loc']==snake_location[0]['y_loc']:
          
            error_count=error_count+1
            didnt_bite=False
        
                
    if foodlocation['x_loc'] == snake_location[0]['x_loc'] and foodlocation['y_loc']==snake_location[0]['y_loc'] : 
        food =False
        length_count+=1

        snake_location.append({'x_loc' : 0 ,'y_loc' : 0})
        snake.append ( turtle.Turtle() )
        snake[length_count].speed(0)
        snake[length_count].color("white")
        #snake.shapesize(stretch_wid=0.5, stretch_len=0.5)
        snake[length_count].shape('square')
        snake[length_count].penup()


    if(up_bool): paddle_up()
    if(down_bool): paddle_down()
    if(right_bool): paddle_right()
    if(left_bool): paddle_left() 
   
           
   
    i=0
    for s in snake_location:
        snake[i].goto( s['x_loc'] , s['y_loc']  )
        #snake[0].goto(x_loc,0)
        i+=1
    time.sleep(0.1)
    wn.update()

while True:  
    file_img=r"dog.gif"
    wn.bgpic(file_img)
    wn.update()
       