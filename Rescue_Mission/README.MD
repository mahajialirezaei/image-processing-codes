# Noorcity — `calculate_area.py`

## Overview

A programming exercise that simulates a digital city called **Noorcity** where colored rectangular and square blocks remain after a color-destroying virus. Your task is to analyze an input image (BGR color image read with OpenCV) and compute the (pixel) area of the remaining shapes grouped by color.

Rectangles are considered damaged and their area **must be multiplied by 3**. Squares are less damaged — their area is used unchanged. You must return the sum of (possibly adjusted) areas for each color in a specific textual format.

## Colors and ordering

If present in the image, the final output must contain colors in this exact left-to-right order:

1. `red`
2. `green`
3. `blue`
4. `yellow`
5. `purple` (magenta)
6. `gray`

If a color does not appear in the image, it must be omitted from the output string. If the image contains no colored shapes at all (only black background), output the color `black` along with the total number of pixels in the image.

## Input / Output

* **Input**: a BGR image (already loaded by the caller using `cv2.imread(...)`) that contains non-overlapping (or possibly touching) colored rectangles and squares on a black background.
* **Output**: a single string with lines of `"Color, Area"`, one color per line, in the order listed above. Example:

```
green, 4900
blue, 36700
gray, 38500
```

Notes:

* Areas are integer pixel counts.
* Use contour-based methods (e.g. `cv2.findContours` and `cv2.contourArea`) as required by the exercise — avoid naive pixel-counting as primary method (it may lead to inconsistencies with OpenCV default behaviors).

## Function signature (required)

Implement the following function in a file called `calculate_area.py`:

```python
# calculate_area.py

def calculate_area(image) -> str:
    """
    image: BGR image as read by OpenCV (numpy array)
    returns: formatted string as described in the README
    """
```

## Detection strategy (recommended)

1. **Preprocess**

   * The background is known to be black (`B=0,G=0,R=0`). You can remove background quickly by thresholding or masking out zero pixels.
   * Use a small morphological open/close to remove specks or fill tiny holes.

2. **Per-color masking**

   * For robust detection use color ranges (BGR or, preferably, convert to HSV/Lab and use `cv2.inRange`).
   * Example colors to detect (tune thresholds as needed):

     * Red: two HSV ranges (low and high hue wrap)
     * Green: single HSV range around 60° hue
     * Blue: single HSV range around 120° hue
     * Yellow: single HSV range around 30° hue
     * Purple (magenta): single HSV range around 300°/330° hue
     * Gray: pixels where `|B-G|`, `|B-R|`, `|G-R|` are small and intensity is within a mid-range (to exclude black/white)

3. **Contours & shape classification**

   * For each color mask run `cv2.findContours(..., cv2.RETR_EXTERNAL, ...)`.
   * For each contour, compute `area = cv2.contourArea(cnt)`.
   * Approximate the contour polygon with `cv2.approxPolyDP(cnt, eps, True)` and/or use `cv2.boundingRect(cnt)` to determine if the contour is a quadrilateral.
   * To distinguish between **square** and **rectangle**:

     * Use the bounding rectangle `(x, y, w, h)` and check if `w` and `h` are close (e.g. `abs(w-h) <= tol`) AND the approximation has 4 vertices. Choose a tolerance `tol` relative to size, for example `tol = max(1, round(0.03 * max(w, h)))` (3% of size). If condition passes => square; otherwise rectangle.

4. **Area adjustment & accumulation**

   * If the shape is a rectangle (not a square), use `adjusted_area = area * 3`.
   * If the shape is a square, `adjusted_area = area`.
   * Sum adjusted areas per color.

5. **Output formatting**

   * Create ordered lines for colors that have non-zero total. Each line: `"{color_name}, {total_area}"`.
   * If every color has zero total, return `"black, {total_pixels}"` where `total_pixels = image.shape[0] * image.shape[1]`.

## Implementation tips & caveats

* **Contour area vs. bounding box area**: use `cv2.contourArea` for the true pixel area of the shape (as required by the problem). Don’t rely solely on counting mask pixels (the problem suggests using contours to avoid OpenCV default aliasing issues).

* **Gray detection**: don't confuse black or white with gray. Use an intensity range to exclude near-black and near-white pixels.

* **Noise**: ignore very small contours (area less than a threshold, e.g. `min_area = 50` pixels) to avoid counting noise.

* **Overlapping / touching shapes**: the problem statement implies shapes are distinct; if they touch or overlap, contour separation may require additional processing (watershed, distance transform). For typical generated test images this is unlikely.

## Example usage

```python
import cv2
from calculate_area import calculate_area

img = cv2.imread('new1.png')
result = calculate_area(img)
print(result)
```

## Example test case (expected behavior)

* If `new1.png` contains a green square of area `4900`, a blue rectangle of area `36700` and a gray rectangle of area `12833` (after contour area measurement), the gray rectangle would be multiplied by 3 and summed accordingly. The output should list the colors present (in the correct order) with their adjusted summed areas.
