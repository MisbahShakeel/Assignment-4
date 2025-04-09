#  Tiny mad lib

sentence_start: str = "Once upon a time, there was a"
sentence_middle: str = "who lived in a"
sentence_end: str = "and they lived happily ever after."

# Get user input for the mad lib

def main():
    adjective: str = input("\033[1;3m Enter an adjective: ")
    noun: str = input("\033[1;3m Enter a noun: ")
    verb: str = input("\033[1;3m Enter a verb: ")

    print(f"{sentence_start} {adjective} {sentence_middle} {noun} {sentence_end} {verb}")

if __name__ == "__main__":
    main()