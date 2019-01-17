# Simple Motion Detection
This project is a simple and fun way of motion detection, with an raspberry pi. It can be use as a start into computer vision and IT-security/surveillance.

## Getting Started
Start by downloading this project, either as .ZIP or with through *desktop*.
If downloaded as zip, you should just be able to unzip it and run the demo - *demo.py*

## Instaling
With python 3.x installed, on raspbian, everything should be ready to run.

## Usage
```python
MD.Motion.Check(baseImage, newImage, sentivity, shouldDraw = False
```
Check if there is movement between two images. It uses the baseImage to check what different between the pictures.

Parameters:
* baseImage -  A location to input/base picture, either relative or absolute.
* newImage -  A location to newest picture, either relative or absolute.
* sentivity - A number between 0-255 to determine which pixel to be mark as changed.
* shouldDraw - Tells the program if it should make a copy of the baseImage and draw out the difference. Default is false. If given, this should be a boolean. It can be traumatically turn up "check" time, so keep that in mind.

Returns:	
*url or false* (It can be used as a boolean)

## Build With
* [PIL](http://www.pythonware.com/products/pil/)

## Authors
1. **Rune Harlyk** - *Initial work*

See also the list of contributors who participated in this project.

## License
This project is licensed under the GNU License - see the /LICENSE.md file for details
