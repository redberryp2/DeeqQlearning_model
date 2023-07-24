# dqn action values
action_values = [-0.75, -0.5, -0.25, -0.15, -0.1, -0.05, 0,
                0.05, 0.1, 0.15, 0.25, 0.5, 0.75]
action_map = {i:x for i, x in enumerate(action_values)}

env_params = {
    'target_speed' :50 ,
    'max_iter': 4000,
    'start_buffer': 4000,
    'train_freq': 1,
    'save_freq': 2000,
    'start_ep': 513,
    'max_dist_from_waypoint': 20
}