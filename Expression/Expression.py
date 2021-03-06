import re
from Stack.Stack import Stack
from Node.Node import Node
class Expression:
    # the checking regular expression
    regex = [
        # wrong number of operands
        '[\+\-\*\/][0-9][\+\-\*\/]+|\([^\+\-\*\/]\)|[\+\-\*\/]\([^\(\)]+\)[\+\-\*\/]',
        # brackets mismatched
        '[0-9]\(|\)[0-9]',
        '[^0-9\+\-\*\/\(\)]'
    ]
    # error message
    err_msg=[
        'Not a valid expression, wrong number of operands.',
        'Not a valid expression, operator missing.',
        'Not a valid expression, expression contains invalid characters.',
        'Not a valid expression, brackets mismatched.',
        'Not a valid expression, expression should not be empty.'
    ]
    # init function, input or reload the expression
    def __init__(self,is_reload=False):
        if(is_reload):
            if(not self._ReloadExpression()):
                print('No more expressions to reload.\n')
        else:
            self._expression=self._ReadExpression()
    # check function, find the valid expression and report why the expression is not valid
    def Check(self):
        self.err=[]
        if(len(self._expression)==0):
            self.err.append(4)
            print(self.err_msg[self.err[0]])
            return len(self.err)
        for i in range(len(self.regex)):
            if(re.findall(self.regex[i],self._expression)):
                self.err.append(i)
        if(self._expression[0]!='(' or self._expression[-1]!=')'):
            self.err.append(3)
        else:
            symb=re.findall('[\(\)]',self._expression[1:-1])
            if(len(symb)%2!=0):
                self.err.append(3)
            elif(len(symb)!=0 and (symb[0]==')' or symb[-1]=='(')):
                self.err.append(3)
        for i in self.err:
            print(self.err_msg[i])
        if(len(self.err)==0):
            self._SaveTree()
        return len(self.err)
    # the function to print tree on terminal
    def DrawTree(self):
        tree=self._ExpressionToTree(self._expression)
        print(10*'-','\n',"Expression's value: ",eval(self._expression),'\n',"Expression's tree: \n")
        box=self._PrintTree(tree)
        print(10*'-')
        return eval(self._expression),box
    # the function to saving expression in file
    def _SaveTree(self):
        with open('Expression.txt','a') as f:
            f.write(self._expression+'\n')
    # the function to reload history expression from file and let user to choose one
    def _ReloadExpression(self):
        with open('Expression.txt','r')as f:
            reader=f.readlines()
            exp=[]
            for i in reader:
                exp.append(re.findall(r'[1-9\(\)\+\-\*\/]+',i))
            for i in range(len(exp)-1,-1,-1):
                print('\r', len(exp)-i,' : ', 'Is ', exp[i][0], '? [y/n]:', end='')
                ans = input()
                if(ans=='y'):
                    self._expression=exp[i][0]
                    print(self._expression)
                    self.is_reload=True
                    return 1
            self.is_reload=False
            return 0
    # input expression from terminal
    def _ReadExpression(self):
        s=input()
        return s
    # change expression to binary tree
    def _ExpressionToTree(self, s):
        expr=Stack()
        symb=Stack()
        for i in range(len(s)):
            if s[i]=='(':
                symb.push('(')
            elif s[i]==')':
                while symb.size()>0 and symb.top()!='(':
                    expr.push(symb.pop())
                if(symb.top()=='('):
                    symb.pop()
            elif s[i]=='+' or s[i]=='-' or s[i]=='*' or s[i]=='/':
                symb.push(s[i])
            else:
                expr.push(s[i])
        result=Stack()
        tree_stack=Stack()
        while expr.size()>0:
            tree_stack.push(expr.pop())
        while tree_stack.size()>0:
            if(tree_stack.top() == '+' or tree_stack.top() == '-' or tree_stack.top() == '*' or tree_stack.top() == '/'):
                node = Node(tree_stack.top())
                node.setR(result.pop())
                node.setL(result.pop())
                result.push(node)
                tree_stack.pop()
            else:
                result.push(tree_stack.pop())
        return result.top()
    # put tree's node into a matrix
    def _AddBox(self,tree,box,level,x,y):
        box[y][x]=tree.getVal()
        delta=2**(level-2)*3 if level>1 else 2
        for i in range(1,delta):
            box[y+i][x-i]='/'
            box[y+i][x+i]='\\'
        if(tree.getL()!=None and (not isinstance(tree.getL(),str))):
            self._AddBox(tree.getL(), box, level-1, x-delta, y+delta)
        elif(isinstance(tree.getL(),str)):
            box[y+delta][x-delta] = tree.getL()
        if(tree.getR()!=None and (not isinstance(tree.getR(),str))):
            self._AddBox(tree.getR(), box, level-1, x+delta, y+delta)
        elif(isinstance(tree.getR(),str)):
            box[y+delta][x+delta] = tree.getR()
        return box
    # from matrix print tree
    def _PrintTree(self,tree):
        boxwidth=2**tree.getHeight()*3-1
        boxheight = 2**(tree.getHeight()-1)*3
        box=[]
        for i in range(boxheight):
            l=[]
            for j in range(boxwidth):
                l.append('@')
            box.append(l)
        box=self._AddBox(tree,box,tree.getHeight(),int((boxwidth-1)/2),0)
        for i in box:
            s=''
            for j in i:
                s+=j if j!='@' else ' '
            print(s)
        return box