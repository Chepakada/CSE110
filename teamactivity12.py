import linecache
scripture=input(f'Enter the book that you want to read. ').lower()

with open('books_and_chapters.txt') as books_chapters:
    a=0
    count=0
    n=0
    for line in books_chapters:
        clean_line=line.strip()
        parts=clean_line.split(':')
        chapter=parts[0]
        number=int(parts[1])
        book=parts[2].lower()
        if book==scripture:
            if count<=number:
                count=number
                n=a
        a=a+1
        
    

chapt=linecache.getline('books_and_chapters.txt', n+1)
print(chapt)
    
    

        