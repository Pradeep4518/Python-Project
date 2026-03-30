import numpy as np
from forward_kinematics import forward_kinematics

def compute_jacobian(dh_params, q):
    T0e, Ts = forward_kinematics(dh_params, q)
    o_n = T0e[:3, 3]
    J = np.zeros((6, 6))
    o_prev = np.array([0.0, 0.0, 0.0])
    z_prev = np.array([0.0, 0.0, 1.0])

    for i in range(6):
        if i > 0:
            Ti = Ts[i-1]
            o_prev = Ti[:3, 3]
            z_prev = Ti[:3, 2]
        Jv = np.cross(z_prev, (o_n - o_prev))
        Jw = z_prev
        J[:3, i] = Jv
        J[3:, i] = Jw
    return J
