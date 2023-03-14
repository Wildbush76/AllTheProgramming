import time

def db(num,base):
    if base == 2:
        return str(bin(num)).replace("0b","") + " "
    base_num = ""
    while num>0:
        dig = int(num%base)
        if dig<10:
            base_num += str(dig)
        else:
            base_num += chr(ord('A')+dig-10)
        num //= base
    base_num = base_num[::-1]  
    return base_num + " "

def convertString(string,base):
    Stringy = [db(ord(x),base) for x in string]
    
    Stringy = "".join(Stringy)
    base -=1 
    if base <= 1:
        return Stringy
    else:
        print(base)
        return convertString(Stringy,base)
    
    
    
    

count = int(input("count down from what "))
message = input("whats your message ")
with open("the.txt","w") as file:
    file.write(convertString(message,count))
print("done")
