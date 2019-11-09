from turtle import*
import turtle
#image = r"/Users/jesscharanjit/Documents/Lunchlady_Dora.gif" 
image = r"C:\Users\thamc\Downloads\Lunchlady_Dora.gif"
bgimage= r"C:\Users\thamc\Pictures\bandah.gif"

screen = turtle.Screen()
#maximize screen size
screen.screensize()
screen.setup(width = 1.0, height = 1.0)

penup()
goto(-300,-100)
pendown()
bgcolor('#e6ffff')
orderTotal=0

#Quantity input, maximum value of each item is 5. Food price is multiplied by quantity to get total.

def takeOrder(item,price):
    itemqty = screen.numinput("Your order",item+" quantity:",minval=0,maxval=5)
    print(item+" total:")
    print(itemqty*price)
    global orderTotal
    orderTotal=orderTotal+(itemqty*price)

#Bottom of canteen
    
def draw_bottom(color,x,y):
    fillcolor(color)
    pencolor(color)
    begin_fill()
    #bgpic(bgimage)
    fd(500)
    rt(90)
    fd(100)
    rt(90)
    fd(500)
    rt(90)
    fd(100)
    end_fill()
    
draw_bottom('#464646',-300,-100)

#Middle section of canteen

def draw_middle(color,x,y):
    penup()
    fillcolor(color)
    pencolor(color)
    goto(x,y)
    pendown()
    begin_fill()
    fd(200)
    rt(90)
    fd(460)
    rt(90)
    fd(200)
    rt(90)
    fd(460)
    end_fill()
    
draw_middle('#c0c0c0',-280,-99)

#Top section of canteen

def draw_top(color,x,y):
    penup()
    fillcolor(color)
    pencolor(color)
    goto(x,y)
    pendown()
    begin_fill()
    rt(90)
    fd(100)
    rt(90)
    fd(500)
    rt(90)
    fd(100)
    rt(90)
    fd(500)
    end_fill()
    
draw_top('#2f4f4f',-300,100)

#Canteen sign

def draw_sign(color,x,y):
    penup()
    fillcolor(color)
    pencolor(color)
    goto(x,y)
    pendown()
    begin_fill()
    rt(90)
    fd(70)
    rt(90)
    fd(300)
    rt(90)
    fd(70)
    rt(90)
    fd(300)
    end_fill()
    penup()
    goto(-150,115)
    pencolor('#ffffff')
    write('Canteen',align='center',font=("Arial",48,'normal'))
    
draw_sign('#263f3f',-280,120)

turtle = Turtle() # create the first turtle
turtle.penup()
turtle.goto(85,-80)
turtle.pendown()
screen.addshape(image)
turtle.shape(image) # set up the callback for moving the first turtle

#Input asking if they want to see the menu, if no, then screen shuts, if yes, menu appears

welcome = screen.textinput("Welcome to Canteen!", "Would you like to see the menu?")
if welcome is None or welcome.lower().startswith('n'):
    print("Thanks for Visiting!")
    screen.clear()
    screen.bye()

else:
    def draw_menu(color,x,y):
        penup()
        fillcolor(color)
        goto(x,y)
        pendown()
        begin_fill()
        rt(90)
        fd(180)
        rt(90)
        fd(260)
        rt(90)
        fd(180)
        rt(90)
        fd(260)
        end_fill()
        penup()
        goto(-260,70)
        pencolor('white')
        write('Sausage Roll',align='left',font=("Arial",15,'normal'))
        goto(-70,70)
        write('$2.50',align='left',font=("Arial",15,'normal'))
        goto(-260,50)
        write('Meat Pie',align='left',font=("Arial",15,'normal'))
        goto(-70,50)
        write('$3.00',align='left',font=("Arial",15,'normal'))
        goto(-260,30)
        write('Frozen juice cups',align='left',font=("Arial",15,'normal'))
        goto(-70,30)
        write('$1.00',align='left',font=("Arial",15,'normal'))
        goto(-260,10)
        write('Yoghurt sticks',align='left',font=("Arial",15,'normal'))
        goto(-70,10)
        write('$0.50',align='left',font=("Arial",15,'normal'))
        goto(-260,-10)
        write('Paddlepop sticks',align='left',font=("Arial",15,'normal'))
        goto(-70,-10)
        write('$2.00',align='left',font=("Arial",15,'normal'))
        goto(-260,-30)
        write('Pizza singles',align='left',font=("Arial",15,'normal'))
        goto(-70,-30)
        write('$1.50',align='left',font=("Arial",15,'normal'))
        goto(-260,-50)
        write('Burrito',align='left',font=("Arial",15,'normal'))
        goto(-70,-50)
        write('$3.00',align='left',font=("Arial",15,'normal'))
        goto(-260,-70)
        write('Hash Brown',align='left',font=("Arial",15,'normal'))
        goto(-70,-70)
        write('$1.00',align='left',font=("Arial",15,'normal'))


draw_menu('black',-270,-80)

goto(85,-80)
addshape(image)
shape(image)

#Order quantity of each food. Input asks if they want to order food. If no, then screen shuts, if yes then input quantity of each food

answer = screen.textinput("Welcome to Canteen!", "Are you ready to order?")
if answer is None or answer.lower().startswith('n'):
    print("Goodbye!")
    screen.clear()
    screen.bye()

#Food item and cost

else:
    print("Start!")
    takeOrder("Sausage Rolls",2.50)
    takeOrder("Party Pies",3.00)
    takeOrder("Frozen juice cups",1.00)
    takeOrder("Yoghurt sticks",0.50)
    takeOrder("Paddlepop sticks",2.00)
    takeOrder("Pizza Singles",1.50)
    takeOrder("Burrito",3.00)
    takeOrder("Hash Brown",1.00)


#Speech bubble appears, with customer's total cost

turtle2 = Turtle()

def draw_speech(color,x,y):
    turtle2.penup()
    turtle2.fillcolor(color)
    turtle2.goto(x,y)
    turtle2.pendown()
    turtle2.begin_fill()
    turtle2.rt(180)
    turtle2.rt(135)
    turtle2.fd(30)
    turtle2.rt(45)
    turtle2.fd(200)
    turtle2.lt(90)
    turtle2.fd(70)
    turtle2.lt(90)
    turtle2.fd(200)
    turtle2.lt(90)
    turtle2.fd(60)
    turtle2.goto(200,10)
    turtle2.end_fill()
    turtle2.penup()
    turtle2.goto(320,60)
    global orderTotal
    if orderTotal > 0:
        turtle2.pencolor('green')
        turtle2.write('Your total is $'+str(orderTotal)+'0',align='center',font=("Arial",15,'normal'))
    else:
        turtle2.pencolor('red')
        turtle2.write('Order not placed',align='center',font=("Arial",15,'normal')) 
    turtle2.goto(320,35)
    turtle2.pencolor('black')
    turtle2.write('Click on screen to exit',align='center',font=("Arial",10,'normal')) 
    turtle2.goto(375,55)
       # turtle2.write(orderTotal,align='left',font=("Arial",20,'normal'))
    turtle2.setpos(0,0)
        
draw_speech('#ffffff',200,10)
exitonclick()
mainloop()

        