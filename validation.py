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


def is_file_exist(path):
    return os.path.exists(path)


def copy_file(filename, src_path, dst_path):
    os.chdir(src_path)
    content = open(filename, 'r')
    copie = content.read()
    content.close()

    os.chdir(dst_path)
    content = open(filename, 'w')
    content.write(copie)
    content.close()


def get_directory(name):
    return os.path.join(basic_location, name)


def delete_file(filename, path):
    os.chdir(path)
    os.remove(filename)


def display_contents(filename):
    with open(filename, 'r') as contents:
        print("{} is filled with : {}.".format(filename, contents.read()))


while True:

    if is_file_exist(os.path.join(basic_location, "A", test)):
        print("{} exists in Rep A, I'm moving it to Rep B".format(test))
        copy_file(test, get_directory("A"), get_directory("B"))
        display_contents(test)
        delete_file(test, get_directory("A"))

    elif is_file_exist(os.path.join(basic_location, "B", test)):
        print("{} exists in Rep B, I'm moving it to Rep A".format(test))
        copy_file(test, get_directory("B"), get_directory("A"))
        display_contents(test)
        delete_file(test, get_directory("B"))
    else:
        print("{} doesn't exist either in rep A nor B, let's create it in rep A !".format(test))
        input("pause\n")
        os.chdir(os.path.join(basic_location, "A"))
        content = open(test, 'x')
        content.close()
        print("Just created it and closed it straight away with open(x, 'x') & x.close()")
        display_contents(test)
        print("Lets open it again using 'a' to append some text to it with \'ajout\' :)")
        content = open(test, 'a')
        content.write("\nAjout")
        content.close()
        print("Lets check {}'s contents using \'with open...\' :".format(test))
        display_contents(test)
    input("keep going on\n")
