class Publication:
    def __init__(self,name):
        self.name = name

class Book(Publication):
    def __init__(self,name, author, page):
        Publication.__init__(self,name)
        self.author = author
        self.page = page
    def print_information(self):
        print(f"Book name {self.name}, author {self.author}, page count {self.page}")

class Magazine(Publication):
    def __init__(self,name,chief_editor):
        Publication.__init__(self,name)
        self.chief_editor = chief_editor
    def print_information(self):
        print(f"Magazine name {self.name}, chief editor {self.chief_editor}")


publication_list = [Magazine("krish", "Alex"),Book("Black panther", "lisa", 192)]
publication_list[0].print_information()
publication_list[1].print_information()