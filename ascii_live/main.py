import cv2
import numpy as np

ascii_chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,^`'. "

def attribute(value):
    value = max(0, min(255, value))
    index = int((value / 255) * (len(ascii_chars) - 1))
    return ascii_chars[index]


def image_to_terminal():
    image = cv2.imread("james.png")
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height, width = grayscale_image.shape
    for j in range(0, height, 10):
        line = ""
        for i in range(0, width, 10):
            char_image = attribute(grayscale_image[j, i])
            line += char_image
        print(line)

def video_capture():

    capture = cv2.VideoCapture(0)

    while True:
        ret, frame = capture.read()
        frame = cv2.flip(frame, 1)

        if not ret:
            print("not able to grab frame")
            break

        grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        height, width = grayscale.shape
        ascii_frame = np.zeros_like(frame)

        for j in range(0, height, 10):
            for i in range(0, width, 10):
                char = attribute(grayscale[j, i])
                cv2.putText(ascii_frame, char, (i, j), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), 1)

        cv2.imshow("frame og", frame)
        cv2.imshow("ascii", ascii_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()

user_input = input("1 or 2\n")
if user_input == '1':
    video_capture()
elif user_input == '2':
    image_to_terminal()
