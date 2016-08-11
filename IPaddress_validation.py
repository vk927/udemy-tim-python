ip=input("enter your IP address \n",)
ip_array=ip.split(".")
note=''
for i in ip:
    if i in ".1234567890":
      continue
    else:
        note="alpha"
        break
if note!="alpha":
    if len(ip_array)==4:
        if (1<=int(ip_array[0])<=255) and (1<=int(ip_array[1])<=255) and (1<=int(ip_array[2])<=255) and (1<=int(ip_array[3])<=255):
            print("valid IP address")
            print ("ping",ip)
        else:
            print("Invalid IP Adress, Enter IP Address with octat numbers between 1 and 255")
    else:
        print("Invalid IP Address, Enter in 4 octat form as x.x.x.x")
else:
    print("Invalid format please don't enter only numbers and period")




