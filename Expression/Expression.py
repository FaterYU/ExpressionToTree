import re
class Stack:
    def  __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def top(self):
        if(self.size()==0):
            return None
        else:
            return self.items[-1]
    def pop(self):
        top=self.items[-1]
        self.items.pop()
        return top
    def size(self):
        return len(self.items)
class Node:
    def __init__(self,val):
        self.val=val
        self.l=None
        self.r=None
    def getVal(self):
        return self.val
    def getL(self):
        return self.l
    def getR(self):
        return self.r
    def setL(self,l):
        self.l=l
    def setR(self,r):
        self.r=r
    def getAll(self):
        result=[self.val]
        if(type(self.l)==str):
            result.append(self.l)
        else:
            result.append(self.l.getAll())
        if(type(self.r)==str):
            result.append(self.r)
        else:
            result.append(self.r.getAll())
        return result
    def getHeight(self):
        if(isinstance(self.l, str) and isinstance(self.r, str)):
            return 1
        elif(isinstance(self.l, str) and isinstance(self.r, Node)):
            return self.r.getHeight()+1
        elif(isinstance(self.l, Node) and isinstance(self.r, str)):
            return self.l.getHeight()+1
        else:
            return max(self.l.getHeight(),self.r.getHeight())+1
class Expression:
    regex = [
        '[\+\-\*\/][0-9][\+\-\*\/]+',
        '\([^\+\-\*\/]\)',
        '[\+\-\*\/]\([^\(\)]+\)[\+\-\*\/]',
        '@',
        '@',
        '@',
        '[0-9]\(|\)[0-9]',
    ]
    def __init__(self):
        self._expression=self._ReadExpression()
    def Check(self):
        self.err=[]
        for i in range(len(self.regex)):
            # if(isinstance(self.regex[i],list)):
            #     exp=self._expression
            #     for j in range(self.regex-1):
            #         exp=''.join(re.findall(self.regex[j],exp))
            #     if(re.findall(self.regex[i][-1],exp)):
            #         self.err.append(i)
            # else:
            if(re.findall(self.regex[i],self._expression)):
                self.err.append(i)
        return self.err
    def DrawTree(self):
        tree=self._ExpressionToTree(self._expression)
        self._PrintTree(tree)
    def SaveTree(self):
        pass
    def _ReadExpression(self):
        s=input()
        return s
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

# expression=Expression()
# print(expression.Check())