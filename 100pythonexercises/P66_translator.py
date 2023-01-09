d = dict(weather = "clima", earth = "terra", rain = "chuva")

def vocabulary(word):
    if word in d.keys():
        return d[word]
    return "The word doesnot exist"

word = input("Enter a word")
print(vocabulary(word))

#or

def vocabulary(word):
    try:
        return d[word]
    except KeyError:
        return "The word doesnot exist"

word = input("Enter a word")
print(vocabulary(word))
