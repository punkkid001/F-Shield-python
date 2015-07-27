# -*- coding : utf-8 -*-

#write file
file_ex=open('example.txt', 'w')
file_ex.write('This is example\n Nice to meet you')
file_ex.flush()
file_ex.close()

#read file
file_ex2=open('example.txt', 'r')
read_string=file_ex2.readlines()
file_ex2.close()

print(read_string)

#delete new-line
print('*** delete new-line***')
print('before : %s'%read_string[0])
print('after : %s'%read_string[0].strip())

#write lines~
data=['too fast\n', 'to live\n', 'too young\n', 'to die.']
file_ex3=open('example2.txt','w')
file_ex3.writelines(data)
file_ex3.close()

#read file using 'for'
print()
print('*** read file - example2.txt ***')

file_ex3=open('example2.txt', 'r')
for line in file_ex3:
    print(line.strip())
