from simpleimage import SimpleImage

FONT_FILE = 'Helvetica.ttc'
SIZE = 30  # Set a size ranging from 1-120, beyond that it exceeds from image
COLOR = 'black'  # Colours = Red, white, green, black, blue.


# For custom colours use:- color='rgb(0, 0, 0)'

class MemeGenerator:
    # Initialize the important variables i.e. tex and filename
    def __init__(self, filename):
        # it's basically the constructor which initializes the meme's image,
        # and accepts as a parameter the filename of the image
        self.tex = []
        self.filename = filename

    # We never called this method but it can be used to updTate the image during runtime
    def set_image(self, filename):
        self.filename = filename

    # We called 'add_text' in 'memegen_test.py' twice to pass values
    # Passed values are 'Custom text', x-coordinate of the text and y-coordinate of the text
    def add_text(self, text, x, y, font_size):
        self.tex.append((text, x, y, font_size))
        # The string stored in tex is placed at position (x, y) on the meme.

    def render(self):
        img = SimpleImage(self.filename)
        for text, x, y, size in self.tex:
            img.create_text(text, x, y, FONT_FILE, size=size, color=COLOR)
        img.show()
        img.pil_image.save('F-F-Everywhere.jpg')
