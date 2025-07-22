import evo.main_ape as main_ape
import evo.main_rpe as main_rpe

from evo.core import metrics
from evo.tools import file_interface
from evo.core import sync

def get_rte(traj_ref, traj_est, correct_scale=False):
    return main_rpe.rpe(traj_ref, traj_est, 
                          pose_relation=metrics.PoseRelation.translation_part,
                          align_origin=True,
                          align=True,
                          correct_scale=correct_scale,
                          delta=1, delta_unit=metrics.Unit.frames) 

def get_roe(traj_ref, traj_est, correct_scale=False):
    return main_rpe.rpe(traj_ref, traj_est, 
                          pose_relation=metrics.PoseRelation.rotation_angle_deg,
                          align_origin=True,
                          align=True,
                          correct_scale=correct_scale,
                          delta=1, delta_unit=metrics.Unit.frames)


def get_ate(traj_ref, traj_est, correct_scale=False):
    return main_ape.ape(traj_ref, traj_est, 
                          pose_relation=metrics.PoseRelation.translation_part,
                          align_origin=True,
                          align=True,
                          correct_scale=correct_scale)



if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('ref_file', help='Ground truth file (it needs to be a in TUM format)')
    parser.add_argument('est_file', help='Odometry estimation (it needs to be a in TUM format)')
    parser.add_argument('--correct_scale', action='store_true', help='Correct scale of the trajectory')
    parser.add_argument('--output_path', help='Path to the output file (default: None)')
    args = parser.parse_args()


    traj_ref = file_interface.read_tum_trajectory_file(args.ref_file)
    traj_est = file_interface.read_tum_trajectory_file(args.est_file)
   
    max_diff = 0.01
    traj_ref, traj_est = sync.associate_trajectories(traj_ref, traj_est, max_diff)


    ate = get_ate(traj_ref=traj_ref, traj_est=traj_est, correct_scale=args.correct_scale)
    rte = get_rte(traj_ref=traj_ref, traj_est=traj_est, correct_scale=args.correct_scale)
    roe = get_roe(traj_ref=traj_ref, traj_est=traj_est, correct_scale=args.correct_scale)
    print('ATE (m):', ate)
    print('RTE (m/frame):', rte)
    print('ROE (deg/frame):', roe)
        
    if(args.output_path):
        with open(args.output_path, 'w') as f:
            f.write(f'ATE (m): {ate.get_all_statistics().rmse}\n')
            f.write(f'RTE (m/frame): {rte.get_all_statistics().rmse}\n')
            f.write(f'ROE (deg/frame): {roe.get_all_statistics().rmse}\n')