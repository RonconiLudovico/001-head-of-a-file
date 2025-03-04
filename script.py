import sys

def print_head(filename, num_lines=10, verbose=False):
    """Print the first `num_lines` of `filename`. Show filename if `verbose` is True."""
    
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        output = [f"====> {filename} <====\n"] if verbose else []
        output.extend(lines[:num_lines])
        print("".join(output), end="\n" if verbose else "")

    except Exception as e:
        errors = {
            FileNotFoundError: f"head: cannot open '{filename}' for reading: No such file or directory",
            PermissionError: f"head: cannot open '{filename}': Permission denied"
        }
        print(errors.get(type(e), f"head: error reading '{filename}': {e}"), file=sys.stderr)


def parse_args(args):
    """Parse command-line arguments, returning (num_lines, verbose, filenames)."""
    
    num_lines = 10
    verbose = "-v" in args
    args = [arg for arg in args if arg != "-v"]

    try:
        n_index = args.index("-n")
        num_lines = int(args[n_index + 1])
        args = args[:n_index] + args[n_index + 2:]  # Remove "-n" and its value
    except (ValueError, IndexError):
        pass  # If "-n" is not found or invalid, default to 10

    return num_lines, verbose, args


def main():
    
    args = sys.argv[1:]
    num_lines, verbose, filenames = parse_args(args)

    filenames or sys.exit("head: missing file operand")  # Exit if no files provided

    for file in filenames:
        print_head(file, num_lines, verbose or len(filenames) > 1)



if __name__ == "__main__":
    main()