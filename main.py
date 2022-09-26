from termcolor import colored


def main():
    color_dict = {0: "red", 1: "yellow", 2: "green", 3: "blue", 4: "magenta", 5: "cyan"}
    
    for index, value in enumerate("Hello world!"):
        print(colored(value, color_dict[index%6]), end="")

    
if __name__ == "__main__":
    main()