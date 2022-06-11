# User Friendly Translator

d = dict(weather = "clima", earth = "terra", rain = "chuva")

def vocabulary(word):
    if word in d.keys():
        return d[word]
    return "We could not find the word "


word = input("Enter word :").lower()
print(vocabulary(word))


