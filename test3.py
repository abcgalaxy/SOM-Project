# This code is for cantilevar beam of concerated loads
def TEST3():
    import matplotlib.pyplot as plt
    import fontstyle as ft
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
