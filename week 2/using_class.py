from class_ex import example #python class import another file
from class_ex import new_example

#using example class
A=example("atom")
B=example("Bob")

sentence_A="class! class! help me!"
A.textViewer(sentence_A)

sentence_B="major lazer"
B.textViewer(sentence_B)

#using new_example class
C=new_example("Jerry")
D=new_example("Tom")

C.printName()
D.printName()
