from PIL import Image
import os.path

class Extraction:
	def __init__(self):
		self.sentivity = 50
		self.pictureWidth = 400
		self.pictureHeight = 300
		self.DrawingImage = False
		self.noiseReduction = 30

	def Extract(self, inputPicture, outputpicture, feature, sentivity, noiseReduction = 30):

		if not os.path.isfile(inputPicture):
			raise "Base image do not seem to exits"
			exit()

		self.inputPicture = Image.open(inputPicture)
		self.pictureWidth, self.pictureHeight = self.inputPicture.size
		self.inputPicture = self.inputPicture.load()

		self.DrawingImage = Image.new("1", (self.pictureWidth, self.pictureHeight))
		self.DrawingImage_PixelAccess = self.DrawingImage.load()

		self.feature = feature
		self.sentivity = sentivity
		self.outputPicture = outputpicture
		self.noiseReduction = noiseReduction
		for W in range(self.pictureWidth):
			for H in range(self.pictureHeight):
				if self.inputPicture[W, H][self.feature] > self.sentivity and abs(self.inputPicture[W, H][self.feature]- self.inputPicture[W, H][self.feature+1] > self.noiseReduction):
					self.DrawingImage_PixelAccess [W, H] = (255)
				else:
					self.DrawingImage_PixelAccess [W, H] = (0)

		del self.inputPicture
		self.DrawingImage.save(self.outputPicture)
		return self.outputPicture

if __name__ == "__main__":
	E = Extraction()
	RedExtraction = E.Extract("test.jpg", "demo.jpg",  0, 100)
	if RedExtraction:
		print("Color extration went successfully! You can find you picture here:")
		print(RedExtraction)
