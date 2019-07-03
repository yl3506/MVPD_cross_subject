# compare different length of training data
# visualization of mean variance explained raw (cross-within) subject
import os
import numpy as np
import matplotlib.pyplot as plt
import itertools as it
import scipy.stats as stats

# initialize parameters
# work_dir = '/gsfs0/data/anzellos/data/forrest/half_output_global_compcorr_pc3_v3/'
# work_dir2 = '/gsfs0/data/anzellos/data/forrest/half_output_nodenoise_pc3_v3/'
work_dir = '/Users/chloe/Documents/Yichen/output_global_compcorr_pc3_v3/'
work_dir2 = '/Users/chloe/Documents/Yichen/output_nondenoise_pc3_v3/'
all_subjects = ['sub-01', 'sub-02', 'sub-04', 'sub-05', 'sub-09', 'sub-15', 'sub-16', 'sub-17', 'sub-18', 'sub-19', 'sub-20']
all_masks = ['rOFA', 'rFFA', 'rATL', 'rSTS', 'rTOS', 'rPPA', 'rPC']



data = []
nodenoise = []
# iterate through all combinations of cross subjects 
for sub_1_index in range(0, len(all_subjects)):
	for sub_2_index in range(0, len(all_subjects)):
		# initialize info
		sub_1 = all_subjects[sub_1_index]
		sub_2 = all_subjects[sub_2_index]
		sub_dir = work_dir + sub_1 + '_to_' + sub_2 + '/'
		sub_dir2 = work_dir2 + sub_1 + '_to_' + sub_2 + '/'
		data_dir = sub_dir + sub_1 + '_to_' + sub_2 + '_raw_ratio_chart.npy'
		data_dir2 = sub_dir2 + sub_1 + '_to_' + sub_2 + '_raw_ratio_chart.npy'
		# load data
		data.append(np.mean(np.load(data_dir)))
		nodenoise.append(np.mean(np.load(data_dir2)))

diff = np.array(data) - np.array(nodenoise)

print(diff)
print(len(diff))


# 8 runs
diff1 = [-0.02277437,0.00370572,0.01449781,0.01054122,0.01871699,0.00525123,\
0.00148093,0.02167774,0.01563588,0.00266991,-0.01234999,0.00085117,\
-0.0215769,0.03130881,0.02392501,0.03111861,0.00853914,0.02187091,\
0.03402852,0.02711055,0.00553522,0.01872352,0.02246251,0.03307025,\
-0.06121679,0.01708223,0.03150001,0.01337766,0.02706165,0.02159221,\
0.01359276,0.02296043,0.01186209,0.01029407,0.01818043,0.00552926,\
-0.09071198,0.01492219,0.00727319,0.01633437,0.00815913,0.0067952,\
0.00626744,-0.0104947,0.01460332,0.02766072,0.02364634,0.01326516,\
-0.0319276,0.01743333,0.01849133,0.02928049,0.01756434,0.00964911,\
0.00970606,0.01214677,0.00940538,0.01477068,0.00901299,0.02897679,\
-0.04341886,0.01939908,0.01232947,0.01362894,0.01689729,-0.00720342,\
-0.00088399,0.0118358,0.01553429,0.01286975,0.01986348,0.01473189,\
-0.06416713,0.01900888,0.01229997,0.00927283,0.00441289,0.01974571,\
0.02756175,0.01018268,0.00745827,0.0321535,0.01195428,0.02389353,\
-0.26977856,0.00584568,0.00065887,0.01231406,0.01709094,0.02503317,\
0.01095275,0.01643561,0.02401067,0.01301126,0.02022586,0.00949549,\
-0.03728377,0.00501051,0.00255806,-0.00113895,-0.00137522,0.01930971,\
0.00688447,0.01358621,0.01246036,0.00878021,-0.0092563,0.00938743,\
-0.05248823,0.00713604,-0.01745932,0.01562338,0.0079516,-0.01510754,\
0.01571156,-0.00919707,0.00496849,0.01077951,0.00512542,0.00723715,\
-0.11387184]

