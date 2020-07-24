# import the MemeGenerator class from memegen.py
from memegenerator import MemeGenerator
from simpleimage import SimpleImage

def main():
    # initalize the meme generator with an image
    meme_gen = MemeGenerator('IsThisAPigeon?.jpg')

    # add text to the top and bottom of the meme
    meme_gen.add_text('ME DURING CS50', 200, 100)
    meme_gen.add_text('MULTIPLE NESTED', 700, 50)
    meme_gen.add_text('FOR LOOPS', 775, 250)
    meme_gen.add_text('IS THIS A FUNCTION?', 400, 600)

    # generate the meme!
    meme_gen.render()

if __name__ == '__main__':
    main()