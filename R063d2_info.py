from shortcut_general import *
import os

# Load the data
# os.chdir('C:\Users\Emily\Desktop\R063-2015-03-20_recording')
csc = load_csc('C:\\Users\\Emily\\Desktop\\R063-2015-03-20_recording\\emi_inputs_csc.mat')
pos = load_videotrack('C:\\Users\\Emily\\Code\\Shortcut\\analysis\\positions\\R063-2015-03-20-vt.mat')
events = load_events('C:\\Users\\Emily\\Desktop\\R063-2015-03-20_recording\\emi_inputs_event.mat')
spikes = load_spikes('C:\\Users\\Emily\\Desktop\\R063-2015-03-20_recording\\emi_inputs_spike.mat')

# Experimental session-specific task times for R063 day 2
task_times = dict()
task_times['prerecord'] = [721.9412, 1027.1]
task_times['phase1'] = [1075.8, 1569.6]
task_times['pauseA'] = [1593.9, 2219.0]
task_times['phase2'] = [2243.4, 3512.4]
task_times['pauseB'] = [3556.1, 5441.3]
task_times['phase3'] = [5469.7, 8794.6]
task_times['postrecord'] = [8812.7, 9143.4]

pxl_to_cm = (8.8346, 7.1628)

fs = 2000

good_lfp = ['R063-2015-03-20-CSC13d.ncs']

# Session-specific path trajectory points
path_pts = dict()
path_pts['feeder1'] = [468, 471]
path_pts['point1'] = [466, 397]
path_pts['turn1'] = [465, 380]
path_pts['point2'] = [445, 380]
path_pts['point3'] = [298, 398]
path_pts['point4'] = [173, 367]
path_pts['turn2'] = [148, 359]
path_pts['point5'] = [138, 319]
path_pts['point6'] = [140, 103]
path_pts['turn3'] = [155, 69]
path_pts['point7'] = [203, 58]
path_pts['feeder2'] = [661, 54]
path_pts['shortcut1'] = [467, 378]
path_pts['point8'] = [466, 195]
path_pts['point9'] = [496, 166]
path_pts['point10'] = [645, 164]
path_pts['point11'] = [669, 162]
path_pts['point12'] = [672, 146]
path_pts['shortcut2'] = [661, 55]
path_pts['novel1'] = [146, 359]
path_pts['novel2'] = [49, 351]

path_pts = convert_to_cm(path_pts, pxl_to_cm)

u_trajectory = [path_pts['feeder1'], path_pts['point1'], path_pts['turn1'],
                path_pts['point2'], path_pts['point3'], path_pts['point4'],
                path_pts['turn2'], path_pts['point5'], path_pts['point6'],
                path_pts['turn3'], path_pts['point7'], path_pts['feeder2']]

shortcut_trajectory = [path_pts['shortcut1'], path_pts['point8'], path_pts['point9'],
                       path_pts['point10'], path_pts['point11'], path_pts['point12'],
                       path_pts['shortcut2']]

novel_trajectory = [path_pts['novel1'], path_pts['novel2']]


