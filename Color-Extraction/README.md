# Color Extraction
This project is a way, my way, into computer vision. It can be use to isolate objects in an image.

## Getting Started
Start by downloading this project, either as .ZIP or with through *desktop*.
If downloaded as zip, you should just be able to unzip it and run the demo - *demo.py*

## Instaling
With python 3.x installed everything should be ready to run.

## Usage
```python
CE.Extraction.Extract(input-picture, output-picture, feature, sentivity, noiseReduction=30)
```
Extracts color-feature from input-picture and draw them on output-picture using given sentivity and noiseReduction.

Parameters:
* input-picture -  A location to input/base picture, either relative or absolute.
* output-picture -  A free location to write the extracted color channel to.
* feature - A number representing a color channel in rgb. Eg. 0=red. 
* sentivity - A number between 1-255 to determing which pixel to extract to input-picture.
* noiseReduction - How much information to throw away. Default is 30. If given, this should be a single integer or floating point value between 0-255.

Returns:	
*Url to ouput image*

## Example
![input-picture](https://github.com/runeharlyk/Computer-Vision/blob/master/Color-Extraction/test.jpg)
![output-picture](https://github.com/runeharlyk/Computer-Vision/blob/master/Color-Extraction/demo.jpg)


## Build With
* [PIL](http://www.pythonware.com/products/pil/)

## Authors
1. **Rune Harlyk** - *Initial work*

See also the list of contributors who participated in this project.

## License
This project is licensed under the GNU License - see the /LICENSE.md file for details
