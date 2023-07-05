# This code is for simple supported beam of concerated loads
def Q3():
    import matplotlib.pyplot as plt
    from matplotlib.animation import PillowWriter     # importing pillowwriter from matplotlib to animate the graph
    import fontstyle as ft
    plt.style.use('dark_background')
    l=float(input("length of beam:"))  # length of beam
    dic_y={}
    dic_m={}
    A_y=0.00
    B_y=0.00
    j=0.00
    i=0
    i1=0
    LINE_UP = '\033[1A'
    LINE_CLEAR = '\x1b[2K'
    while True:
        t=input(ft.apply("Enter the value of x_position(for force):",'PURPLE/UNDERLINE/ITALIC'))
        if t == "":
            print(LINE_UP, end=LINE_CLEAR)
            break
        f=float(input("value of force in the y direction:")) # force is positive in positive y direction
        j+=f
        dic_y[float(t)]=f
        dic_m[float(t)]=[0,f]
        B_y-=float(t)*f/l
        if t==l:
            i=1
    if i==0:
        dic_y[l]=0
    while True:
        t=input(ft.apply("Enter the value of x_position(for moment):",'RED/UNDERLINE/ITALIC'))
        if t == "":
            print(LINE_UP, end=LINE_CLEAR)
            break
        f=float(input("value of moment in the z direction:")) # force is positive in positive y direction
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
            #print(x," ",t)
            if x>k:
                x=k
                #print(x," ",t)
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
