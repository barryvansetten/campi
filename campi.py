import os, datetime

class campi:
    """Class for controlling the Pi Camera"""
    def __init__(self):
        #the directory where the pictures are stored
        self.targetDirectory = os.getenv("HOME") + "/Pictures/campi/" + datetime.datetime.now().strftime("%Y%m%dT%H%M%S")

        self.width = 1024
        self.height = 768
        self.prefix = "campi-"
        
        #the number of pictures that were made
        self.pictureCounter = 0

    def filename(self):
        self.pictureCounter+=1
        return self.prefix + str(self.pictureCounter) + ".jpg"
        
    def shoot(self):
        """ Take picture"""

        #if no pictures have been made yet then it is first checked of the target folder exists
        if self.pictureCounter == 0:
            if not os.path.exists(self.targetDirectory):
                os.makedirs(self.targetDirectory)

        

        shootCommand = "raspistill -w " + str(self.width) + " -h " + str(self.height) + " -o " + self.targetDirectory + "/" + self.filename()
        #print(shootCommand)       
        os.system(shootCommand)
        



cam = campi()
cam.shoot()

