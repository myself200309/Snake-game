import pygame as py
import time
import random as rn

py.init()    # initializing package modules

red = (0,0,128)
white = (255,0,0)
yellow = (255,255,255)

wd = 400
ht = 300

dis=py.display.set_mode((wd,ht))      #display "surface" object
py.display.set_caption("Snake Game")   #setting caption

clock = py.time.Clock()
speed = 5

font = py.font.SysFont(None,20)



def snake(block,lis):
   for z in lis:
      py.draw.rect(dis,red,[z[0],z[1],block,block])

def food(fx,fy,block):
   py.draw.rect(dis,yellow,[fx,fy,block,block])

#function to display message

def message(msg,color):
   mesg = font.render(msg,True,color)
   dis.blit(mesg,[50,150])

# new function


def loop():
   
   
   over = False
   close= False
   

   x = wd/2           
   y = ht/2
   block =10

   
   length=1

   
   fx = round(rn.randrange(0,wd-block)/10.0)*10.0
   fy = round(rn.randrange(0,ht-block)/10.0)*10.0

   lis =[[x,y]]

   x_change =0
   y_change =0


   while not over:
      while close==True:
         dis.fill(white)
         message("You Lost! Press Q-Quit or C to play again",red)
         py.display.update()

         for event in py.event.get():
            if event.type==py.QUIT:
               over = True
               close = False
            elif event.type==py.KEYDOWN:
               if event.key ==py.K_q:
                  over = True
                  close = False
               elif event.key == py.K_c:
                  fx = round(rn.randrange(0,wd-block)/10.0)*10.0
                  fy = round(rn.randrange(0,ht-block)/10.0)*10.0

                  lis =[[x,y]]
                  length = 1

                  x_change =0
                  y_change =0
                  close = False
   
      for event in py.event.get():
         if event.type==py.QUIT:
            over = True
      if event.type==py.KEYDOWN:
         if event.key == py.K_LEFT:
               x_change = -block
               y_change = 0
         elif event.key == py.K_RIGHT:
            x_change= block
            y_change = 0
         elif event.key == py.K_UP:
            x_change = 0
            y_change= -block
         elif event.key == py.K_DOWN:
            x_change = 0
            y_change = block
      if lis[-1][0]>=wd or lis[-1][0]<0 or lis[-1][1]>=ht or lis[-1][1]<0:
         close =True

      a = lis[0]
      for i in range(length-1):
         lis[i][0] = lis[i+1][0]
         lis[i][1] = lis[i+1][1]

      lis[-1][0] += x_change
      lis[-1][1] += y_change

      

      dis.fill(white)

      food(fx,fy,block)

      snake(block,lis)
   
      py.display.update()

      if lis[-1][0] == fx and lis[-1][1] == fy:
         a = fx
         b = fy

         fx = round(rn.randrange(0,wd-block)/10.0)*10.0
         fy = round(rn.randrange(0,ht-block)/10.0)*10.0
         length+=1
         lis.append([a+block,b+block])

      clock.tick(speed)



   py.quit()
   quit()


loop()
