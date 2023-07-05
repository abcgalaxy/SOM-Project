import fontstyle as ft
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter

#To run this code u need to install python , matplotlib and  fontstyle module

    # This function is for simply supported beam of constant and varying load
def Q2():
    a=float(input('coefficient of x^2:'))
    b=float(input('coefficient of x^1:'))
    c=float(input('coefficient of x^0:'))   #the load is in the form ax^2+bx+c
    l=float(input('length of beam:'))       #consiered load upwards as positive so put negative sign when load is downwards
    x=0.00
    x_ordinate=[]
    shear=[]
    moment=[]
    B_y=-((a*l**3)/4+(b*l**2)/3+c*l/2)       #Finding reactions at Hinge(A_y) and roller(B_y)
    A_y=-((a*l**3)/3+(b*l**2)/2+c*l+B_y)
    while x<=l:
        x_ordinate.append(x)
        f=A_y+(a*x**3)/3+(b*x**2)/2+c*x
        shear.append(f)
        m=f*x-((a*x**4)/4+(b*x**3)/3+(c*x**2)/2)
        moment.append(m)
        x+=l/40
    if x!=l:                                 # I considered this case due to floating point error
        x=l
        x_ordinate.append(x)
        f=A_y+(a*x**3)/3+(b*x**2)/2+c*x
        shear.append(f)
        m=f*x-((a*x**4)/4+(b*x**3)/3+(c*x**2)/2)
        moment.append(m)

    fig=plt.figure()
    d, =plt.plot([],[],'#A020F0',label='shear graph')
    e, =plt.plot([],[],'#FF0000',label='Bending moment')

    f=min(shear)
    g=min(moment)
    h=max(shear)
    i=max(moment)
    plt.xlim(0,l+3)
    plt.ylim(min(f,g)-2,max(h,i)+2)
    plt.xlabel('Distance / x co-ordinate',fontname="Gabriola",fontsize=20)
    plt.ylabel('shear force / bending moment',fontname="Gabriola",fontsize=20)
    #plt.title('shear force and bending moment diagram',fontsize=15)
    plt.grid(True)
    plt.legend()

    list1=[]
    list2=[]
    list3=[]
    writer=PillowWriter(fps=10)           #This section is to create gif of graphs
    j=0
    with writer.saving(fig,'graph.gif',100):   #gif name is graph.gif
        for k in x_ordinate:
            list1.append(k)
            list2.append(shear[j])
            list3.append(moment[j])
            j+=1
            d.set_data(list1,list2) #plotting x and shear
            e.set_data(list1,list3) #plotting x and moment
            writer.grab_frame()  #grabbing that frame to create gif

    plt.show()  #To show the figure 

        # This function is for simple supported beam of concerated loads and moments
