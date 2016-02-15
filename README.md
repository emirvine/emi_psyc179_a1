This repository contains the code relevant for PSYC 179 Assignment 1.

Here, I implemented the loading and analyses of neural data to determine tuning curves of dorsal hippocampus CA1 neurons' firing rate by rat position.

I used a Python notebook (Jupyter) with Python 2.7. Github renders the evaluations of each of these code cells, so it should be possible for you to see the output of the code. Click on the tuning_curves.ipynb file to view this notebook. If you want to run this code yourself, follow these instructions:

- In Matlab (I used R2013b), run the loading_data.m script which loads the data from the Neuralynx files. To run this script you will have to specify the file path to R063-2015-03-20_recording on your computer. Ensure that the *.mat files produced from this script are saved in the same file where you have located the tuning_curves.ipynb. This will enable the notebook to have those files in its path when running the notebook and loading the data!

- Download a working version of Python 2.7. I recommend using the Anaconda distribution (https://www.continuum.io/downloads) which also includes a number of scientific packages that we use in the analyses. 

- Ensure you have installed all the dependencies, which are imported in the first cell block. This includes Shapely (https://pypi.python.org/pypi/Shapely), which isn't in the Anaconda distribution. 

- Run the Jupyter notebook from a terminal (command prompt), which will open it in a browser. Run all cells and/or any particular cell of interest from there!

Let me know if any of this is unclear! 

Finally, for comparison purposes, I have implemented this analysis in Matlab in tuning_curves_compare.m. This script requires a number of functions, mainly in the neuraldata-w16 codebase, but some included in the folder matlab_tc_req which should also be in your path when you run the matlab script.