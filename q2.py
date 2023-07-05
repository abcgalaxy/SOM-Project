    # This code is for simple supported beam of constant and varying load
def Q2():
    import matplotlib.pyplot as plt   
    from matplotlib.animation import PillowWriter   
    a=float(input('coefficient of x^2:'))
    b=float(input('coefficient of x^1:'))
    c=float(input('coefficient of x^0:'))
    l=float(input('length of beam:'))
    x=0.00
    x_ordinate=[]
    shear=[]
    moment=[]
    B_y=-((a*l**3)/4+(b*l**2)/3+c*l/2)
    A_y=-((a*l**3)/3+(b*l**2)/2+c*l+B_y)
    while x<=l:
        x_ordinate.append(x)
        f=A_y+(a*x**3)/3+(b*x**2)/2+c*x
        shear.append(f)
        m=f*x-((a*x**4)/4+(b*x**3)/3+(c*x**2)/2)
        moment.append(m)
        x+=l/40
    if x!=l:
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
    writer=PillowWriter(fps=10)
    j=0
    with writer.saving(fig,'graph.gif',100):
        for k in x_ordinate:
            list1.append(k)
            list2.append(shear[j])
            list3.append(moment[j])
            j+=1
            d.set_data(list1,list2)
            e.set_data(list1,list3)
            writer.grab_frame()

    plt.show()
