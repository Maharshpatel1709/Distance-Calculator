# Distance Calculator
This project is used to compute the distance of a known object from our camera.
## Dependent Packages
* [numpy](https://pypi.python.org/pypi/numpy)
* [OpenCV-Python](http://docs.opencv.org/master/dd/dd5/tutorial_py_setup_in_fedora.html)
## Project Workflow
To accomplish this task we use the following principle:
* **Area enclosed by the contours of an object decreases as the object moves farther from the camera.**
### Step-1
Find the area enclosed by the countour.
```python
cv2.contourArea(contour)
```
### Step-2
1. Calibrate the readings of area with those of manually measured distance.
2. Use these readings to plot a graph.
3. Find the equation of the trendline in excel which fits best with the data.
4. Now finally, use the equation of trendline to calculate the distance.
```python
Distance = 1134.6*((cv2.contourArea(contour))**(-0.497))
```
## Output
<img src="https://github.com/Maharshpatel1709/Distance-Calculator/blob/master/Near_img.png" width="360">
<img src="https://github.com/Maharshpatel1709/Distance-Calculator/blob/master/Far_img.png" width="360">
