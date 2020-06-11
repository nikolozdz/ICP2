def ibsToKgs(ibs:list):
    kgs=list()
    for pound in ibs:
        kgs.append(round(pound*0.45359237,2))
    return kgs

def inp(TYPE): # input function which autmoatically catches errors
    while True:
        try:
            if TYPE==int:
                N = int(input()) #if type indicated inp(int) is called and user enters float it will crash
            elif TYPE ==float:
                N = float(input()) # if inp(float) is called and user inputs something else than numbers it will throw exception
            else:
                return -1
            return N
        except ValueError:
            print("Please input float/integer type. Try again.")

print("Please input the size of a List:")
N= inp(int)

ibs=[] #user will initialize this list
for i in range(N):
    print("Enter element {} :".format(i+1),end=" ")
    ibs.append(inp(float)) #append value entered by user

print(ibsToKgs(ibs)) #final result