# 4 runs
diff2 = [-0.04742377,-0.03780329,0.01442457,0.00033786,0.00126173,0.01111509,\
-0.01594925,0.02006936,0.00665698,-0.0008078,-0.0225213,-0.01503244,\
0.01910185,0.04642193,0.0155565,0.04145819,0.01468099,0.00078791,\
0.04638313,0.02289345,0.01146002,0.01208932,0.01255332,0.02884194,\
-0.08420334,0.00943992,0.01778878,0.02376873,0.03144234,0.022533,\
0.01623586,0.03015032,0.01520869,-0.00580916,0.00574579,0.00258796,\
-0.05098155,-0.00415654,0.00701505,0.01119718,0.01161727,0.00451474,\
0.00239116,-0.04543156,-0.00588145,0.02868775,0.01382228,-0.00144639,\
0.00850927,0.03246173,0.02186195,0.02828335,0.01308899,0.02135795,\
0.00733057,0.00221797,-0.03056166,0.00234774,0.00426716,0.01752932,\
-0.14108351,0.01064009,-0.00259531,0.0082411,0.00730135,-0.00245847,\
-0.02983964,-0.04235396,0.02009864,0.00537956,0.01342739,0.01895262,\
-0.02164802,0.02913454,0.01375331,-0.00201419,-0.00711755,0.02351484,\
0.03208569,0.00997857,0.01597623,0.03030826,0.00767595,0.03261274,\
-0.3219613,0.00129843,0.02111318,0.00845215,0.00796586,0.01159092,\
0.01255407,0.00497841,0.00956138,0.01056115,0.01495963,0.00532776,\
0.00460205,0.00855703,-0.00063917,-0.02507999,-0.04576027,0.02509766,\
0.00401705,0.01681295,0.01083347,-0.00926747,0.01831588,0.01171972,\
-0.02581858,0.01466587,-0.01314731,-0.00347991,0.00049435,-0.04565546,\
0.01389581,-0.01141736,0.00506546,-0.00136041,-0.00920839,0.00821443,\
-0.21712095]


# 2 runs
diff3 = [-6.70842228e-02,-1.11114891e-02,7.32828124e-03,1.13802342e-03,\
3.09512434e-03,-6.72933837e-03,-1.45860990e-02,1.23806154e-02,\
-6.29241835e-03,-5.76951634e-03,-4.57107275e-03,-3.74561466e-03,\
3.37421595e-02,7.35988003e-03,1.78719574e-03,8.54783914e-03,\
-1.39245596e-02,3.41921235e-02,1.65867743e-02,4.38714214e-03,\
2.33599969e-02,9.99862875e-03,1.33106222e-02,3.74915535e-02,\
-5.78496215e-02,1.27479774e-03,-3.50883483e-03,-2.61995560e-02,\
3.69705527e-02,3.57764414e-03,2.16235262e-03,1.68609724e-02,\
2.79453925e-03,-3.52208416e-03,1.58550717e-03,-7.53620819e-03,\
-1.57054206e-02,-1.26455312e-02,-1.61158427e-02,1.90787516e-03,\
-4.54817207e-03,-1.20042143e-02,-2.50301041e-03,-4.82381450e-03,\
-3.00907827e-03,6.58715408e-03,-1.01624243e-02,-5.56967020e-03,\
-2.24091302e-02,-2.33476694e-02,4.60177257e-03,1.01938522e-02,\
-1.60177448e-02,-8.09535251e-03,-7.43661837e-05,-6.08575571e-03,\
-1.50458699e-02,-3.01389668e-02,-8.67980580e-03,-2.04715242e-02,\
-5.15482511e-02,-2.50072891e-03,-3.19770019e-02,-1.53974235e-02,\
-1.37276514e-02,-1.61468507e-02,-3.07575277e-02,2.80375439e-02,\
2.09603767e-02,6.80574122e-04,5.18403254e-03,1.11625333e-02,\
2.64992828e-02,3.39218430e-02,1.36967642e-02,2.04840782e-02,\
-1.40103962e-03,3.20860127e-02,3.33960504e-02,-2.43638161e-02,\
7.00454061e-03,7.55272508e-03,-2.48413146e-02,3.90681614e-02,\
-2.48080824e-01,-9.37021115e-03,1.98238241e-02,5.78532600e-03,\
9.59840982e-05,4.13486495e-03,-1.77700787e-02,-3.85650406e-03,\
-1.39653436e-02,-1.91861850e-02,8.74898522e-03,-1.48366021e-02,\
-2.98502347e-02,-7.80637781e-03,1.52651533e-03,-2.81023164e-02,\
1.66198068e-05,-2.53194480e-03,2.69276613e-03,-3.65928031e-04,\
-2.52145215e-02,1.44504769e-02,-1.38545270e-02,4.61616421e-05,\
-7.86892888e-03,-1.86901051e-02,-7.04893109e-02,-2.64619417e-03,\
-8.08752692e-03,8.69808657e-06,2.46945001e-04,-2.53368994e-02,\
-1.23129136e-02,-3.59094601e-03,-5.05156998e-03,-7.29915384e-03,\
-3.13681625e-02]

print(stats.f_oneway(diff1, diff2, diff3))

# plt.scatter([0,1,2,3], [3,4,5,6])
plt.scatter(np.random.rand(len(diff1)), diff1, color='b', alpha=0.3)
plt.scatter(np.random.rand(len(diff2))+2, diff2, color='g', alpha=0.6)
plt.scatter(np.random.rand(len(diff3))+4, diff3, color='orange', alpha=0.9)

plt.show()