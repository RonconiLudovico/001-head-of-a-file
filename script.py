import sys

def main():

    if len(sys.argv) == 2:
        print_lines(10)

    elif len(sys.argv) > 2:

        if sys.argv[1] == "-n":
            num = int(sys.argv[2])
            print_lines(num)
        
        elif sys.argv[1] == "-v":
            print(f"====> {sys.argv[-1]} <====")

            if sys.argv[2] == "-n":
                num = int(sys.argv[3])
                print_lines(num)
            
            else:
                print_lines(10)


def print_lines(num):

    file = sys.argv[-1]
    with open(file, 'r') as file_name:
        lines = file_name.readlines()
        
    for line in lines[:num]:
        print(line)


if __name__ == "__main__":
    main()