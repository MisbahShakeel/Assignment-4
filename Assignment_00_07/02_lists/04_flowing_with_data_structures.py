def add_three_copies(my_list, data):
    for i in range(3):
        my_list.append(data)

def main():
    message = input("\033[1;3m Enter a message to copy: ")
    my_list = []
    print(f"List before: {my_list}")
    add_three_copies(my_list, message)
    print(f"list after: {my_list}")

if __name__ == "__main__":
    main()