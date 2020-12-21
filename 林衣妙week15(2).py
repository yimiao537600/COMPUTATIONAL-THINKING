import turtle
shelly = turtle.Turtle()
colors = ["red","green","blue","black","purple","yellow"]
# 外迴圈重複正方形6次
for n in range(6):
   shelly.color(colors[n]) #
   shelly.begin_fill()
   shelly.fillcolor(colors[n])
#內迴圈重複4次來畫正方形
for i in range(4):
   shelly.forward(250)
   shelly.left(90)
shelly.right(60) #畫下一個正方形前轉彎
shelly.end_fill()
