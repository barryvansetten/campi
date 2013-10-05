import os
import datetime


class Campi:
    """Class for controlling the Pi Camera"""

    def __init__(self):
        #the directory where the pictures are stored
        self.__target_directory = (os.getenv("HOME") + "/Pictures/campi/"
        + datetime.datetime.now().strftime("%Y%m%dT%H%M%S"))

        self.width = 1024
        self.height = 768

        #the prefix of the file name
        self.__prefix = "campi-"
        
        #the number of pictures that were made
        self.__picture_counter = 0

    def __generate_filename(self):
        self.__picture_counter+=1
        return self.__prefix + str(self.__picture_counter) + ".jpg"
        
    def shoot(self):
        """ Take picture"""
        #if no pictures have been made yet then it is first checked of the target folder exists
        if self.__picture_counter == 0:
            if not os.path.exists(self.__target_directory):
                os.makedirs(self.__target_directory)

        #generate the raspistill command for taking the pictures
        shootCommand = ("raspistill -w " + str(self.width) + " -h " +
        str(self.height) + " -o " + self.__target_directory +
        "/" + self.__generate_filename())

        #take the pictures
        print(shootCommand)       
        #os.system(shootCommand)
        



cam = Campi()
cam.shoot()


