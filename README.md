# 🚗 Mountain Car Homework Assignment

The [Mountain Car environment](https://gym.openai.com/envs/MountainCar-v0) was originally described in [1].
A friendly description is also available in the textbook [2].
The goal of this homework assignment is to solve the Mountain Car environment using [SARSA](https://en.wikipedia.org/wiki/State%E2%80%93action%E2%80%93reward%E2%80%93state%E2%80%93action) and tile coding.

## ⚙️ Setup

Create a new Python environment and install [OpenAI Gym](https://gym.openai.com) and [Pygame](https://www.pygame.org):
```
python -m venv ~/gym_env
source ~/gym_env/bin/activate
pip install gym pygame
```

## Solution

The solution is provided alongside the homework so you can tell if your implementation is correct.
You can run the solution (without peeking at it) by running
```
source ~/gym_env/bin/activate
./solution.sh
```

## Instructions

Implement your solution by modifying `homework.py`.
Replace all lines of the form
```
# TODO: Your code here!
```
with your own code.

If you use the helper functions provided in `src/mountain_car/_mountain_car.py`, each `TODO` only requires you to write a single line of code.
You should take a look at these helper functions before starting your implementation.
Note that you can call them directly since the necessary import is already included at the top of `homework.py`.

## 🏃 Running

To run your implementation, execute
```
source ~/gym_env/bin/activate
PYTHONPATH=src ./homework.py
```

## 🆘 Troubleshooting

If the environment renders too quickly (e.g., the car moves so fast you cannot see it), you may have an old version of Gym.
To fix this, change the line
```
env.render()
```
to
```
env.render(); import time; time.sleep(0.01)
```

## Bonus

* Experiment with different learning rates.
* Experiment with different tilings.
* Experiment with different ε.
* Rerun the N episodes many times to generate a distribution for the number of steps to completion.

## 📚 References

**[1]** Moore, Andrew William. "Efficient memory-based learning for robot control." (1990).

**[2]** Sutton, Richard S., and Andrew G. Barto. Reinforcement learning: An introduction. MIT press, 2018.
