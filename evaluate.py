from evo.core import metrics
from evo.tools import file_interface
from evo.core import sync


def get_metrics(ref_file, est_file):
    traj_ref = file_interface.read_tum_trajectory_file(ref_file)
    traj_est = file_interface.read_tum_trajectory_file(est_file)
   
    max_diff = 0.01
    traj_ref, traj_est = sync.associate_trajectories(traj_ref, traj_est, max_diff)
    traj_est.align(traj_ref, correct_scale=True, correct_only_scale=False)
    data = (traj_ref, traj_est)

    #APE
    pose_relation = metrics.PoseRelation.translation_part
    ate_metric = metrics.APE(pose_relation)
    ate_metric.process_data(data)
    ate_stat = ate_metric.get_statistic(metrics.StatisticsType.rmse)
    print('ATE: ', round(ate_stat, 2))
    return ate_stat


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('ref_file', help='Ground truth file (it needs to be a in TUM format)')
    parser.add_argument('est_file', help='Odometry estimation (it needs to be a in TUM format)')
    parser.add_argument('--output_path', help='Path to the output file (default: None)')
    args = parser.parse_args()
    ate = get_metrics(args.ref_file, args.est_file)
    if(args.output_path):
        with open(args.output_path, 'w') as f:
            f.write('Ground-truth file: ' + args.ref_file+'\n') 
            f.write('Estimation file: ' + args.est_file+'\n')
            f.write(' ATE: ' + str(ate)+' (m)\n')
