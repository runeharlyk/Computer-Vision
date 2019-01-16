import CE
from time import sleep

E = CE.Extraction()

RedExtraction = E.Extract("test.jpg", "demo.jpg",  0, 100)
if RedExtraction:
	print("Color extration went successfully! You can find you picture here:")
	print(RedExtraction)
