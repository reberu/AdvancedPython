str1 = 'разработка'
str2 = 'сокет'
str3 = 'декоратор'
str1_bytes = str1.encode('utf-8')
str2_bytes = str2.encode('utf-8')
str3_bytes = str3.encode('utf-8')
print(f'Преобразованная строка "{str1}" имеет тип {type(str1_bytes)} и выглядит так: {str1_bytes}')
print(f'Преобразованная строка "{str2}" имеет тип {type(str1_bytes)} и выглядит так: {str1_bytes}')
print(f'Преобразованная строка "{str3}" имеет тип {type(str1_bytes)} и выглядит так: {str1_bytes}')
