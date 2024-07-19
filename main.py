import cv2
import os
import numpy as np
import gzip
import shutil
import time

characters = r"@&%QWNM0gB$#DR8mHXKAUbGOV4d9h6PkqwSE2]ayjxY5Zoen[ult13If}C{iF|(7J)vTLs?z/*cr!+<>;=^,_:'-.` "


def get_brightness(pixel):
    return 0.299 * pixel[2] + 0.587 * pixel[1] + 0.114 * pixel[0]


def getAscii(img, size) -> str:
    print(img.shape)

    img = cv2.resize(img, (256, 144))
    final_ascii = ""
    t = time.time()
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            # print(img[x, y])
            bright = get_brightness(img[x, y])
            final_ascii += characters[int(bright / 255 * len(characters)) - 1]

        final_ascii += "\n"
    print("TIME TO RESIZE:", time.time() - t)
    return final_ascii


def writeAsciiToFile(ascii, filename):
    if not os.path.exists("ascii"):
        os.makedirs("ascii")
    with open("ascii/" + filename, "w") as file:
        file.write(ascii)
    with open("ascii/" + filename, "rb") as f_in:
        with gzip.open("ascii/" + filename + ".gz", "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)


if __name__ == "__main__":
    img = cv2.imread("tree.png")
    ascii = getAscii(img, 256)
    writeAsciiToFile(ascii, "tree.txt")
