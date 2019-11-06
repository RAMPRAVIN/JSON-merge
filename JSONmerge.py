import json
f_p=input("Enter the folder path :")
fn1=input("Enter the input file name 1 :")
fn2=input("Enter the input file name 2 :")
fn3=input("Enter the input file name 3 :")
fn4=input("Enter the output file name :")
fs=int(input("Enter the maximum file size (in bytes) :"))
#content
f1=fn1+'1.json'
f2=fn2+'2.json'
f3=fn3+'3.json'
f4=fn4+'.json'
with open (f_p/f1) as f:
    d1=json.load(f)
with open (f_p/f2) as g:
    d2=json.load(g)
with open (f_p/f3) as h:
    d3=json.load(h)
val=[d1,d2,d3]

#writing
with open(f4,'w') as jsonfile:
    json.dump(val,jsonfile)
