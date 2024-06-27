#file = open("yay.txt", "r")
#var = file.readlines()
#print(var)

#var = [line.strip() for line in open("yay.txt")]
#for i in var:
#    print(i)

#file = open("yay.txt", "r")
#for i in file.readlines():
#    print(i)

#file = open("yay.txt", "w")
#file.write("zyay\n")
#file.write("kaduot ")
#file.write("numan\n")
#file.close()

while True:
    write = open("yay.txt", "a")
    name = input("name: ")
    print(name, file=write)
    write.close()
