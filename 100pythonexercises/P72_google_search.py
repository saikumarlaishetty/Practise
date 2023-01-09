import webbrowser

query = input("Input your query: ")
webbrowser.open("https://google.com/search?q=%s" % query)