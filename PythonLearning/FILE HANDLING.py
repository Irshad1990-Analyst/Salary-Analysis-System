f = open("data.txt", "w")
f.write("Irshad, 3000")
f.close()
f = open("employees.txt", "w")

f.write("Irshad, 3000\n")
f.write("Ahmed, 4000\n")

f.close()
f = open("employees.txt", "r")
print(f.read())

f = open("employees.txt", "r")

data = f.read()

print(data)

f.close()

f = open("employees.txt", "a")
f.write("Irshad, 3000\n")
print("Irshad, 3000")
f.close()
f= open("employees.txt", "a")
f.write("Ahmed, 4000\n")
print("Ahmed, 4000")
f.close()

f = open("employees.txt", "r")

data = f.read()

print(data)

f.close()

f = open("employees.txt", "r")
for line in f:
    print(line)
f.close()




