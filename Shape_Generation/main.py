# --------------------------------------------------------------------------------------------------------
# Random 3D body generator for input into OpenFoam/ParaView simulations

# Matthew H. Cornfield
# Rhodes University
# 2022
# --------------------------------------------------------------------------------------------------------

import os
import mouse
import time
import datetime
import pyautogui
import random
from os.path import exists
import natsort

# ===========================INSTRUCTIONS=================================================================

# Requires SelfCAD - https://www.selfcad.com/download-for-pc

# 1. use two 1080x1920 monitors
# 2. Open this project (main.py) on the right-hand monitor
# 3. Specify the path to file location for the BodyData.txt file. e.g. "D:\BScHons\DataSet\BodyData"
save_path = "D:\BScHons\DataSet\BodyData"

# 4. Enter the total size of the final dataset that you would like to create. e.g. 24000
#   The generator will not allow the user to create more shapes than this number but be aware that the count starts from 0.
#   Final shape will be entered count -1
tShapes = 24000

# 5. Enter number of shapes to generate for this run. e.g. 1200
#   Some computers stuggle to generate the entire dataset in one run, it is recommended not to run more than 2000 at a time.
gShapes = 1200

# 6. Create a new SelfCAD project in full screen on the left-hand monitor
# 7. Press 'p' and 'c' together to generate a cube, then click the tick in the menu that pops up
# 8. Hold 'Ctrl' and 'e' together, in the 'more' drop down select 'OBJ format without material file' and select 'Make default'
# 9. Navigate to the location that you wish to save the .obj files from the generation and save the cube as "123.obj (This step must be repeated every time a run is completed in a new SelfCAD project)
# 10. Locate the cube saved as '123.obj' and delete it.
# 11. In the SelfCAD project click on the object and press delete and then delete the object
#   This creation and deletion is the only way to tell selfCAD where you would like the files saved.
#   The environment is now configured to run the generator

# 12. Run main.py and do not touch the mouse or keyboard until the generation is complete
# The terminal will output:
#                         - The number of shapes to be generated.
#                         - The estimated time that the run should take.
#                         - The shapes being generated and their properties
#                         - When it is clearing the memory
#                         - When the data is being cleaned (this may take multiple epochs)

# Data Saved:
#           - The shape data will be saved as a textfile in the file location specified by the user
#           - The shape data is in a .txt file that is ready to be converted into .csv format
#           - The .obj files will be saved in the location specified when setting up the SelfCAD project

# 13. Once some shapes have been generated run the 'check()' method to manually check if the data requires cleaning.
# 14. If the 'check()' method produces an output run the 'cleanData()' method to manually force data cleaning.

# ========================================================================================================

tShapes = tShapes - 1

file_name = "BodyData.txt"

# initialize array to store body features
bodyArray = []

# average generation time per shape (seconds)
gen_time = 6.403421149253845


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


# Sets/randomises shape features:
#     Top radius
#     Bottom radius
#     Angle
#     No. of edges
#     Height
# accepts:
#     mouse y-location
#     range for random number generation
def build_shape(locy, minrand, maxrand, ID, val):
    if ID == 1:
        num = int(val)
    else:
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


# --------------------------------------------------------------------------------------------------------


# method to generate number of bodies and body data within specified range
#     Top radius    : 3 - 175
#     Bottom radius : 3 - 175
#     Angle         : 120 - 360
#     No. of edges  : 3, 64
#     Height        : 15, 350
#     Bevel         : -1 - 10
# accepts:
#     No. of shapes to generate
#     Total number of shapes required for the data set
def gen_shape(no, size):
    mouse.move(987, 500, absolute=True)
    time.sleep(2)
    mouse.click(button=mouse.LEFT)
    time.sleep(2)

    exp_time = str(datetime.timedelta(seconds=int(gen_time) * no))

    print(gShapes, " bodies will take roughly: " + exp_time + " to generate")

    sample_size = size
    data_no = check_data()

    print("==================================\n" + "Generating Bodies")
    for x in range(0, no):
        if check_data() != sample_size + 1:
            del_shape(check_data())

            open_gen()

            build_shape(425, 3, 175, 0, 0)
            build_shape(515, 3, 175, 0, 0)
            build_shape(570, 120, 360, 0, 0)
            build_shape(620, 3, 64, 0, 0)
            build_shape(680, 15, 350, 0, 0)
            build_bevel(805, -5, 10)

            export_shape(x + data_no, 0, 0)
            create_file()
            time.sleep(1)
    print("==================================\n")


# Opens shape generator
def open_gen():
    pyautogui.hotkey('g', 's')
    time.sleep(2)


# method for exporting/saving body
# accepts:
#   incremented shape number
def export_shape(inc, ver, ID):
    if ver == 1:
        name = ID
    else:
        name = 'Shape_' + str(inc)
        bodyArray.insert(0, name + ', ')

    mouse.move(274, 241, absolute=True)
    mouse.click(button=mouse.LEFT)

    time.sleep(1)

    pyautogui.hotkey('ctrl', 'e')
    mouse.move(817, 580, absolute=True)
    time.sleep(1)
    mouse.move(820, 580, absolute=True)
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


# --------------------------------------------------------------------------------------------------------

