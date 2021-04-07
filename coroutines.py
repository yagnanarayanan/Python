def searcher():
    import time
    book = "This is a book"
    time.sleep(3)

    while True:
        text = (yield)
        if text in book:
            print(":)")
        else:
            print(":(")


search = searcher()
print("Search started")
next(search)
print("Next method run")
search.send("is")
search.send("was")
search.close()
