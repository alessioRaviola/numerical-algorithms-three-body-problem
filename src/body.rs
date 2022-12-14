#[derive(Clone)]
pub struct Body {
    pub x: f64,
    pub y: f64,
    pub vx: f64,
    pub vy: f64,
    pub mass: f64,
}

pub fn build_body(x: f64, y: f64, vx: f64, vy: f64, mass: f64) -> Body {
    Body {
        x,
        y,
        vx,
        vy,
        mass,
    }
}