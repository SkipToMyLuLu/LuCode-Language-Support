import sys

def interpret_lucode(filename):
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("PRINT "):
                # Extract and print quoted string
                to_print = line[6:].strip().strip('"')
                print(to_print)
            elif line.startswith("ADD "):
                parts = line[4:].split()
                if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                    result = int(parts[0]) + int(parts[1])
                    print(f"Result: {result}")
                else:
                    print("ADD command error.")
            elif line == "":
                continue
            else:
                print(f"Unknown command: {line}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python lucode_interpreter.py <filename.lucode>")
    else:
        interpret_lucode(sys.argv[1])