from random import randint

# generate some integers

with open('data.csv','w') as fh:
    fh.write("mass,acceleration,force")
    fh.write("\n")
    for _ in range(100000):
        mass = randint(0,10)
        acc = randint(0,10)
        force = mass*acc
        fh.write(str(mass))
        fh.write(",")
        fh.write(str(acc))
        fh.write(",")
        fh.write(str(force))
        fh.write("\n")
