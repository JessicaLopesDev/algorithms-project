def is_palindrome_iterative(word):
    if word == "":
        return False

    reversedWord = "".join(reversed(word))

    return reversedWord == word
