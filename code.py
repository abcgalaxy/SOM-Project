try:
    import sys
    import fontstyle as ft
    sys.path.insert(1,'C:/vscode files/codes')
    from test2 import *
    from test3 import *
    from q2 import  *
    from q3 import  *
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
except:
    print("something went wrong")