# static

class Emp:
    cname='wipro'
    def __init__(self,eid,ename):
        self.eid=eid
        self.ename=ename


e1=Emp(101,'john')
e2=Emp(102,'harry')
print(e1.eid)
print(e2.eid)
print(Emp.cname)
print(e1.cname,e2.cname)
Emp.cname = "TCS" 
print(e1.cname,e2.cname)