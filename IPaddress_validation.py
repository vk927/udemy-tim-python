ip=input("enter your IP address \n",)
ip_array=ip.split(".")
note=''

note2=''
xp=list(ip)
if xp[0]=='.':
    note2='beta'

for i in ip:
    if i in ".1234567890":
      continue
    else:
        note="alpha"
        break

x=0
if note!="alpha":
    x+=1
else:
    print("Invalid format please don't enter only numbers and period")


if len(ip_array)==4:
    x+=1
else:
    print("Invalid IP Address, Enter in 4 octat form as x.x.x.x")

if(note2!="beta"):
    if (1<=int(ip_array[0])<=255) and (1<=int(ip_array[1])<=255) and (1<=int(ip_array[2])<=255) and (1<=int(ip_array[3])<=255):
        x+=1
    else:
        print("Invalid IP Adress, Enter IP Address with octat numbers between 1 and 255")
else:
    print("Invalid IP Adress, please dont start with oeriod")


if x==4:
    print("valid IP address")
    print("Ping",ip)




