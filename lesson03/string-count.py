text=input("give me the string:")
search=input("query letters:")
text=text.lower().strip()
n=text.count(search.lower())

print(f"The text:{text} contain key words:{search} total:{n}")

