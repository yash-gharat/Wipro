f=open('abc.txt','w')
# print(f)
f.write('GET')
f.write('SET')
f.write('TECH')
print('Data Written Successfully') 
f.close()
#GETSETTECH
 
f=open('abc.txt','w')
f.write('GET\n')
f.write('SET\n')
f.write('TECH\n')
print('Data Written Successfully') 
f.close()
# GET
# SET
# TECH

 
f=open('abc.txt','a')
f.write('GET\n')
f.write('SET\n')
f.write('TECH\n')
print('Data Written Successfully')
f.close()
f=open('abc.txt','w')
list=['Sachin','Virat','Rohit','Rahul','Dhawan']
f.writelines(list)
print('Data Written Successfully')
f.close()
# SachinViratRohitRahulDhawan
 
 
f=open('abc.txt','r')
data=f.read(20)
print(data) #SachinViratRohitRahu
f.close()

f=open('abc.txt','r')
line1=f.readline()
print(line1)
line2=f.readline()
print(line2)
line3=f.readline()
print(line3)
f.close()

f=open('abc.txt','r')
line1=f.readline()
print(line1,end='')
line2=f.readline()
print(line2,end='')
line3=f.readline()
print(line3,end='')
f.close()

f=open('abc.txt','r')
lines=f.readlines()
for line in lines:
  print(line)
f.close()

f=open('abc.txt','r')
lines=f.readlines()
for line in lines:
    print(line,end='')
f.close()

def read_file(fname):
    f=open(fname+'.txt','r')
    data=f.read()
    print("\n",data)
read_file("flight")
 