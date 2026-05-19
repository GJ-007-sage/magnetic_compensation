import numpy as np
mm = 1e-3

PMTs = {
    'PMT1': np.array([-760, -834, 0]) * mm,
    'PMT2': np.array([-760, 0, 0]) * mm,
    'PMT3': np.array([-530, 1173, 0]) * mm,
    'PMT4': np.array([530, -837, 0]) * mm,
    'PMT5': np.array([530, 3, 0]) * mm,
    'PMT6': np.array([530, 1173, 0]) * mm,
}