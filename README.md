# IBEX Pipeline 🛰️

IBEX Pipeline downloads public sky maps from NASA's Interstellar Boundary Explorer (IBEX),
checks each file for problems, plots the maps, and reports what changed between two data
releases. IBEX-Hi, the sensor these maps come from, was built by Los Alamos National
Laboratory and Southwest Research Institute.

This is a learning project for practicing data pipelines, Python, Bash, and Git.

## Status

🚧 Work in progress

- [x] Set up the environment and repo
- [x] Download IBEX-Hi maps from data releases 16 and 18
- [ ] Read a map file and check it against its header
- [ ] Plot an all-sky map
- [ ] Compare the same maps across releases 16 and 18
- [ ] Run the pipeline on a schedule with cron and log the results
- [ ] Add a status report (last run, disk usage, errors)
- [ ] Add GitLab CI for style checks and tests

## Data

IBEX data releases from the IBEX science team (https://ibex.princeton.edu/DataRelease),
mirrored by NASA's Space Physics Data Facility (https://cdaweb.gsfc.nasa.gov/pub/data/ibex/).
