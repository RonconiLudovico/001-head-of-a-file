import sys

def main():

# Here we created a function in which, depending on the arguments of sys.argv, behaves differently
# Case in which the arguments are only the script name and the file passed to the script
    if len(sys.argv) == 2:
        print_lines(10)

# If there are more than 2 arguments
    elif len(sys.argv) > 2:

# Case in which the second argument is "-n", the number of lines printed should be the third argument
        if sys.argv[1] == "-n":
            num = int(sys.argv[2])
            print_lines(num)

# Case in which the second argument is "-v", the name of the file should be outputted before the lines        
        elif sys.argv[1] == "-v":
            print(f"====> {sys.argv[-1]} <====")

# Case in which we combine the previous 2 cases
            if sys.argv[2] == "-n":
                num = int(sys.argv[3])
                print_lines(num)


def print_lines(num):

# Here we created a function in which the last argument of sys.argv (file name) is opened and printed as many lines as num parameter
    file = sys.argv[-1]
    with open(file, 'r') as file_name:
        lines = file_name.readlines()
        
    for line in lines[:num]:
        print(line)


if __name__ == "__main__":
    main()