# method for clearing all generated data
def clear_data():
    # change path to the location of the .obj files that are generated by SelfCAD
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

    # change path to the location of the bodydata.txt file
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

# Method for deleting the accumulated shaped and clearing memory for the system
# allows for more shapes to be generated in one run without the system freezing
# accepts:
#       fsize - the amount of shapes generated in a run
def del_shape(fsize):
    if fsize % 100 == 0 and fsize != 0:
        time.sleep(30)
    if fsize % 20 == 0 and fsize != 0:
        print("==================================")
        print("Clearing Memory")
        print("Missing:", missing())
        print("==================================")
        mouse.move(224, 111, absolute=True)
        time.sleep(0.5)
        mouse.move(224, 176, absolute=True)
        mouse.click(button=mouse.LEFT)
        time.sleep(0.5)
        mouse.move(265, 225, absolute=True)
        time.sleep(0.5)
        pyautogui.press('enter')

        time.sleep(3)

        if missing() > 0:
            cleanData()
            bodyArray.clear()
            del_shape(fsize)


# --------------------------------------Data cleaning-----------------------------------------------------

# method that writes names of all bodies that have been generated to a textfile
def getBodies():
    bodies = []

    with open("bodies.txt", "w") as a:
        # change path to the location of the .obj files that are generated by SelfCAD
        for path, subdir, files in os.walk(r'D:\BScHons\DataSet\Bodys'):
            for filename in files:
                f = os.path.join(filename[6:])
                j = f[:-4] + '\n'
                bodies.append(j)
                # a.write(str(f))
        bodies.sort()
        for body in natsort.natsorted(bodies, reverse=False):
            a.write(body)


# method to check if any 3D bodies are missing
def check():
    getBodies()
    # change path to the location of the bodydata.txt file
    bodyData = open('D:\BScHons\DataSet\BodyData\BodyData.txt', 'r')
    data = bodyData.readlines()

    count = 0

    for i in range(len(data)):
        if i > 0:

            dat1 = data[i][6:]
            dat1j = dat1.split(",", 2)
            dat1k = int(dat1j[0])

            dat2 = data[i - 1][6:]
            dat2j = dat2.split(",", 2)
            dat2k = int(dat2[0])
            # print(k)

            if dat1k - dat2k != 1:
                print(dat1k)


# method to check how many 3D bodies are missing if any
def missing():
    getBodies()

    bodies = open('bodies.txt', 'r')
    # change path to the location of the bodydata.txt file
    bodyData = open('D:\BScHons\DataSet\BodyData\BodyData.txt', 'r')

    lines = bodies.readlines()
    data = bodyData.readlines()

    count = 0

    with open("missing.txt", "w") as a:
        for i in range(len(lines) - 1):
            if i == len(data):
                break
            elif (int(lines[i + 1]) - int(lines[i])) > 1:

                count += 1

                mis = data[int(lines[i]) + 1]
                a.write(mis)

    misses = open('missing.txt', 'r')
    miss = misses.readlines()

    return len(miss)


# method to clean data
# sorts through existing bodies and generates any missing bodies
def clean():
    if missing() > 0:
        print("==================================\n" + "Cleaning: " + str(
            missing()) + " Data Points!")

        mouse.move(987, 500, absolute=True)
        time.sleep(2)
        mouse.click(button=mouse.LEFT)
        time.sleep(2)

        exp_time = str(datetime.timedelta(seconds=int(gen_time) * missing()))

        print(str(missing()), " Missing bodies will take roughly: " + exp_time + " to generate")

        misses = open('missing.txt', 'r')
        miss = misses.readlines()

        print("==================================\n" + "Generating Bodies")

        for m in miss:
            # for non-inline data cleaning
            # del_shape(count)

            shape = m.split(",", 9)

            name = shape[0].strip()
            radT = shape[1].strip()
            radB = shape[2].strip()
            angle = shape[3].strip()
            edge = shape[4].strip()
            height = shape[5].strip()
            offset = shape[6].strip()
            level = shape[7].strip()
            weight = shape[8].strip()

            print(name, radT, radB, angle, edge, height, offset, level, weight)

            open_gen()

            build_shape(425, 0, 0, 1, radT)
            build_shape(515, 0, 0, 1, radB)
            build_shape(570, 0, 0, 1, angle)
            build_shape(620, 0, 0, 1, edge)
            build_shape(680, 0, 0, 1, height)
            clean_bevel(805, offset)
            clean_bevel(860, level)
            clean_bevel(895, weight)

            export_shape(0, 1, name)
            time.sleep(1)
        print("==================================\n")


# generates new body bevel data for bodies created while cleaning
def clean_bevel(locy, val):
    if int(val) != 0:
        num = int(val)
        word = str(num)

        mouse.move(280, locy, absolute=True)
        mouse.click(button=mouse.LEFT)
        pyautogui.write(word)
        pyautogui.press('enter')


# checks if data is clean
def cleanData():
    while missing() > 0:
        clean()
        bodyArray.clear()

    else:
        print("==================================\n" + "No Data Missing!\n" + "==================================\n")


# --------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    # run gen-shape methods with a specified number of bodies to create out of the final amount of bodies
    gen_shape(gShapes, tShapes)

    # manually checks if data is clean
    # check()

    # manually force data cleaning
    # cleanData()
