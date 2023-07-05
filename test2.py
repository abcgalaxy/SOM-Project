# This code is for uniformly or non uniformly varying load on cantilevar beam
def TEST2():
    import matplotlib.pyplot as plt    # importing library to plot graph

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