# nllab-platereaderAnalysis
Raw data processing from BMG POLARstar Omega plate reader

[http://laohakunakorn.bio.ac.uk](http://laohakunakorn.bio.ac.uk)

This repository contains code to process raw data from the Omega plate reader into reduced form which can be easily analysed in downstream applications. Equivalent code is available as a python script or jupyter notebook. The jupyter notebook contains extensive beginner-friendly documentation. 

Raw data files must be saved in `.xlsx` format (converted from `.CSV`). These are put into the `raw_data` folder. Outputs of the processing will be saved in the `reduced_data` folder. The plate reader output must be in a format compatible with the scripts: the preferred output format used is called ```List, sorted by wells, only measured```. The instrument export settings file is stored in the `instrument_settings` folder, as well as instrument protocols used to collect the data.

---
### Usage (Docker)

The preferred method of usage is to run the code from one of our lab's predefined Docker containers. We currently have three Docker containers:

	nadanai263/nllab-python:002
	nadanai263/nllab-jupyter:004
	nadanai263/nllab-julia:004

The numeric tags will increase as the containers are updated, so please check them on [DockerHub](https://hub.docker.com/). To use these, clone the repository, open up a terminal and navigate to the directory containing the repository. Then (making sure you have a working [Docker](https://www.docker.com) installation in place), run (on Mac, Linux)

	docker run -it --rm -v "$PWD":/app nadanai263/nllab-python:002 /bin/bash

On Windows, replace `"$PWD"` with `"%CD%"` (for command prompt) or `${pwd}` (for powershell).

This will pull and launch a Docker container, and start up a Linux shell. Your current working folder will be mounted to `/app`. Run the scripts as required.

#### Running Jupyter notebook in Docker container

You can directly start a Jupyter notebook in your current directory, using

	docker run -p 8888:8888 --rm -it -v "$PWD":/home/jovyan nadanai263/nllab-jupyter:004

Again, on Windows replace `"$PWD"` with `"%CD%"` (for command prompt) or `${pwd}` (for powershell).

---
### Usage (local)

The alternative method is to generate your environment locally, using the included pipenv files as a guide.
