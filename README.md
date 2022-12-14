# numerical-algorithms-three-body-problem
University Project (Università degli Studi di Torino).

Three body problem simulation to study Jupiter's effect on the Earth.

## Usage
Use `cargo run` from inside the directory to run the source code and generate the .csv files containing the results inside the results directory. A single execution generates all the files in one go.

If desired some sections of the execution can be skipped by changing the value of the variables `skip_sej`, `skip_tests` and `skip_adaptive` in `src\main.rs`.

Use `python plotter.py` to run the python code used to plot the results. This needs an argument:
- `-m dual_tests` create the plot for qualitative testing
- `-m dual_diff` create the plot for quantitative testing with a large time-step
- `-m dual_diff_p` create the plot for quantitative testing with a small time-step
- `-m dual_conv` create the plot for the convergence of the algorithm
- `-m sej` create the plots for the Sun-Earth-Jupiter system
- `-m sej_special` create the plots for the Sun-Earth-Jupiter system but with no influence of Jupiter on the Earth
- `-m sej_adaptive` create the plots for the Sun-Earth-Jupiter system integrated with the adaptive time step method

