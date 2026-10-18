# nanoplot-tokupic

Load and analyze DICOM images and videos recorded from TOKUPIC in the NanoPLoT setup.

## Installation

```console
pip install git+https://github.com/Weber-Microscopy-Group/nanoplot-tokupic.git
```

## Example

```python
import matplotlib.pyplot as plt
import nanoplot_tokupic as toku

vid = toku.load("video.dcm")
print("Number of frames: {vid.frames}")
print("Number of rows: {vid.rows}")
print("Number of cols: {vid.cols}")
plt.imshow(vid.data[0])
```

## License

`nanoplot-tokupic` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
