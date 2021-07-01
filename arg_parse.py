import sys
if len(sys.argv)!=3:
   print("Error In Suff args/Overflow")
   print("Usage : ")
   print("$ python %s int int " %(sys.argv[0]))
else:
   a = sys.argv[1]
   b = sys.argv[2]
   if a.isdigit() and b.isdigit():
       res = int(a) + int(b)
       print("Result = ",res)
   else:
       print("Error Invalid args")
       print("Usage : ")
       print("$ python %s int int " %(sys.argv[0]))
	   
	   ==========================================================================
OR with exception handling

	
	==============================================================================
import argparse
p = argparse.ArgumentParser() 
p.add_argument("-a","--op1", type=int, action="store",dest="opt1")
p.add_argument("-b","--op2", type=int, action="store",dest="opt2")
p.add_argument("-o","--oper", type=str, action="store",dest="opt3")
args = p.parse_args()  # parse it
if args.opt1 and args.opt2 and args.opt3:
  a = args.opt1
  b = args.opt2
  if args.opt3=="add":
    res = a +b
    print("REsut = ",res)
else:
  print("Error Isuff args")
=================================================================================
import argparse
p = argparse.ArgumentParser() 
p.add_argument("-a","--op1", type=int, action="store",dest="opt1")
p.add_argument("-b","--op2", type=int, action="store",dest="opt2")
p.add_argument("-o","--oper", type=str, action="store",dest="opt3")
args = p.parse_args()  # parse it
if args.opt1 and args.opt2 and args.opt3:
  valid=("add","mul","div","sub")
  a = args.opt1
  b = args.opt2
  if args.opt3 in valid:
    if args.opt3=="add":
      res = a +b
    elif args.opt3=="sub":
      res = a-b
    elif args.opt3=="mul":
      res = a*b
    elif args.opt3=="div":
      res = a/b
    print("REsut = ",res)
  else:
    print("Invalid operation")
else:
  print("Error Isuff args")
============================================
import sys
sys.stdin  = open("data.txt")
sys.stdout = open("out.txt", "w")
sys.stderr = open("err.txt", "w")
a = input()
b = input()
oper = input().split("=")[-1].strip()
if oper == "add":
  res=a+b
  print("Result",res)
