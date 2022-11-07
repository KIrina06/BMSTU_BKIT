import emoji
from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square


def main():

    r = Rectangle("синего", 10, 10)
    c = Circle("зеленого", 10)
    s = Square("красного", 10)
    print(r)
    print(c)
    print(s)
    print(emoji.emojize(':blue_square:'), emoji.emojize(':green_circle:'),
          emoji.emojize(':red_square:'))
    print(emoji.emojize(':beaming_face_with_smiling_eyes:'), emoji.emojize(':thumbs_up:'),
          emoji.emojize(':face_savoring_food:'))


if __name__ == '__main__':
    main()