def Q3():
    plt.style.use('dark_background')
    l=float(input("length of beam:"))  
    dic_y={}
    dic_m={}
    A_y=0.00
    B_y=0.00
    j=0.00
    i=0
    i1=0
    LINE_UP = '\033[1A'
    LINE_CLEAR = '\x1b[2K'
    #  Note:  here i am taking unlimited inputs from user 
    # when user entered the all inputs just press enter(only when it is asking x position)
    while True:     #this loop is to take force value and its x position
        t=input(ft.apply("Enter the value of x_position(for force):",'PURPLE/UNDERLINE/ITALIC'))
        if t == "":
            print(LINE_UP, end=LINE_CLEAR) 
            break
        f=float(input("value of force in the y direction:")) # force is positive in positive y direction , so if the load is downwards give negative sign
        j+=f
        dic_y[float(t)]=f
        dic_m[float(t)]=[0,f]
        B_y-=float(t)*f/l
        if t==l:
            i=1
    if i==0:
        dic_y[l]=0

    #note: please don't give moment and force at same x  .  otherwise it will give wrong values
    while True:  #  This loop is to take momentvalue and its position clockwise is -ve
        t=input(ft.apply("Enter the value of x_position(for moment):",'RED/UNDERLINE/ITALIC'))
        if t == "":
            print(LINE_UP, end=LINE_CLEAR)
            break
        f=float(input("value of moment in the z direction:")) 
        dic_m[float(t)]=[1,f]
        B_y-=f/l
        if t==l:
            i1=1
    if i==0 and i1==0:
        dic_m[l]=[1,0]
    A_y=-B_y-j
    x=0
    g=0
    a=0.00
    x_ordinate=[]
    x1_ordinate=[]
    shear=[]
    moment=[]
    for k in sorted(dic_y.keys()):
        t=(k-g)/10
        while True:
            f=A_y+a
            x_ordinate.append(x)
            shear.append(f)
            x+=t
            if x>k:
                x=k
                x_ordinate.append(x)
                shear.append(f)
                a+=dic_y[k]
                g=k
                break
    x=0.00
    g=0.00
    a=A_y
    d=0.00
    p=0.00
    for k in sorted(dic_m.keys()):
        t=(k-g)/10
        while True:
            if x>k:
                if dic_m[k][0]==0:
                    a+=dic_m[k][1]
                    p-=k*dic_m[k][1]
                else:
                    d-=dic_m[k][1]
                g=k
                x=k
                m=a*x+d+p
                moment.append(m)
                x1_ordinate.append(x)
                break
            m=a*x+d+p
            moment.append(m)
            x1_ordinate.append(x)
            x+=t

    fig=plt.figure()
    s1, =plt.plot([],[],'#A020F0',label='shear graph')
    s2, =plt.plot([],[],'#FFFFFF',label='Bending moment')

    p=min(shear)
    q=min(moment)
    r=max(shear)
    s=max(moment)
    plt.xlim(0,l+3)
    plt.ylim(min(p,q)-2,max(r,s)+2)
    plt.xlabel('Distance / x co-ordinate',fontname="Gabriola",fontsize=20)
    plt.ylabel('shear force / bending moment',fontname="Gabriola",fontsize=20)
    plt.legend()

    list1=[]
    list2=[]
    list3=[]
    list4=[]
    writer=PillowWriter(fps=7)
    i=0
    with writer.saving(fig,'graph.gif',100):
        for k in x_ordinate:
            list1.append(k)
            list2.append(shear[i])
            i+=1
            s1.set_data(list1,list2)
            writer.grab_frame()
        i=0
        for k in x1_ordinate:
            list3.append(k)
            list4.append(moment[i])
            i+=1
            s2.set_data(list3,list4)
            writer.grab_frame()
    plt.show()

          # This  is function is for uniformly or non uniformly varying load on cantilevar beam
def TEST2():
    a=float(input('coefficient of x^2:'))
    b=float(input('coefficient of x^1:'))
    c=float(input('coefficient of x^0:'))
    w=float(input('weight of beam:'))
    l=float(input('length of beam:'))
    x=0.00
    x_ordinate=[]
    shear=[]
    moment=[]
    R_y=w-(a*(l**3)/3)-(b*(l**2)/2)-c*l
    M_z=a*(l**4)/4+b*(l**3)/3+c*(l**2)/2-w*l/2

    fig1,ax1=plt.subplots()
    fig2,ax2=plt.subplots()
    while x<=l:
        f=R_y-(w/l)*x+a*(x**3)/3+b*(x**2)/2+c*x
        x_ordinate.append(x)
        shear.append(f)
        m=-a*(x**4)/4-b*(x**3)/3-c*(x**2)/2+((w/l)*x**2)/2+f*x+M_z
        moment.append(m)
        x+=l/50
        ax1.plot(x_ordinate,shear,color='#A020F0')
        ax2.plot(x_ordinate,moment,color='b')

    ax1.set_xlabel('Distance / x co-ordinate',fontname="Gabriola",fontsize=18)
    ax1.set_ylabel('shear force ',fontname="Gabriola",fontsize=18)
    ax1.set_title('shear force diagram',fontsize='16')

    ax2.set_xlabel('Distance / x co-ordinate',fontname="Gabriola",fontsize=18)
    ax2.set_ylabel('Bending moment ',fontname="Gabriola",fontsize=18)
    ax2.set_title('Bending moment diagram',fontsize=16)
    ax1.legend(['shear graph'])
    ax2.legend(['bending moment graph'])
    plt.show()

          # This function is for cantilevar beam of concerated loads and moments
