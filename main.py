# ---------------------------------------------------------------------
# Random 3D body generator for input into OpenFoam/ParaView simulations

# Matthew H. Cornfield
# Rhodes University
# 2022
# ---------------------------------------------------------------------

import os
import mouse
import time
import datetime
import pyautogui
import random
from os.path import exists

# path to file location for the BodyData.txt file "File path----File Name"
save_path = "D:\BScHons\DataSet\BodyData"
file_name = "BodyData.txt"

# initialize array to store body features
bodyArray = []

# average generation time per shape (seconds)
gen_time = 6.403421149253845

# Enter total number of shapes
tShapes = 25000
# Enter shapes to generate
gShapes = 25000


# Checks if previous data exists
# returns the length of existing text file i.e. returns how many shapes have already been generated
def check_data():
    # create file path
    complete_name = os.path.join(save_path, file_name)
    # check if file exists
    file_exists = exists(complete_name)

    # if it exists open file
    # read number of lines in textfile
    # return number of lines
    if file_exists:
        with open(complete_name, 'r') as fp:
            f_size = len(fp.readlines())
        return f_size
    # else return no lines exist in text file (0)
    else:
        return 0


# Opens shape generator
def open_gen():
    pyautogui.hotkey('g', 's')
    time.sleep(1.5)


# Sets/randomises shape features:
#     Top radius
#     Bottom radius
#     Angle
#     No. of edges
#     Height
# accepts:
#     mouse y-location
#     range for random number generation
def build_shape(locy, minrand, maxrand):
    # set a random variable between th specified range per feature
    num = int(random.uniform(minrand, maxrand))
    word = str(num)

    bodyArray.append(str(num) + ', ')

    mouse.move(280, locy, absolute=True)
    mouse.click(button=mouse.LEFT)
    pyautogui.write(word)
    pyautogui.press('enter')


# checks if the shape has a bevel
# adds bevel parameters:
#     Bevel offset
#     Bevel level
#     Bevel weight
# accepts:
#     mouse y-location
#     range for random number generation
def build_bevel(locy, minrand, maxrand):
    num = int(random.uniform(minrand, maxrand))
    word = str(num)

    # add to array
    bodyArray.append(str(num) + ', ')

    mouse.move(280, locy, absolute=True)
    mouse.click(button=mouse.LEFT)
    pyautogui.write(word)
    pyautogui.press('enter')

    # if shape has a bevel -> create bevel parameters
    if word != "0":
        num = int(random.uniform(1, 20))
        word = str(num)

        # add to array
        bodyArray.append(str(num) + ', ')

        mouse.move(280, 860, absolute=True)
        mouse.click(button=mouse.LEFT)
        pyautogui.write(word)
        pyautogui.press('enter')

        num = int(random.uniform(-3, 4))
        word = str(num)

        bodyArray.append(str(num))

        mouse.move(280, 895, absolute=True)
        mouse.click(button=mouse.LEFT)
        pyautogui.write(word)
        pyautogui.press('enter')
    # if no bevel set bevel parameters to zero
    else:
        bodyArray.append('0, ')
        bodyArray.append(0)


# method for exporting/saving body
# accepts:
#   incremented shape number
def export_shape(inc):
    name = 'Shape_' + str(inc)
    bodyArray.insert(0, name + ', ')

    mouse.move(274, 241, absolute=True)
    mouse.click(button=mouse.LEFT)

    time.sleep(0.5)

    pyautogui.hotkey('ctrl', 'e')
    mouse.move(817, 580, absolute=True)
    time.sleep(1)
    mouse.click(button=mouse.LEFT)
    time.sleep(1)
    pyautogui.write(name)
    pyautogui.hotkey('enter')


# method of writing array data of body features to text file for later conversion to CSV data
def create_file():
    complete_name = os.path.join(save_path, file_name)
    f = open(complete_name, "a")
    for j in bodyArray:
        f.write(str(j))
    f.write("\n")
    f.close()

    print(bodyArray)

    bodyArray.clear()


# method to generate number of bodies and body data within specified range
#     Top radius    : 3 - 175
#     Bottom radius : 3 - 175
#     Angle         : 120, 360
#     No. of edges  : 3, 64
#     Height        : 15, 350
#     Bevel         : -1 - 10
# accepts:
#     No. of shapes to generate
#     Total number of shapes required for the data set
def gen_shape(no, size):
    mouse.click(button=mouse.LEFT)

    exp_time = str(datetime.timedelta(seconds=int(gen_time) * no))

    print(gShapes, " bodies will take roughly: " + exp_time + " to generate")

    sample_size = size
    data_no = check_data()

    print("==================================\n" + "Generating Bodies")
    for x in range(0, no):
        if check_data() != sample_size + 1:
            del_shape(check_data())

            open_gen()

            build_shape(425, 3, 175)
            build_shape(515, 3, 175)
            build_shape(570, 120, 360)
            build_shape(620, 3, 64)
            build_shape(680, 15, 350)
            build_bevel(805, -5, 10)

            export_shape(x + data_no)
            create_file()
            time.sleep(0.5)
    print("==================================\n")


# method for clearing all generated data
def clear_data():
    path = r"D:\BScHons\DataSet\Bodys\\"
    print("==================================\n" + "Deleting Bodies")
    for file_n in os.listdir(path):
        # construct full file path
        file = path + file_n
        if os.path.isfile(file):
            print('Deleting file:', file)
            os.remove(file)
        else:
            print('No Bodies Found!')
    print("==================================\n")

    path = r"D:\BScHons\DataSet\BodyData\\"
    print("==================================\n" + "Deleting Data")
    for file_n in os.listdir(path):
        # construct full file path
        file = path + file_n
        if os.path.isfile(file):
            print('Deleting file:', file)
            os.remove(file)
        else:
            print('No Data Found!')
    print("==================================\n")


def del_shape(fsize):
    if fsize % 50 == 0 and fsize != 0:
        print("==================================")
        print("Clearing Memory")
        print("==================================")
        mouse.move(224, 111, absolute=True)
        time.sleep(0.2)
        mouse.move(224, 176, absolute=True)
        mouse.click(button=mouse.LEFT)
        time.sleep(0.2)
        mouse.move(265, 225, absolute=True)
        time.sleep(0.2)
        pyautogui.press('enter')

        time.sleep(3)


if __name__ == '__main__':
    # run gen-shape methods with a specified number of bodies to create out of the final amount of bodies
    gen_shape(gShapes, tShapes)
    # clear_data()
