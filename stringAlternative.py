
def string_alternative(Str):
    result=''
    for index in range(len(Str)):
        if index%2==0:
            result+=Str[index]
    return result

print(string_alternative('Good evening'))