def TEST3():
    LINE_UP = '\033[1A'
    LINE_CLEAR = '\x1b[2K'
    plt.style.use('seaborn-v0_8-darkgrid')
    l=float(input("length of beam:"))  
    dic_y={}
    dic_m={}
    R_y=0.00
    i=0
    i1=0
    M_z=0.00
    while True:
        t=input(ft.apply("Enter the value of x_position(for force):","YELLOW_BG/ITALIC"))
        if t == "":
            print(LINE_UP, end=LINE_CLEAR)
            break
        f=float(input("value of force in the y direction:")) 
        R_y-=f
        dic_y[float(t)]=f
        M_z+=f*float(t)
        dic_m[float(t)]=[0,f]
        if t==l:
            i=1
    if i==0:
        dic_y[l]=0
    while True:
        t=input(ft.apply("Enter the value of x_position(for moment):",'RED/UNDERLINE/ITALIC'))
        if t == "":
            print(LINE_UP, end=LINE_CLEAR)
            break
        f=float(input("value of moment in the z direction:")) 
        dic_m[float(t)]=[1,f]
        M_z+=f
        if t==l:
            i1=1
    if i==0 and i1==0:
        dic_m[l]=[1,0]
    x=0.00
    g=0.00
    a=0.00
    x_ordinate=[]
    x1_ordinate=[]
    shear=[]
    moment=[]

    fig,(ax1,ax2)=plt.subplots(nrows=2,ncols=1,sharex=True)
    for k in sorted(dic_y.keys()):
        t=(k-g)/100
        while True:
            if x>=k:
                x=k
                x_ordinate.append(x)
                shear.append(f)
                a+=dic_y[k]
                g=k
                break
            f=R_y+a
            x_ordinate.append(x)
            shear.append(f)
            x+=t
    x=0.00
    g=0.00
    p=0.00
    d=M_z
    a=R_y
    for k in sorted(dic_m.keys()):
        t=(k-g)/10
        while True:
            if x>k:
                x=k
                moment.append(m)
                x1_ordinate.append(x)
                if dic_m[k][0]==0:
                    a+=dic_m[k][1]
                    p-=k*dic_m[k][1]
                else:
                    d-=dic_m[k][1]
                g=k
                break
            m=a*x+d+p
            moment.append(m)
            x1_ordinate.append(x)
            x+=t
    ax1.plot(x_ordinate,shear,color='#A020F0')
    ax2.plot(x1_ordinate,moment,color='b')
    ax1.set_ylabel('shear force',fontname="Gabriola",fontsize=18)
    ax2.set_ylabel('Bending moment',fontname="Gabriola",fontsize=18)
    ax2.set_xlabel('distance',fontname="Gabriola",fontsize=18)
    ax1.legend(['shear force'])
    ax2.legend(['Bending moment'])
    ax1.grid(True)
    ax2.grid(True)
    plt.show()


print('SIMPLE SUPPORTED BEAM\n\t1)uniformly distributed load\n\t2)uniformly varying load\n\t3)point loads\nCANTILEVAR BEAM\n\t4)uniformly distributed load\n\t5)uniformly varying load\n\t6)point loads')
t=int(input(ft.apply('choose the option:','GREEN')))
if t==1 or t==2:
    Q2()
if t==3:
   Q3()
if t==4 or t==5:
    TEST2()
if t==6:
    TEST3()