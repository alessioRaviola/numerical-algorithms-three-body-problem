use std::fs;
struct Body {
    x: f64,
    y: f64,
    vx: f64,
    vy: f64,
    mass: f64,
}

fn build_body(x: f64, y: f64, vx: f64, vy: f64, mass: f64) -> Body {
    Body {
        x,
        y,
        vx,
        vy,
        mass,
    }
}

static mut G_GC: f64 = 1.0;

fn newton_gravity_acceleration<const DIM: usize>(
    p: &[Body; DIM],
    ax: &mut[f64; DIM],
    ay: &mut[f64; DIM]
) {
    // Evaluate accelerations for an array of bodies

    for i in 0..DIM {
        ax[i] = 0.0;
        ay[i] = 0.0;
    }

    for i in 0..DIM {
        for j in (i+1)..DIM {
            let rx = p[j].x - p[i].x;
            let ry = p[j].y - p[i].y;
            let r_sqr = ry * ry + rx * rx;
            // Declare k and assign, unsafe becouse G_GC is a static mut
            let k: f64;
            unsafe { k = G_GC / (r_sqr * r_sqr.sqrt()); }

            ax[i] += p[j].mass * k * rx;
            ax[j] += - p[i].mass * k * rx;
            ay[i] += p[j].mass * k * ry;
            ay[j] += - p[i].mass * k * ry;
        }
    }
}

fn newton_gravity_acceleration_attraction<const DIM: usize>(
    p: &[Body; DIM],
    ax: &mut[f64; DIM],
    ay: &mut[f64; DIM],
    attraction: &mut[f64; 2],
) {
    // Evaluate accelerations for an array of bodies
    // Variation of function for compute magnitude of acceleration contribution on earth

    for i in 0..DIM {
        ax[i] = 0.0;
        ay[i] = 0.0;
    }

    for i in 0..DIM {
        for j in (i+1)..DIM {
            let rx = p[j].x - p[i].x;
            let ry = p[j].y - p[i].y;
            let r_sqr = ry * ry + rx * rx;
            // Declare k and assign, unsafe becouse G_GC is a static mut
            let k: f64;
            unsafe { k = G_GC / (r_sqr * r_sqr.sqrt()); }

            ax[i] += p[j].mass * k * rx;
            ax[j] += - p[i].mass * k * rx;
            ay[i] += p[j].mass * k * ry;
            ay[j] += - p[i].mass * k * ry;

            if i == 0 && j == 1 {
                attraction[0] = (p[i].mass * k * p[i].mass * k * (rx * rx + ry * ry)).sqrt();
            } else if i == 1 && j == 2 {
                attraction[1] = (p[j].mass * k * p[j].mass * k * (rx * rx + ry * ry)).sqrt();
            }
        }
    }
}

fn newton_gravity_acceleration_special<const DIM: usize>(
    p: &[Body; DIM],
    ax: &mut[f64; DIM],
    ay: &mut[f64; DIM]
) {
    // Evaluate accelerations for an array of bodies
    // No forces on earth from jupiter

    for i in 0..DIM {
        ax[i] = 0.0;
        ay[i] = 0.0;
    }

    for i in 0..DIM {
        for j in (i+1)..DIM {
            let rx = p[j].x - p[i].x;
            let ry = p[j].y - p[i].y;
            let r_sqr = ry * ry + rx * rx;
            // Declare k and assign, unsafe becouse G_GC is a static mut
            let k: f64;
            unsafe { k = G_GC / (r_sqr * r_sqr.sqrt()); }

            if i == 1 && j == 2 {
                ax[j] += - p[i].mass * k * rx;
                ay[j] += - p[i].mass * k * ry;
            }
            else {
                ax[i] += p[j].mass * k * rx;
                ax[j] += - p[i].mass * k * rx;
                ay[i] += p[j].mass * k * ry;
                ay[j] += - p[i].mass * k * ry;
            }
        }
    }

}

