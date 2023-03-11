import turtle
turtle.pensize(10)  #調整畫筆大小

turtle.color("blue") #將畫筆顏色改成藍色
turtle.penup()  #將畫筆筆頭提起來
                #避免移動時，畫到不必要的部分
turtle.goto(-110,-25) #將畫筆筆頭移動到此點
turtle.pendown() #將畫筆筆頭抵住此點，
turtle.circle(45) #以此點為中心畫出半徑
                  #45pixel的圓。
turtle.color("black") #換顏色
turtle.penup()
turtle.goto(0,-25) #換到適當位置
turtle.pendown()
turtle.circle(45)
                    #以下依照會旗改變顏色。
turtle.color("red")
turtle.penup()
turtle.goto(110,-25)
turtle.pendown()
turtle.circle(45)

turtle.color("yellow")
turtle.penup()
turtle.goto(-55,-75)
turtle.pendown()
turtle.circle(45)

turtle.color("green")
turtle.penup()
turtle.goto(55,-75)
turtle.pendown()
turtle.circle(45)

turtle.done() #讓程式執行完，不要自動關掉。
