country = input('你來自哪個國家')
age = input('你幾歲')
age = int(age)
if country == '台灣':
    if age >= 18:
    	print('台灣')
    else:
    	print('你還不能考駕照')
elif country == '美國':
    if age >= 16:
    	print('你可以考駕照')
    else:
    	print('你還不能考駕照')

