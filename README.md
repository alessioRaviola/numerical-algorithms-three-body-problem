# numerical-algorithms-three-body-problem
University Project (Università degli Studi di Torino).

Three body problem simulation to study Jupiter's effect on the Earth.

## Usage
Use `cargo run` from inside the directory to run the source code and generate the .csv files containing the results inside the results directory. A single execution generates all the files in one go.

Use `python plotter.py` to run the python code used to plot the results. This can take an argument:
- `-m dual_tests` create the plot for qualitative testing
- `-m dual_diff` create the plot for quantitative testing with a large time-step
- `-m dual_diff_p` create the plot for quantitative testing with a small time-step

If no argument is provided, the code generates the plots for the study of the Sun-Earth-Jupiter system.
