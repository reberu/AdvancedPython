str1 = 'разработка'
str2 = 'администрирование'
str3 = 'protocol'
str4 = 'standard'
str1_byte = str1.encode('utf-8')
print(str1_byte, type(str1_byte))
str1_byte_str = str1_byte.decode('utf-8')
print(str1_byte_str, type(str1_byte_str))
str2_byte = str2.encode('utf-8')
print(str1_byte, type(str1_byte))
str2_byte_str = str2_byte.decode('utf-8')
print(str2_byte_str, type(str2_byte_str))
str3_byte = str3.encode('latin-1')
print(str3_byte, type(str3_byte))
str3_byte_str = str3_byte.decode('latin-1')
print(str3_byte_str, type(str3_byte_str))
str4_byte = str4.encode('latin-1')
print(str4_byte, type(str4_byte))
str4_byte_str = str4_byte.decode('latin-1')
print(str4_byte_str, type(str4_byte_str))
