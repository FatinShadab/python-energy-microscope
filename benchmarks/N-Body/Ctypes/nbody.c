#include <math.h>
#include <stdlib.h>

#define G 6.67430e-11

typedef struct {
    double mass;
    double position[3];
    double velocity[3];
} Body;

void update_position(Body* body, double dt) {
    for (int i = 0; i < 3; i++) {
        body->position[i] += body->velocity[i] * dt;
    }
}

void update_velocity(Body* body, double* force, double dt) {
    for (int i = 0; i < 3; i++) {
        body->velocity[i] += (force[i] / body->mass) * dt;
    }
}

void compute_force(Body* body1, Body* body2, double* force_out) {
    double distance = 0.0;
    double direction[3];
    
    for (int i = 0; i < 3; i++) {
        direction[i] = body2->position[i] - body1->position[i];
        distance += direction[i] * direction[i];
    }
    
    distance = sqrt(distance);
    
    if (distance == 0) {
        force_out[0] = force_out[1] = force_out[2] = 0.0;
        return;
    }

    double force_magnitude = G * body1->mass * body2->mass / (distance * distance);
    
    for (int i = 0; i < 3; i++) {
        force_out[i] = force_magnitude * direction[i] / distance;
    }
}

void simulate_nbody(Body* bodies, int num_bodies, double dt, int num_steps, double* output_positions) {
    double* forces = (double*)calloc(num_bodies * 3, sizeof(double));

    for (int step = 0; step < num_steps; step++) {
        // Save positions
        for (int i = 0; i < num_bodies; i++) {
            for (int j = 0; j < 3; j++) {
                output_positions[step * num_bodies * 3 + i * 3 + j] = bodies[i].position[j];
            }
        }

        // Reset forces
        for (int i = 0; i < num_bodies * 3; i++) {
            forces[i] = 0.0;
        }

        // Compute forces
        for (int i = 0; i < num_bodies; i++) {
            for (int j = 0; j < num_bodies; j++) {
                if (i != j) {
                    double temp_force[3];
                    compute_force(&bodies[i], &bodies[j], temp_force);
                    for (int k = 0; k < 3; k++) {
                        forces[i * 3 + k] += temp_force[k];
                    }
                }
            }
        }

        // Update velocities and positions
        for (int i = 0; i < num_bodies; i++) {
            update_velocity(&bodies[i], &forces[i * 3], dt);
            update_position(&bodies[i], dt);
        }
    }

    free(forces);
}
