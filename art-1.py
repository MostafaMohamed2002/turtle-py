from turtle import *
import colorsys
tracer (100)
bgcolor("black")
h=0.0
pensize(2)
for i in range (210):
   goto(10,20)
   c=colorsys.hsv_to_rgb(h, 1,0.8)
   pencolor(c)
   h+=0.005
   circle(190-1,90)
   rt(120)
   rt(120)
   circle(190-i,90)
   circle(190-1,90)
done()