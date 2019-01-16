from PIL import Image
import warnings
import os.path

class Motion:
    def __init__(self):
        self.sentivity = 50
        self.pictureWidth = 400
        self.pictureHeight = 300
        self.changes = 0
        self.motion = False
        self.preview_image = False
        warnings.simplefilter('always', DeprecationWarning)

    def Check(self, baseImage, newImage, sentivity, shouldDraw = False):
        
        self.motion = False
        
        if not os.path.isfile(baseImage):
            raise "Base image do not seem to exits"
            exit()
        if not os.path.isfile(newImage):
            raise "New image do not seem to exits"
            exit()
        
        self.baseImage = Image.open(baseImage)
        self.pictureWidth, self.pictureHeight = self.baseImage.size

        self.newImage = Image.open(newImage)
        tempSize = self.newImage.size

        # capture errors early on
        if (self.pictureWidth, self.pictureHeight) != tempSize:
            raise "Base picture and the new picture must share dimension"
            exit()
        if self.pictureWidth > 400:
            warnings.warn("Base image and the new image are to big for feasible motion detection. They are being resized now")
            self.resize()

        self.sentivity = sentivity
        self.shouldDraw = shouldDraw
        if self.shouldDraw:
            self.preview_image = tempImg
            self.preview_image_pixelAccess = self.preview_image.load()
        self.baseImage = self.baseImage.convert("LA").load()
        self.newImage = self.newImage.convert("LA").load()
        for W in range(self.pictureWidth):
            for H in range(self.pictureHeight):
                if abs(self.baseImage[W, H][0] - self.newImage[W, H][0]) > 35:
                    self.changes += 1
                    # if self.shouldDraw:
                    #     self.preview_image_pixelAccess[W, H] = (255, 0, 0)
                    if not self.shouldDraw and self.changes > 25:
                        self.motion = True
                        break
                    elif self.shouldDraw:
                        self.preview_image.save("camstatus.jpg")
                        del self.preview_image
        del baseImage
        del newImage

        return self.motion
    def resize(self):
        ratio = self.pictureWidth / 400
        self.baseImage.resize((400, int(self.pictureHeight/ratio)), Image.ANTIALIAS)
        self.newImage.resize((400, int(self.pictureHeight/ratio)), Image.ANTIALIAS)
