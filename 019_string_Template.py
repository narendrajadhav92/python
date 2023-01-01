from string import Template

Student = [('Ram',90), ('Ankit',78), ('Bob',92)]
 
# We are creating a basic structure to print the name and
# marks of the students.
t = Template('Hi $name, you have got $marks marks')
 
for i in Student:
    print (t.substitute(name = i[0], marks = i[1]))

'''
The ${Identifier} works similar to that of $Identifier.
It comes in handy when valid identifier characters follow 
the placeholder but are not part of the placeholder. '''

template = Template( 'That ${noun} looks ${noun}y')
string = template.substitute(noun='Fish')
print(string)