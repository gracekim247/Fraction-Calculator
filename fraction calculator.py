import sys

def gcd(x,y):
    if y<0:
        y*=-1
    if x<0:
        x*=-1
    if x>y:
        small = y
    else:
        small = x
    for i in range(1, small+1):
        if x%i==0 and y%i==0:
            g = i
    return g

def simplify_fraction(dictiona):
    num = dictiona["numerator"]
    den = dictiona["denominator"]
    new_dic = {}
    if num==0:
        new_dic["numerator"] = int(0)
        new_dic["denominator"] = int(0)
    else:
        d = gcd(num, den)
        new_dic["numerator"] = int(num/d)
        new_dic["denominator"] = int(den/d)
        if new_dic["denominator"]<0:
            new_dic["denominator"]*=-1
            new_dic["numerator"]*=-1
    return new_dic

def get_fraction():
    frac = {}
    f = input("Enter a fraction (a/b): ")
    if "/" in f:
        f_split = f.split("/")
        if len(f_split)>2:
            print("Error! Fractions are of the form a/b, where a and b are integers.")
            sys.exit()
    else:
        print("Error! Fractions are of the form a/b, where a and b are integers.")
        sys.exit()
    try:
        f_split[0]=int(f_split[0])
        f_split[1]=int(f_split[1])
    except ValueError:
        print("Error! Fractions are of the form a/b, where a and b are integers.")
        sys.exit()
    if f_split[1]==0:
        print("Error! Can't have a zero denominator.")
        sys.exit()
    frac["numerator"]=f_split[0]
    frac["denominator"]=f_split[1]
    return simplify_fraction(frac)

def get_operation():
    op = input("Enter operation (+,-,*,/): ")
    if op=='+' or op=='-' or op=='*' or op=='/':
        return op
    else:
        print("Error! Operation must be +,-,*,/.")
        sys.exit()

def add_fractions(f1,f2):
    add_frac = {}
    denom_val1 = f1["denominator"]
    denom_val2 = f2["denominator"]
    numer = (f1["numerator"]*denom_val2)+(f2["numerator"]*denom_val1)
    denom = f1["denominator"]*denom_val2
    add_frac["numerator"]=numer
    add_frac["denominator"]=denom
    return simplify_fraction(add_frac)

def subtract_fractions(f1,f2):
    denom_val1 = f1["denominator"]
    denom_val2 = f2["denominator"]
    numer = (f1["numerator"]*denom_val2)-(f2["numerator"]*denom_val1)
    denom = f1["denominator"]*denom_val2
    sub = {}
    sub["numerator"]=numer
    sub["denominator"]=denom
    return simplify_fraction(sub)

def multiply_fractions(f1,f2):
    numer = f1["numerator"]*f2["numerator"]
    denom = f1["denominator"]*f2["denominator"]
    mult_frac = {}
    mult_frac["numerator"]=numer
    mult_frac["denominator"]=denom
    return simplify_fraction(mult_frac)

def divide_fractions(f1,f2):
    if f2["denominator"]==0:
        print("Error! Can't divide by a zero fraction.")
        sys.exit()
    numer = f1["numerator"]*f2["denominator"]
    denom = f1["denominator"]*f2["numerator"]
    div_frac = {}
    div_frac["numerator"]=numer
    div_frac["denominator"]=denom
    return simplify_fraction(div_frac)

def print_fraction(fr):
    numlist = []
    numlist.append(fr["numerator"])
    if fr["denominator"]==1 or fr["denominator"]==0:
        print(str(numlist[0]), end=" ")
    else:
        numlist.append(fr["denominator"])
        print(str(numlist[0])+"/"+str(numlist[1]), end=" ")

def print_results(first,operation,second,result):
    print_fraction(first)
    print(operation, end=" ")
    print_fraction(second)
    print("=", end=" ")
    print_fraction(result)
    

one = get_fraction()
o = get_operation()
two = get_fraction()
if o=="+":
    r = add_fractions(one,two)
elif o=="-":
    r = subtract_fractions(one,two)
elif o=="*":
    r = multiply_fractions(one,two)
elif o=="/":
    r = divide_fractions(one,two)
print_results(one, o, two, r)


