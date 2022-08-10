print(' *** Wind classification ***')
speed = float(input('Enter wind speed (km/h) : '))
print('Wind classification is ', end='')
if speed >= 209:
    print('Super Typhoon.')
elif speed >= 102:
    print('Typhoon.')
elif speed >= 56:
    print('Tropical Storm.')
elif speed >= 52:
    print('Depression.') 
elif speed >= 0:
    print('Breeze.')