fn verlet_velocity_bodies<const DIM: usize>(
	bodies: &mut [Body; DIM],
	rhs_acc: fn(&[Body; DIM], &mut [f64; DIM], &mut [f64; DIM]),
    ax: &mut [f64; DIM],
    ay: &mut [f64; DIM],
	dt: f64
	) {
	// Make a step using the velocity-Verlet symplectic integrator
	// this methods are used to integrate Newton's equation
	// RHSAcc = evaluate rhs of acceleration in function of position

    let hdt = 0.5 * dt;
	// Set half step velocity
	let mut hvy = [0.0; DIM];
    let mut hvx = [0.0; DIM];
	for i in 0..DIM {
		hvx[i] = bodies[i].vx + (hdt * ax[i]);
        hvy[i] = bodies[i].vy + (hdt * ay[i]);
	}
	// Modify position
	for i in 0..DIM {
		bodies[i].x += dt * hvx[i];
        bodies[i].y += dt * hvy[i];
	}
	// Evaluate RHS of acceleration and update it
	rhs_acc(bodies, ax, ay);
	// Modify velocity
	for i in 0..DIM {
		bodies[i].vx = hvx[i] + (hdt * ax[i]);
        bodies[i].vy = hvy[i] + (hdt * ay[i]);
	}

}

fn verlet_velocity_bodies_attraction<const DIM: usize>(
	bodies: &mut [Body; DIM],
	rhs_acc: fn(&[Body; DIM], &mut [f64; DIM], &mut [f64; DIM], &mut [f64; 2]),
    ax: &mut [f64; DIM],
    ay: &mut [f64; DIM],
	dt: f64,
    attraction: &mut [f64; 2],
	) {
	// Make a step using the velocity-Verlet symplectic integrator
	// this methods are used to integrate Newton's equation
	// RHSAcc = evaluate rhs of acceleration in function of position

    // Variation of main function to compute magnitude of acceleration contributions on Earth

    let hdt = 0.5 * dt;
	// Set half step velocity
	let mut hvy = [0.0; DIM];
    let mut hvx = [0.0; DIM];
	for i in 0..DIM {
		hvx[i] = bodies[i].vx + (hdt * ax[i]);
        hvy[i] = bodies[i].vy + (hdt * ay[i]);
	}
	// Modify position
	for i in 0..DIM {
		bodies[i].x += dt * hvx[i];
        bodies[i].y += dt * hvy[i];
	}
	// Evaluate RHS of acceleration and update it
	rhs_acc(bodies, ax, ay, attraction);
	// Modify velocity
	for i in 0..DIM {
		bodies[i].vx = hvx[i] + (hdt * ax[i]);
        bodies[i].vy = hvy[i] + (hdt * ay[i]);
	}

}

fn test_dual_system(v: f64, dt: f64, indexfile: i32, nsteps: i32) {
    let a: Body = build_body(-0.25, 0.0, 0.0, v, 1.0);
    let b: Body = build_body(0.25, 0.0, 0.0, -v, 1.0);

    let mut bodies = [a, b];
    let mut ax = [0.0; 2];
    let mut ay = [0.0; 2];
    newton_gravity_acceleration(&bodies, &mut ax, &mut ay);

    let mut data: String = "Time;a x;a y;b x;b y\n".to_owned();

    for i in 0..nsteps {
        verlet_velocity_bodies(
            &mut bodies, newton_gravity_acceleration, &mut ax, &mut ay, dt
        );
        data.push_str(&format!("{}", i as f64 * dt));
        // Write data to string
        for j in 0..2 {
            data.push_str(&format!(";{};{}", bodies[j].x, bodies[j].y));
        }
        data.push_str("\n");
    }

    // Write data to file
    fs::write(format!("results/test_dual_{}.csv", indexfile), data).expect("Impossible to write to file!");
}

fn three_body_problem(b1: Body, b2: Body, b3: Body, dt: f64, nsteps: i32, filename: &str) {
    let mut bodies = [b1, b2, b3];
    // Initial acceleration
    let mut ax = [0.0; 3];
    let mut ay = [0.0; 3];
    newton_gravity_acceleration(&bodies, &mut ax, &mut ay);

    // Results string
    let mut data: String = "Time;a x;a y;b x;b y;c x;c y\n".to_owned();

    for i in 0..nsteps {
        verlet_velocity_bodies(
            &mut bodies, newton_gravity_acceleration, &mut ax, &mut ay, dt
        );
        // Write data to string
        data.push_str(&format!("{}", i as f64 * dt));
        for j in 0..3 {
            data.push_str(&format!(";{};{}", bodies[j].x, bodies[j].y));
        }
        data.push_str("\n");
    }

    // Write data to file
    fs::write(format!("results/{}.csv", filename), data).expect("Impossible to write to file!");
}

