class Text():

    def __init__(self, document):

        self.font_type = 'Arial'
        self.document = document
    
    def write(self, text):
        self.document += text

    def set_font(self, font_type ):
        self.font_type = font_type


    
    def display_text(self):
        print(self.document)

    
class SavedText():

    all_texts = []

    def __init__(self):
        pass
    
    def save_text(self, text):
        self.all_texts.append(text)
    
    def get_version(self, version):
        print(self.all_texts[version])

text = Text('')
save = SavedText()

text.write('This is the first text')
save.save_text(text.document)

text.write(' and the second time addind to the same text')
save.save_text(text.document)

text.set_font('Sans')




print("version 0 : " ,end='')
save.get_version(0)

print('version 1 : ' , end='')
save.get_version(1)

print('font : ' ,end='')
print(text.font_type)


