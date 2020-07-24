# import the MemeGenerator class from memegen.py
from memegenerator import MemeGenerator
from simpleimage import SimpleImage

def main():
    # initalize the meme generator with an image
    meme_gen = MemeGenerator('X-X-Everywhere.jpg')

    # add text to the top and bottom of the meme
    meme_gen.add_text('for loops', 800, 100, 200)
    meme_gen.add_text('C', 1100, 750, 200)
    meme_gen.add_text('for loops everywhere', 150, 1200, 200)

    # generate the meme!
    meme_gen.render()

if __name__ == '__main__':
    main()