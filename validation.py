import os.path


basic_location = (os.path.abspath('.'))
print("\nFYI : All work will be done within the current repertory which is : {} .\n".format(basic_location))
test = "text.txt"

print("First of all, lets create some reps for file moving purposes : rep A & B\n"
      "and remove any existing {} file in them.".format(test))

try:
    os.remove(os.path.join(basic_location, "A", test))
    os.remove(os.path.join(basic_location, "B", test))
except:
    pass

input("pause\n\n")


try:
    os.mkdir("A")
    os.mkdir("B")
except:
    pass

while True:

    if os.path.exists(os.path.join(basic_location, "A", test)):
        print("{} exists in Rep A, I'm moving it to Rep B".format(test))
        os.chdir(os.path.join(basic_location, "A"))
        content = open(test, 'r')
        copie = content.read()
        content.close()
        os.chdir(os.path.join(basic_location, "B"))
        content = open(test, 'w')
        content.write(copie)
        content.close()
        with open(test, 'r') as contents:
            print("{} is filled with : {}.".format(test, contents.read()))
        os.chdir(os.path.join(basic_location, "A"))
        os.remove(test)
    elif os.path.exists(os.path.join(basic_location, "B", test)):
        print("{} exists in Rep B, I'm moving it to Rep A".format(test))
        os.chdir(os.path.join(basic_location, "B"))
        content = open(test, 'r')
        copie = content.read()
        content.close()
        os.chdir(os.path.join(basic_location, "A"))
        content = open(test, 'w')
        content.write(copie)
        content.close()
        with open(test, 'r') as contents:
            print("{} is filled with : {}.".format(test, contents.read()))
        os.chdir(os.path.join(basic_location, "B"))
        os.remove(test)
    else:
        print("{} doesn't exist either in rep A nor B, let's create it in rep A !".format(test))
        input("pause\n")
        os.chdir(os.path.join(basic_location, "A"))
        content = open(test, 'x')
        content.close()
        print("Just created it and closed it straight away with open(x, 'x') & x.close()")
        with open(test, 'r') as contents:
            print("{} is filled with : {}.".format(test, contents.read()))
        print("Lets open it again using 'a' to append some text to it with \'ajout\' :)")
        content = open(test, 'a')
        content.write("\nAjout")
        content.close()
        print("Lets check {}'s contents using \'with open...\' :".format(test))
        with open(test, 'r') as contents:
            print("{} is filled with : {}.".format(test, contents.read()))
    input("recommencer\n")
