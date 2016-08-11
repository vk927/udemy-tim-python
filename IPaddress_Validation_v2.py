ipAddress = input("Please enter an IP address: ")

position = 1
segment = 1
number = ''
errorMessage = ''

for digit in ipAddress:
    if digit != '.':
        # we havent got a full stop, so we should have a digit
        if digit in '0123456789':
            number += digit
        else:
            errorMessage = "Error in position {} in section {}, invalid character {}".format(position, segment,digit)
            break
    else:
        # we have a full stop, check the length of the number that we've built up so far
        if(len(number) == 0) or (len(number) > 3):
            errorMessage = "Error near position {} in section {}, each number must be 1 to 3 digits".format(position,segment)
            break
        number = ''
        segment += 1
        if segment > 4:
            errorMessage = "Error near position {}, IP address contains more than 4 segments".format(position)
            break
    position += 1
else:
    if(len(number) == 0) or (len(number) > 3):
        errorMessage = "Error near position {} in section {}, each number must be 1 to 3 digits".format(position, segment)
    elif position > 16:
        errorMessage = "Error: IP address can not be more than 15 characters, {} found".format(position)
    elif segment != 4:
        errorMessage = "Error near position {}, IP address contains {} segments, 4 required".format(position, segment)
    else:
        print("ping {}".format(ipAddress))
if errorMessage:
    print(ipAddress)
    print(' ' * (position -1) + '^')
    print(errorMessage)
