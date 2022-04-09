"""_mountain_car.py"""

import numpy as np

import tiles3 as tc


def get_action_value(A, tile_indices, weights):
    """Computes the action-value using the model learned so far.

    Parameters
    ----------
    A: int
        The action.
    tile_indices: array_like, shape (n_tilings, )
        The tile indices corresponding to the state.
    weights: array_like, shape (n_actions, iht_size)
        The weights.

    Returns
    -------
    float
        The action-value.
    """
    return weights[A][tile_indices].sum()


def get_epsilon_greedy_action(ε, tile_indices, weights):
    """Returns an action sampled from the epsilon-greedy policy.

    Parameters
    ----------
    ε: float
        Epsilon.
    tile_indices: array_like, shape (n_tilings, )
        The tile indices corresponding to the state.
    weights: array_like, shape (n_actions, iht_size)
        The weights.

    Returns
    -------
    int
        The action.
    """
    if np.random.rand() < ε:
        A_next = np.random.randint(weights.shape[0])
    else:
        A_next = get_greedy_action(tile_indices, weights)
    return A_next


def get_greedy_action(tile_indices, weights):
    """Computes the greedy action with respect to the given state.

    Parameters
    ----------
    tile_indices: array_like, shape (n_tilings, )
        The tile indices corresponding to the state.
    weights: array_like, shape (n_actions, iht_size)
        The weights.

    Returns
    -------
    int
        The argmax of the action-value function.
    """
    best_action = None
    best_action_value = float('-inf')
    for a in range(weights.shape[0]):
        action_value = get_action_value(a, tile_indices, weights)
        if action_value > best_action_value:
            best_action_value = action_value
            best_action = a
    return best_action


def get_init_weights(n_actions, iht_size):
    """Initializes the weights.

    Returns
    -------
    array_like, shape (n_actions, iht_size)
        The weights.
    """
    return np.zeros((n_actions, iht_size))


def get_tile_indices(iht, n_tiles, n_tilings, S, S_high, S_low):
    """Computes tile indices for the given state.

    Parameters
    ----------
    iht: tc.IHT
        The IHT.
    n_tiles: int
        The number of tiles.
    n_tilings: int
        The number of tilings.
    S: array_like, shape (2, )
        The state.
    S_high: array_like, shape (2, )
        The state upper bounds.
    S_low: array_like, shape (2, )
        The state lower bounds.

    Returns
    -------
    array_like, shape (n_tilings, n_tiles)
        The tile indices corresponding to the state.
    """
    S0_scaled = n_tiles * (S[0] - S_low[0]) / (S_high[0] - S_low[0])
    S1_scaled = n_tiles * (S[1] - S_low[1]) / (S_high[1] - S_low[1])
    tiles = tc.tiles(iht, n_tilings, [S0_scaled, S1_scaled])
    return np.array(tiles)


def update_weights(α, δ, A, tile_indices, weights):
    """Updates the weights using the given state-action pair.

    Parameters
    ----------
    α: float
        The learning rate.
    δ: float
        The TD error.
    A: int
        The action.
    tile_indices: array_like, shape (n_tilings, )
        The tile indices corresponding to the state.
    weights: array_like, shape (n_actions, iht_size)
        The weights.
    """
    weights[A][tile_indices] += α * δ
