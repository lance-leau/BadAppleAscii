import cv2
import sys

resolution = 1
if len(sys.argv) != 1:
    resolution = (int)(sys.argv[1])

def ascii(img):
    ret = ""
    i = 0
    while i < 360:
        row = ""
        j = 0
        while j < 480:
            (r, g, b) = img[i, j]
            pixel = (0.3*r + 0.59*g + 0.11*b)
            temp = grayRamp[int(rampLength * pixel / 255)]
            row += temp + temp
            j += resolution
        ret += row + "\n"
        i += resolution
    return ret

grayRamp = " -=+*##%@@@@@@@@@@@@@@@@@@@@@@@"
rampLength = len(grayRamp) - 1

vidcap = cv2.VideoCapture('./BadApple.mp4')
success,image = vidcap.read()
count = 0
while success:  
    success, img = vidcap.read()
    print(ascii(img))
    c = cv2.waitKey(1)
    if c == 27:# exit on ESC
        break
  
    count += 1
    


vidcap.release()
cv2.destroyAllWindows()