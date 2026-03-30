import numpy as np
from dh import dh_transform

def forward_kinematics(dh_params, q):
    T = np.eye(4)
    Ts = []
    for (a, alpha, d, theta_offset), qi in zip(dh_params, q):
        A = dh_transform(a, alpha, d, qi + theta_offset)
        T = T @ A
        Ts.append(T.copy())
    return T, Ts
