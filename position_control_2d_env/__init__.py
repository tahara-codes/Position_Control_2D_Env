from gym.envs.registration import register

register(
    id='position_control_2d-v0',
    entry_point='position_control_2d_env.position_control_2d_env:PositionControl2DEnv'
)
