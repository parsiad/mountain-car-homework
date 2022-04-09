#!/usr/bin/env python

import sys

import gym

from mountain_car_homework import *
import tiles3 as tc

# yapf: disable
IHT_SIZE                = 4096
MAX_N_STEPS_PER_EPISODE = 1000
N_TILINGS               = 8
N_TILES                 = 8
N_EPISODES              = 50
α                       = 1. / N_TILINGS
γ                       = 1.
ε                       = 0.1
# yapf: enable

gym.envs.register(
    id='MountainCarHomework-v0',
    entry_point='gym.envs.classic_control:MountainCarEnv',
    max_episode_steps=MAX_N_STEPS_PER_EPISODE,
)
env = gym.make('MountainCarHomework-v0')

# Initialize an index hash table (IHT) to implement tile coding.
# You can read more about IHTs on Richard Sutton's website: http://incompleteideas.net/tiles/tiles3.html
iht = tc.IHT(IHT_SIZE)

# Initialize the weights.
weights = # TODO: Your code here!

for episode in range(1, N_EPISODES + 1):
    S_init = env.reset()

    # Tile indices for the current state.
    tile_indices = get_tile_indices(
        iht,
        N_TILES,
        N_TILINGS,
        S_init,
        env.observation_space.high,
        env.observation_space.low,
    )

    # Sample the ε-greedy policy to get the first action.
    A = # TODO: Your code here!

    step = 0
    done = False
    while not done:

        # Perform action and observe reward and next state.
        S_next, R_next, done, _ = env.step(A)

        # Render last episode only.
        if episode == N_EPISODES:
            env.render()

        # Tile indices for the next state.
        tile_indices_next = get_tile_indices(
            iht,
            N_TILES,
            N_TILINGS,
            S_next,
            env.observation_space.high,
            env.observation_space.low,
        )

        # Compute the action-value for the current state-action pair.
        Q = # TODO: Your code here!

        # Sample the ε-greedy policy to get the next action.
        A_next = # TODO: Your code here!

        # Compute the action-value for the next state-action pair.
        Q_next = # TODO: Your code here!
        if done:
            Q_next = 0.

        # Compute the TD error.
        δ = # TODO: Your code here!

        # Update the weights.
        # TODO: Your code here!

        tile_indices = tile_indices_next
        A = A_next
        step += 1

    sys.stderr.write(f'Episode {episode} took {step} steps\n')

env.close()
