import numpy as np
from forward_kinematics import forward_kinematics
from jacobian import compute_jacobian

def pose_error(T_current, T_desired):
    # position error
    e_p = T_desired[:3, 3] - T_current[:3, 3]
    # orientation error using rotation matrix cross-product form
    R = T_current[:3, :3]
    Rd = T_desired[:3, :3]
    e_o = 0.5 * (
        np.cross(R[:,0], Rd[:,0]) +
        np.cross(R[:,1], Rd[:,1]) +
        np.cross(R[:,2], Rd[:,2])
    )
    return np.hstack((e_p, e_o))

def inverse_kinematics_numeric(dh_params, T_desired, q0=None, max_iter=300, tol=1e-5, damping=1e-3):
    if q0 is None:
        q = np.zeros(6)
    else:
        q = np.array(q0, dtype=float)

    for _ in range(max_iter):
        T, _ = forward_kinematics(dh_params, q)
        e = pose_error(T, T_desired)
        if np.linalg.norm(e) < tol:
            return q, True

        J = compute_jacobian(dh_params, q)
        # damped least squares
        JT = J.T
        dq = JT @ np.linalg.inv(J @ JT + (damping**2) * np.eye(6)) @ e
        q = q + dq

    return q, False
