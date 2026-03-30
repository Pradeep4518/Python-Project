import numpy as np
from forward_kinematics import forward_kinematics

def verify_ik(dh_params, q_ik, T_desired):
    T_calc, _ = forward_kinematics(dh_params, q_ik)
    pos_err_vec = T_calc[:3,3] - T_desired[:3,3]
    pos_err = np.linalg.norm(pos_err_vec)

    R = T_calc[:3,:3]
    Rd = T_desired[:3,:3]
    R_err = R.T @ Rd
    angle_err = np.arccos(np.clip((np.trace(R_err)-1)/2, -1.0, 1.0))
    return T_calc, pos_err, angle_err
