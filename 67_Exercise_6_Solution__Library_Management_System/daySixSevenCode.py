class Library:
    def __init__(self):
        self.noBook=0
        self.books=[]
        
        
    def addBook(self,book):
        self.books.append(book)
        self.noBook=len(self.books)
        
        
    def showinfo(self):
        print(f"The library has {self.noBook} books ")
        
        
l1=Library()
l1.addBook("Coding by Munawar")
l1.addBook("Programming Life")
l1.addBook("Coding Knowledge")
l1.addBook("Coding Time")
l1.addBook("Django Framework")
l1.showinfo()