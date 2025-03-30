# Simple is better than complex

def reverse_string(string):
    if len(string) == 1:
        return string
    else:
        return reverse_string(string[:1]) + string[0]

if __name__ == "__main__":

    string = "barbara"

    print(reverse_string(string))

    """
    arabrab
    """
