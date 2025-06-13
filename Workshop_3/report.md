# Workshop 3 — Detailed Report

## Summary of the Machine Learning Algorithms Implemented

In this project, we implemented a **Deep Q-Network (DQN)** as the primary reinforcement learning algorithm. DQN was selected due to its ability to efficiently handle complex, high-dimensional state spaces by using neural networks to approximate the Q-value function. This approach allows the agent to learn optimal navigation and decision-making policies in a dynamic and partially observable environment. The implementation was developed using the **Stable-Baselines3** library with **PyTorch** as the backend framework, which offers robust tools for reinforcement learning experiments and simplifies the integration with the simulation.

## Description of the Feedback Loops and Their Integration with the Learning Process

The autonomous agent is equipped with a sensor system modeled as a **3×3 local grid view**, representing its immediate surroundings in the environment. This grid provides information about nearby obstacles, delivery points, and potential threats, such as a randomly moving bird acting as a dynamic obstacle. Sensor data is processed by the feedback control mechanism, which maps these inputs to reward signals that guide the learning process. The feedback loop ensures that the agent adapts its actions in real-time, promoting behaviors like avoiding collisions, successfully delivering packages, and adjusting to unpredictable environmental changes. This design aligns with core cybernetic principles of self-regulation and adaptability.

## Analysis of the Agent’s Performance

The agent’s performance will be evaluated through multiple metrics designed to provide insights into learning efficiency and task accomplishment:
- **Cumulative episode reward**: Tracks overall reward obtained in each episode, indicating progress in achieving desired behaviors.
- **Learning curves**: Visualizes reward trends across training episodes to assess convergence patterns.
- **Convergence speed**: Measures the number of episodes needed for the agent to achieve stable and consistent performance.
- **Collision rate**: Quantifies how often the agent collides with static and dynamic obstacles.
- **Successful delivery rate**: Represents the percentage of episodes where the agent completes its delivery task without collisions.

These metrics will be collected under different test conditions, such as varying random seeds and environmental parameters, to validate the robustness of the agent’s learning.

## Challenges Faced During Implementation

Several challenges were encountered during the development of the agent:
- Designing an effective reward function that simultaneously incentivizes delivery success and collision avoidance required careful tuning to prevent unintended behaviors.
- Hyperparameter selection for the DQN algorithm (e.g., learning rate, discount factor, exploration rate) demanded iterative experimentation to achieve stable training.
- Integrating the feedback loop tightly with the DQN update mechanism while maintaining computational efficiency was non-trivial and required performance optimizations.

## Future Work or Improvements

Potential future enhancements to this system include:
- Implementing **multi-agent scenarios** where drones collaborate or compete, enabling the study of distributed decision-making and communication protocols.
- Testing alternative reinforcement learning architectures, such as **Double DQN** or **Dueling DQN**, to further improve learning stability and performance.
- Enhancing the sensory model by incorporating simulated range sensors or camera-like perception for richer environmental understanding.
- Applying **domain randomization** techniques to improve the generalization ability of the agent to new or altered environments.
- Extending the reward function with more nuanced penalties and incentives to better shape desired behaviors.

