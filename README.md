# SAR Ship Detection

This project was developped by Liam Loughman & Tristan Donzé.
Using the research paper "Optimal Target Detection Using One Channel SAR Complex Imagery" by Armand Lopès, Jérôme Bruniquel, Franck Sery, Jean-Claude Souyris, and Frédéric Adragna, the project focuses on detecting ships in Sentinel-1 SAR imagery using statistical methods.
By implementing a combination of Statistical Whitening Filter (SWF) and Likelihood Ratio Test (LRT), followed by radiometric thresholding and morphological operations, we developed a robust non-learning approach for maritime vessel detection. Our methodology was applied to images from the Strait of Malacca.

---

## Data

The original data was downloaded from the [Copernicus Browser](https://browser.dataspace.copernicus.eu). You can find it by searching for `S1A_IW_SLC__1SDV_20241228T113437_20241228T113505_057192_070894_70FE` in the search bar.

To understand how the images were preprocessed, please refer to the notebook.

The preprocessed images can be downloaded from [here](https://www.icloud.com/iclouddrive/032K1jARLtETKiQylxUk3x2rA#S1A%5FIW1%5FSLC%5FCal%5Fvv%5Fintensity%5FVV%5FIW1) (first image) and [here](https://www.icloud.com/iclouddrive/063xa-i5fq8jPyNtceDQST15A#S1A%5FIW1%5FSLC%5FCal%5Fvv%5Fintensity%5FVV%5FIW2) (second image):

---

## Packages

Make sure you have the following packages installed before running the notebook:

```
numpy
matplotlib
scipy
skimage
shapely
```

---

The image file sizes are big (1.12 GB and 1.49 GB). The notebook might take some time to run. It was run and tested on a MacBook Pro M3 Pro.
