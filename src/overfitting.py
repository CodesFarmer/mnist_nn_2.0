import numpy as np
from matplotlib import pyplot as matplt

acy_0 = np.load("test_acy_.npy")
acy_1 = np.load("test_acy_L1.npy")
acy_2 = np.load("test_acy_L2.npy")
acy_3 = np.load("test_acy_DPL2.npy")
z = range(0, 200);
matplt.plot(z, acy_0, 'r', z, acy_1, 'g', acy_2, 'b', acy_3, 'y')
matplt.show()