fn three_body_problem_attraction(b1: Body, b2: Body, b3: Body, dt: f64, nsteps: i32, filename: &str) {
    let mut bodies = [b1, b2, b3];
    // Initial acceleration
    let mut ax = [0.0; 3];
    let mut ay = [0.0; 3];
    let mut attraction = [0.0; 2];
    newton_gravity_acceleration(&bodies, &mut ax, &mut ay);

    // Results string
    let mut data: String = "Time;F_ab;F_bc\n".to_owned();

    for i in 0..nsteps {
        verlet_velocity_bodies_attraction(
            &mut bodies, newton_gravity_acceleration_attraction, &mut ax, &mut ay, dt, &mut attraction
        );
        // Write data to string
        data.push_str(&format!("{}", i as f64 * dt));
        data.push_str(&format!(";{};{}\n", attraction[0], attraction[1]));
    }

    // Write data to file
    fs::write(format!("results/{}_attraction.csv", filename), data).expect("Impossible to write to file!");
}

fn three_body_problem_special(b1: Body, b2: Body, b3: Body, dt: f64, nsteps: i32, filename: &str) {
    let mut bodies = [b1, b2, b3];
    // Initial acceleration
    let mut ax = [0.0; 3];
    let mut ay = [0.0; 3];
    newton_gravity_acceleration(&bodies, &mut ax, &mut ay);

    // Results string
    let mut data: String = "Time;a x;a y;b x;b y;c x;c y\n".to_owned();

    for i in 0..nsteps {
        verlet_velocity_bodies(
            &mut bodies, newton_gravity_acceleration_special, &mut ax, &mut ay, dt
        );
        // Write data to string
        data.push_str(&format!("{}", i as f64 * dt));
        for j in 0..3 {
            data.push_str(&format!(";{};{}", bodies[j].x, bodies[j].y));
        }
        data.push_str("\n");
    }

    // Write data to file
    fs::write(format!("results/{}.csv", filename), data).expect("Impossible to write to file!");
}

