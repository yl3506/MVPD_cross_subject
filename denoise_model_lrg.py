import os, json, time
import nibabel as nib
import numpy as np
from sklearn.decomposition import PCA
from sklearn import linear_model

# initalize data
### work_dir = '/mindhive/saxelab3/anzellotti/forrest/derivatives/fmriprep/'
### main_out_dir = '/mindhive/saxelab3/anzellotti/forrest/output_denoise/'
### all_subjects = ['sub-01', 'sub-02', 'sub-03', 'sub-04', 'sub-05', 'sub-09', 'sub-10', 'sub-14', 'sub-15', 'sub-16', 'sub-17', 'sub-18', 'sub-19', 'sub-20']
work_dir = '/Users/chloe/Documents/'
main_out_dir = '/Users/chloe/Documents/output_denoise/'
all_subjects = ['sub-01', 'sub-02']
mask = '_CSF_WM_mask_union_bin_shrinked_funcSize.nii.gz'
noise = ''
rois = ['rATL', 'rFFA', 'rOFA', 'rSTS']
total_run = 8
n_pc = 5

if not os.path.exists(main_out_dir):
	os.makedirs(main_out_dir)

# iterate through all subjects
for sub in all_subjects:

	# initialize data
	sub_dir = work_dir + sub + '_complete/'
	sub_out_dir = main_out_dir + sub + '_denoise/'
	mask_dir = sub_out_dir + sub + mask
	if not os.path.exists(sub_out_dir):
		os.makedirs(sub_out_dir)
	
	# load mask
	mask = nib.load(mask_dir).get_data()

	# load the data from all runs
	for run in range(1, total_run + 1):

		print('run number: ' + str(run))
		
		# initialize data
		run_dir = sub_dir + 'ses-movie/func/' + sub + '_ses-movie_task-movie_run-' + str(run) + '_bold_space-MNI152NLin2009cAsym_preproc.nii.gz'
		run_data = nib.load(run_dir).get_data()
		mask_data = np.zeros((int(np.sum(mask)), run_data.shape[3]))
		print('shape of mask_data: ')
		print(mask_data.shape)
		# get roi data
		roi_dir = sub_dir + sub + '_pre/'
		roi_data = []
		first_flag = True
		roi_len = np.zeros(len(rois))
		for m in range(0, len(rois)):
			roi_tmp = np.transpose(np.load(roi_dir + sub + '_' + rois[m] + '_run_' + str(run) + '.npy'))
			if first_flag:
				roi_data = roi_tmp
				first_flag = False
			else:
				roi_data = np.concatenate((roi_data, roi_tmp))
			roi_len[m] = roi_tmp.shape[0]
			print('roi_tmp shape after transpose:')
			print(roi_tmp.shape)
			print('roi_data shape after transpose:')
			print(roi_data.shape)
			print('roi_len: ' + str(roi_len[m]))
		
		t1 = time.time()
		# load data in noise mask
		mask_data = np.transpose(np.load(roi_dir + sub + '_noise_run_' + str(run) + '.npy'))
		t2 = time.time()
		print(t2 - t1)
		print('shape of mask data')
		print(mask_data.shape)
		

		print('ready to do PCA')
		# do PCA on the mask_data
		mask_pc = PCA(n_components = n_pc).fit(mask_data).components_ # get principal components
		mask_pc = np.transpose(mask_pc) # t x 5
		roi_data = np.transpose(roi_data) # t x v

		print('pca finished\nshape of mask_pc: ')
		print(mask_pc.shape)

		# linear regression on each voxel: PCs -> voxel pattern
		print('linear regression step')
		linear = linear_model.LinearRegression()
		linear.fit(mask_pc, roi_data)

		print('fitting finished')
		# predict the activity of each voxel for this run 
		predict = linear.predict(mask_pc)
		brain_real = roi_data - predict # t x v
		brain_real = np.transpose(brain_real)
		
		# weight = np.empty((n_pc, np.sum(roi_mask)))
		# weight_tr = np.transpose(weight)

		# print('shape of initialized weight_tr: ')
		# print(weight_tr.shape)
		
		# weight_tr = np.matmul(brain_data, np.linalg.pinv(mask_pc)) # pseudo inverse

		# print('shape of pca-modeled weight_tr: ')
		# print(weight_tr.shape)

		# # predict the activity of each voxel for this run 
		# predict = np.matmul(weight_tr, mask_pc)
		# brain_real = brain_data - predict

		predict_all = []
		len_count = 0
		# split data into different rois
		for m in range(0, len(rois)):
			predict_all.append(np.transpose(predict[len_count: roi_len[m], :]))
			len_count += roi_len[m]
			print('predict_all number ' + str(m) + '\nshape: ')
			print(predict_all[m].shape)
			# save real data into file
			out_file = sub_out_dir + sub + '_' + str(roi[m]) + '_run_' + str(run) + '_brain_real.npy'
			np.save(out_file, predict_all[m])