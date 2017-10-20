def getbook(bookname):
    try:
        fin = open(bookname, 'r')
        line = fin.read()
    except:
        print("Something Went wrong while reading")

    word = line.strip(' ')
    mk = word.split()
    d=[]
    for c in mk:
        d.append(len(c))
        e = max(d) 
    for b in mk:
        if len(b) == e:
            return b

book1_long_word=getbook("Book1.txt")
book2_long_word=getbook("Book2.txt")
book3_long_word=getbook("Book3.txt")

print("The longest word in Book1 is :",book1_long_word)
print("The longest word in Book2 is :",book2_long_word)
print("The longest word in Book3 is :",book3_long_word)

