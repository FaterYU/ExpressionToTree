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