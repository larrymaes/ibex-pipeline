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
- [x] Read a map file and check it against its header
- [x] Plot an all-sky map
- [x] Compare the same maps across releases 16 and 18
- [ ] Run the pipeline on a schedule with cron and log the results
- [ ] Add a status report (last run, disk usage, errors)
- [ ] Add GitLab CI for style checks and tests

## Findings

### The IBEX ribbon

![IBEX-Hi all-sky map showing the ribbon](docs/ribbon_hi4.png)

Fourteen years of IBEX-Hi data (2009–2022, energy step 4), centered on the heliosphere's nose. The bright arc is the IBEX ribbon, discovered by IBEX in 2009.

### What changed between release 16 and release 18

Full table: [docs/compare_r16_r18.md](docs/compare_r16_r18.md)

- Release 18 changed nearly every observed flux pixel in the 2009A map, a small increase of about +0.4% to +1.9% (median), largest at low energies.
- It also dropped 25–27 low-energy pixels (steps 2–3) as unobserved. This matches the gap counts from `check_maps.py`.
- Exposure maps changed in 1,136 pixels, but by tiny amounts (median 0.00%).

## Data

IBEX data releases from the IBEX science team (https://ibex.princeton.edu/DataRelease),
mirrored by NASA's Space Physics Data Facility (https://cdaweb.gsfc.nasa.gov/pub/data/ibex/).
