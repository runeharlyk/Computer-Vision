# Color Extraction

## Getting Started

## Prerequisites

## Instaling

## Usage
```python
CE.Extraction.Extract(input-picture, output-picture, feature, sentivity, noiseReduction=30)
```
Extracts color-feature from input-picture and draw them on output-picture using given sentivity and noiseReduction.

Parameters:
input-picture -  A location to input/base picture, either relative or absolute.
output-picture -  A free location to write the extracted color channel to
feature - A number representing a color channel in rgb. Eg. 0=red 
sentivity - A number between 1-255 to determing which pixel to extra input-picture
noiseReduction - How much information to throw away. Default is 30. If given, this should be a single integer or floating point value between 0-255.
Returns:	
Url to ouput image

Build With
*PIL
