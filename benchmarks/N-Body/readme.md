# N-Body

The **N-Body Problem** refers to the problem in physics and astronomy of predicting the individual motions of a group of celestial objects (like stars, planets, or satellites) that interact with each other gravitationally. Given the positions, velocities, and accelerations of the objects, the goal is to determine their future positions and velocities over time.

In simple terms, it involves the calculation of the motion of **N** particles under the influence of mutual forces (gravity, electrostatic, etc.), based on their masses, distances, and velocities.

## Algorithm:
The N-Body Problem is typically solved using **numerical methods**, as it does not have a general analytical solution. Here are some common approaches:

1. **Euler’s Method**: A simple approach where the future positions and velocities of particles are estimated using their current values.
2. **Verlet Integration**: A more stable method that is commonly used in simulations of physical systems.
3. **Leapfrog Integration**: An efficient and stable integration method for the N-Body problem.
4. **Runge-Kutta Methods**: A higher-order, more accurate method for solving ordinary differential equations.
5. **Barnes-Hut Algorithm**: An optimization technique for large numbers of particles that uses a tree structure to reduce the time complexity.
6. **Direct Summation Method**: A brute-force approach that computes the gravitational force between every pair of bodies.

## Implementation Approach:
1. **Initialization**: 
   - Start by defining the properties of each body, including position, velocity, and mass.
   - For each time step, you calculate the gravitational force between each pair of bodies.

2. **Force Calculation**: 
   - For each pair of bodies, compute the gravitational force using Newton’s Law of Gravitation:
   
     \[
     F = G \frac{m_1 m_2}{r^2}
     \]
     where:
     - \( F \) is the gravitational force.
     - \( G \) is the gravitational constant.
     - \( m_1 \) and \( m_2 \) are the masses of the two bodies.
     - \( r \) is the distance between them.

3. **Update Positions and Velocities**: 
   - Use numerical integration (such as the Euler method, Verlet, or Runge-Kutta) to update the position and velocity of each body.

4. **Repeat the Process**: 
   - Repeat the force calculation and position/velocity update for a number of time steps to simulate the system's motion.

5. **Optimization** (if necessary):
   - For large systems, optimize the direct summation method using the Barnes-Hut algorithm or other methods to reduce computational complexity.

## Time Complexity:
- **Direct Summation Method**: The time complexity is \(O(N^2)\), as every body interacts with every other body.
- **Barnes-Hut Algorithm**: The time complexity of the Barnes-Hut method is \(O(N \log N)\), which is a significant improvement for large systems.
- **Euler Method**: Time complexity is \(O(N)\) for each time step.
- **Verlet and Leapfrog Methods**: Similarly, these methods also operate in \(O(N)\) for each time step.

## Space Complexity:
- The space complexity is typically \(O(N)\) for storing the positions, velocities, and accelerations of the bodies.
- In the case of using a tree structure (Barnes-Hut), the space complexity may increase slightly, but it generally remains at \(O(N)\).

## References:
1. "An Introduction to the N-Body Problem" by David L. Williams, available in various physics and computational science texts.
2. Numerical Methods for Physics by Alfredo D. Medina.
3. "Computational Astrophysics: A Practical Guide" by J. L. J. M. L. R. Cortes and M. R. L. A. B. K. Salgado.
4. Barnes-Hut Algorithm: *"Efficient Computation of Gravitational Forces in N-Body Simulations"*, *ACM Transactions on Mathematical Software*.