import Expression.Expression as Expression
import os
step=0
while 1:
    step+=1
    print('\n# '+str(step)+' #\n'+10*'-'+'\n# Options \n' +'Please input your option!\n\tinput\n\treload\n\texit\n'+10*'-'+'\n'+'Your OPTION: ', end='')
    opt=input()
    if(opt=='input'):
        print(10*'-'+'\n# Tips\n' +'Please input your expression!'+'\n'+10*'-'+'\n'+'Your INPUT: ', end='')
        expression=Expression.Expression()
        if(expression.Check()==0):
            expression.DrawTree()
    elif(opt=='reload'):
        expression=Expression.Expression(is_reload=True)
        if(expression.is_reload):
            expression.DrawTree()
    elif(opt=='exit'):
        break
    else:
        print('\n# ERROR\n' +'Please input your option correctly!')
    os.system('pause')