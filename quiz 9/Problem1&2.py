# Sarah Stephenson
#Problem 1
fout=open("notep1.txt", "w")
line1= "Hello, My name is Sarah  \n"
line2= " I am feeling sleepy\n"
line3= "How are you today \n"
line4= "What school do you go to  \n"
line5= "I go to Saint Mary's \n"

fout.write(line1)
fout.write(line2)
fout.write(line3)
fout.write(line4)
fout.write(line5)

fout.close()
# Problem 2

fin = open("notep1.txt", "r")
for line in fin:
    print(line)
