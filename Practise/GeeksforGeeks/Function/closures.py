# Nested functions
# A Closure is a function object that remembers values in
# enclosing scopes even if they are not present in memory.
def o(text):
    text = text

    def i():
        print(text)

    return i


if __name__ == '__main__':
    myf = o('Hey!')
    myf()
