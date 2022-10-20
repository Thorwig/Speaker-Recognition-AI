import numpy as np
import sys
# data = np.load('D:/audio-classification/extracted_features/labels.npy')[:-1]
# np.save('extracted_features/labels.npy',data)

filenamel = "extracted_features/labels.npy"
filenamef = "extracted_features/features.npy"

dataf= np.load(filenamef)
datal= np.load(filenamel)

print(dataf.shape)
print(datal.shape)
# for x in datalabel:
#     if x == id_number:
#         index = datalabel.index(x)
#         datalabel.pop(index)
#         datafeat.pop(index)
#         np.save('D:/audio-classification/extracted_features/labels.npy',np.array(datalabel))
#         np.save('D:/audio-classification/extracted_features/features.npy',np.array(datafeat))