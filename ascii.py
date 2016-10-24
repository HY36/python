from PIL import Image

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_char(r, b, g, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126*r+0.7152*g+0.0722*b)

    unit  = (256.0+1)/length

    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    im = Image.open(input('please input:'))
    w,h = im.size

    txt = " "
    for i in range(h):
        for j in range(w):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'
    with open("output.txt",'w') as f:
        f.write(txt)