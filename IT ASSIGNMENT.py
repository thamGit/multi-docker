from turtle import*
penup()
goto(-300,-100)
pendown()
bgcolor('#e6ffff')

def draw_bottom(color,x,y):
    fillcolor(color)
    pencolor(color)
    begin_fill()
    fd(500)
    rt(90)
    fd(100)
    rt(90)
    fd(500)
    rt(90)
    fd(100)
    end_fill()
    
draw_bottom('#e6a263',-300,-100)

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
    
draw_middle('#fff2d1',-280,-99)

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
    
draw_top('#6e92ff',-300,100)

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
    goto(-180,170)
    pencolor('black')
    write('Canteen',align='center',font=("Arial",48,'normal'))
    
draw_sign('#ffffff',-280,160)

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
    pencolor('black') 
    write('Sausage Roll',align='left',font=("Arial",15,'normal'))
    goto(-50,70)
    write('$2.50',align='left',font=("Arial",15,'normal'))
    goto(-260,50)
    write('Meat Pie',align='left',font=("Arial",15,'normal'))
    goto(-50,50)
    write('$3.00',align='left',font=("Arial",15,'normal'))
    goto(-260,30)
    write('Frozen juice cups',align='left',font=("Arial",15,'normal'))
    goto(-50,30)
    write('$1.00',align='left',font=("Arial",15,'normal'))
    goto(-260,10)
    write('Yoghurt sticks',align='left',font=("Arial",15,'normal'))
    goto(-50,10)
    write('$0.50',align='left',font=("Arial",15,'normal'))
    goto(-260,-10)
    write('Paddlepop sticks',align='left',font=("Arial",15,'normal'))
    goto(-50,-10)
    write('$2.00',align='left',font=("Arial",15,'normal'))
    goto(-260,-30)
    write('Pizza singles',align='left',font=("Arial",15,'normal'))
    goto(-50,-30)
    write('$1.50',align='left',font=("Arial",15,'normal'))
    goto(-260,-50)
    write('Burrito',align='left',font=("Arial",15,'normal'))
    goto(-50,-50)
    write('$3.00',align='left',font=("Arial",15,'normal'))
    goto(-260,-70)
    write('Hash Brown',align='left',font=("Arial",15,'normal'))
    goto(-50,-70)
    write('$1.00',align='left',font=("Arial",15,'normal'))
    
draw_menu('white',-270,-90)
