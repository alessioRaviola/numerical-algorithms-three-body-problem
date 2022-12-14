
use std::fs;

use crate::{Body, verlet_velocity_bodies};
use crate::newton_gravity_acceleration;

// If the error is lower than this, double the timestep
const LOW_BOUND: f64 = 1e-14;
// if intead is higher than this, half it
const HIGH_BOUND: f64 = 1e-8;

/// Verlet-velocity itegrator implementation with adaptive time-step.
/// The time step supplied will be double the minimum time-step used.
pub fn verlet_velocity_bodies_adaptive<const DIM: usize>(
    bodies: &mut [Body; DIM],
    rhs_acc: fn(&[Body; DIM], &mut [f64; DIM], &mut [f64; DIM]),
    ax: &mut [f64; DIM],
    ay: &mut [f64; DIM],
    dt: &mut f64
) {

    // Create two copies of the bodies and accelerations.
    // For the first copy the integration will be done one time with timestep = dt.
    let mut bodies_one = bodies.clone();
    let mut ax_one = ax.clone();
    let mut ay_one = ay.clone();
    // On the second copy the integration will be done instead two times with
    // timestep = 0.5 * dt.
    let mut bodies_half = bodies.clone();
    let mut ax_half = ax.clone();
    let mut ay_half = ay.clone();


    // Single step integration
    verlet_velocity_bodies(
        &mut bodies_one, rhs_acc,
        &mut ax_one, &mut ay_one,
        *dt
    );

    // Double step integration
    verlet_velocity_bodies(
        &mut bodies_half, rhs_acc,
        &mut ax_half, &mut ay_half,
        *dt * 0.5
    );
    verlet_velocity_bodies(
        &mut bodies_half, rhs_acc,
        &mut ax_half, &mut ay_half,
        *dt * 0.5
    );


    // Check if the timestep must be doubled, halved or neither
    // this is done with a check on the error summing the
    // differences between positions of the bodies
    // i.e. error = \sum_i^DIM |x_{i,1} + y_{i,1} - x_{i,.5} - y_{i,.5}|
    let mut error = 0.0;
    for i in 0..DIM {
        error += (
            bodies_one[i].x + bodies_one[i].y
            - bodies_half[i].x - bodies_half[i].y
        ).abs();
    }

    // If the timestep must be doubled, double it, set result, then return
    if error < LOW_BOUND {
        *dt = 2.0 * *dt;
    }
    
    // If it has to be halved, half it then repeat this integration
    else if error > HIGH_BOUND {
        *dt = 0.5 * *dt;
        verlet_velocity_bodies_adaptive(bodies, rhs_acc, ax, ay, dt)
    }

    // If remains the same set the result, then return
    *bodies = bodies_half;
    *ax = ax_half;
    *ay = ay_half;
}

pub fn three_body_problem_adaptive(
    b1: Body, b2: Body, b3: Body,
    mut dt: f64, max_time: f64,
    filename: &str
) {
    let mut bodies = [b1, b2, b3];
    // Initial acceleration
    let mut ax = [0.0; 3];
    let mut ay = [0.0; 3];
    newton_gravity_acceleration(&bodies, &mut ax, &mut ay);

    // Results string
    let mut data: String = "Time;a x;a y;b x;b y;c x;c y\n".to_owned();

    let mut time = 0.0;
    while time < max_time {
        verlet_velocity_bodies_adaptive(
            &mut bodies, newton_gravity_acceleration, &mut ax, &mut ay, &mut dt
        );
        time += dt;
        // Write data to string
        data.push_str(&format!("{}", time));
        for j in 0..3 {
            data.push_str(&format!(";{};{}", bodies[j].x, bodies[j].y));
        }
        data.push_str("\n");
    }

    // Write data to file
    fs::write(format!("results/{}.csv", filename), data)
        .expect("Impossible to write to file!");
}