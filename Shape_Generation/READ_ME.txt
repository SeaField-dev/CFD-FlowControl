===========================INSTRUCTIONS=================================================================

Requires SelfCAD - https://www.selfcad.com/download-for-pc

1. use two 1080x1920 monitors
2. Open this project (main.py) on the right-hand monitor
3. Read code comments carfully and change file paths where instructed
4. Specify the path to file location for the BodyData.txt file. e.g. "D:\BScHons\DataSet\BodyData"

5. Enter the total size of the final dataset that you would like to create. e.g. 24000
    The generator will not allow the user to create more shapes than this number but be aware that the count starts from 0.
    Final shape will be entered count -1

6. Enter number of shapes to generate for this run. e.g. 1200
   Some computers stuggle to generate the entire dataset in one run, it is recommended not to run more than 2000 at a time.

7. Create a new SelfCAD project in full screen on the left-hand monitor
8. Press 'p' and 'c' together to generate a cube, then click the tick in the menu that pops up
9. Hold 'Ctrl' and 'e' together, in the 'more' drop down select 'OBJ format without material file' and select 'Make default'
10. Navigate to the location that you wish to save the .obj files from the generation and save the cube as "123.obj (This step must be repeated every time a run is completed in a new SelfCAD project)
11. Locate the cube saved as '123.obj' and delete it.
12. In the SelfCAD project click on the object and press delete and then delete the object
    This creation and deletion is the only way to tell selfCAD where you would like the files saved.
    The environment is now configured to run the generator

13. Run main.py and do not touch the mouse or keyboard until the generation is complete
     The terminal will output:
                         - The number of shapes to be generated.
                         - The estimated time that the run should take.
                         - The shapes being generated and their properties
                         - When it is clearing the memory
                         - When the data is being cleaned (this may take multiple epochs)

  Data Saved:
           - The shape data will be saved as a textfile in the file location specified by the user
           - The shape data is in a .txt file that is ready to be converted into .csv format
           - The .obj files will be saved in the location specified when setting up the SelfCAD project

14. Once some shapes have been generated run the 'check()' method to manually check if the data requires cleaning.
15. If the 'check()' method produces an output run the 'cleanData()' method to manually force data cleaning.

========================================================================================================