fn main() {

    unsafe { G_GC = 1.0; }
    // Data for qualitative tests
    test_dual_system(0.8, 0.01, 0, 100);
    test_dual_system(1.0, 0.01, 1, 100);
    test_dual_system(1.2, 0.01, 2, 100);
    // Data to show difference from theoretical orbit
    test_dual_system(1.0, 0.01, 3, 5000);
    test_dual_system(1.0, 0.001, 4, 50000);


    unsafe { G_GC = 1.184e-4; }
    // Sun - Earth - Jupiter system (Time step: 0.0001 years)
    let sun: Body = build_body(0.0, 0.0, 0.0, 0.0, 3.33e5);
    let earth: Body = build_body(1.017, 0.0, 0.0, 6.174, 1.0);
    let jupiter: Body = build_body(5.457, 0.0, 0.0, 2.622, 3.178e2);
    three_body_problem(sun, earth, jupiter, 0.00001, 1200000, &"sun_earth_jupiter_1");

    let sun: Body = build_body(0.0, 0.0, 0.0, 0.0, 3.33e5);
    let earth: Body = build_body(1.017, 0.0, 0.0, 6.174, 1.0);
    let jupiter_10: Body = build_body(5.457, 0.0, 0.0, 2.622, 3.178e2 * 10.0);
    three_body_problem(sun, earth, jupiter_10, 0.00001, 1200000, &"sun_earth_jupiter_10");

    let sun: Body = build_body(0.0, 0.0, 0.0, 0.0, 3.33e5);
    let earth: Body = build_body(1.017, 0.0, 0.0, 6.174, 1.0);
    let jupiter_100: Body = build_body(5.457, 0.0, 0.0, 2.622, 3.178e2 * 100.0);
    three_body_problem(sun, earth, jupiter_100, 0.00001, 1200000, &"sun_earth_jupiter_100");

    let sun: Body = build_body(0.0, 0.0, 0.0, 0.0, 3.33e5);
    let earth: Body = build_body(1.017, 0.0, 0.0, 6.174, 1.0);
    let jupiter_1000: Body = build_body(5.457, 0.0, 0.0, 2.622, 3.178e2 * 1000.0);
    three_body_problem(sun, earth, jupiter_1000, 0.00001, 225000, &"sun_earth_jupiter_1000");

    // Sun - Earth - Jupiter system (Time step: 0.0001 years) - Attraction
    let sun: Body = build_body(0.0, 0.0, 0.0, 0.0, 3.33e5);
    let earth: Body = build_body(1.017, 0.0, 0.0, 6.174, 1.0);
    let jupiter: Body = build_body(5.457, 0.0, 0.0, 2.622, 3.178e2);
    three_body_problem_attraction(sun, earth, jupiter, 0.00001, 1200000, &"sun_earth_jupiter_1");

    let sun: Body = build_body(0.0, 0.0, 0.0, 0.0, 3.33e5);
    let earth: Body = build_body(1.017, 0.0, 0.0, 6.174, 1.0);
    let jupiter_10: Body = build_body(5.457, 0.0, 0.0, 2.622, 3.178e2 * 10.0);
    three_body_problem_attraction(sun, earth, jupiter_10, 0.00001, 1200000, &"sun_earth_jupiter_10");

    let sun: Body = build_body(0.0, 0.0, 0.0, 0.0, 3.33e5);
    let earth: Body = build_body(1.017, 0.0, 0.0, 6.174, 1.0);
    let jupiter_100: Body = build_body(5.457, 0.0, 0.0, 2.622, 3.178e2 * 100.0);
    three_body_problem_attraction(sun, earth, jupiter_100, 0.00001, 1200000, &"sun_earth_jupiter_100");

    let sun: Body = build_body(0.0, 0.0, 0.0, 0.0, 3.33e5);
    let earth: Body = build_body(1.017, 0.0, 0.0, 6.174, 1.0);
    let jupiter_1000: Body = build_body(5.457, 0.0, 0.0, 2.622, 3.178e2 * 1000.0);
    three_body_problem_attraction(sun, earth, jupiter_1000, 0.00001, 225000, &"sun_earth_jupiter_1000");


    // No sun - jupiter interaction
    let sun: Body = build_body(0.0, 0.0, 0.0, 0.0, 3.33e5);
    let earth: Body = build_body(1.017, 0.0, 0.0, 6.174, 1.0);
    let jupiter: Body = build_body(5.457, 0.0, 0.0, 2.622, 3.178e2);
    three_body_problem_special(sun, earth, jupiter, 0.00001, 1200000, &"sun_earth_jupiter_special_1");

    let sun: Body = build_body(0.0, 0.0, 0.0, 0.0, 3.33e5);
    let earth: Body = build_body(1.017, 0.0, 0.0, 6.174, 1.0);
    let jupiter_10: Body = build_body(5.457, 0.0, 0.0, 2.622, 3.178e2 * 10.0);
    three_body_problem_special(sun, earth, jupiter_10, 0.00001, 1200000, &"sun_earth_jupiter_special_10");

    let sun: Body = build_body(0.0, 0.0, 0.0, 0.0, 3.33e5);
    let earth: Body = build_body(1.017, 0.0, 0.0, 6.174, 1.0);
    let jupiter_100: Body = build_body(5.457, 0.0, 0.0, 2.622, 3.178e2 * 100.0);
    three_body_problem_special(sun, earth, jupiter_100, 0.00001, 1200000, &"sun_earth_jupiter_special_100");

    let sun: Body = build_body(0.0, 0.0, 0.0, 0.0, 3.33e5);
    let earth: Body = build_body(1.017, 0.0, 0.0, 6.174, 1.0);
    let jupiter_1000: Body = build_body(5.457, 0.0, 0.0, 2.622, 3.178e2 * 1000.0);
    three_body_problem_special(sun, earth, jupiter_1000, 0.00001, 225000, &"sun_earth_jupiter_special_1000");    
}