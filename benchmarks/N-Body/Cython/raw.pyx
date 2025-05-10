# nbody_sim.pyx
import cython
from libc.math cimport sqrt

cdef double G = 6.67430e-11  # Gravitational constant

cdef class Body:
    cdef public double mass
    cdef public double[3] position
    cdef public double[3] velocity

    def __cinit__(self, double mass, double[:] position, double[:] velocity):
        self.mass = mass
        for i in range(3):
            self.position[i] = position[i]
            self.velocity[i] = velocity[i]

    cpdef update_position(self, double dt):
        for i in range(3):
            self.position[i] += self.velocity[i] * dt

    cpdef update_velocity(self, double[:] force, double dt):
        for i in range(3):
            self.velocity[i] += force[i] / self.mass * dt


cdef void compute_gravitational_force(Body body1, Body body2, double[:] result):
    cdef double dx, dy, dz, distance, force_magnitude
    cdef int i

    dx = body2.position[0] - body1.position[0]
    dy = body2.position[1] - body1.position[1]
    dz = body2.position[2] - body1.position[2]

    distance = sqrt(dx * dx + dy * dy + dz * dz)

    if distance == 0:
        for i in range(3):
            result[i] = 0.0
        return

    force_magnitude = G * body1.mass * body2.mass / (distance * distance)

    result[0] = force_magnitude * dx / distance
    result[1] = force_magnitude * dy / distance
    result[2] = force_magnitude * dz / distance


cpdef simulate_nbody(list bodies, double dt, int num_steps):
    cdef int num_bodies = len(bodies)
    cdef int step, i, j, k

    cdef double[:, :, :] positions = cython.view.array(
        shape=(num_steps, num_bodies, 3), itemsize=cython.sizeof(double), format="d")

    cdef double[:, :] forces = cython.view.array(
        shape=(num_bodies, 3), itemsize=cython.sizeof(double), format="d")

    cdef double[3] force

    for step in range(num_steps):
        for i in range(num_bodies):
            for k in range(3):
                positions[step, i, k] = bodies[i].position[k]

        for i in range(num_bodies):
            for k in range(3):
                forces[i, k] = 0.0

        for i in range(num_bodies):
            for j in range(num_bodies):
                if i != j:
                    compute_gravitational_force(bodies[i], bodies[j], force)
                    for k in range(3):
                        forces[i, k] += force[k]

        for i in range(num_bodies):
            bodies[i].update_velocity(forces[i], dt)
            bodies[i].update_position(dt)

    # Convert memoryview to nested list of lists of lists
    result = []
    for step in range(num_steps):
        step_data = []
        for i in range(num_bodies):
            body_pos = [positions[step, i, 0], positions[step, i, 1], positions[step, i, 2]]
            step_data.append(body_pos)
        result.append(step_data)

    return result
