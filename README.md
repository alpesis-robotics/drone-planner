# Drone Planner

## Step 1. Simulator

Download the simulator at the [release page](https://github.com/udacity/FCND-Simulator-Releases/releases),
once downloaded, double click to open the simulator that is look like

![Step1_Simulator](./images/Step1_Simulator.png)

## Step 2. Environment

Install miniconda.

```
# download miniconda at https://conda.io/miniconda.html
$ bash ./Miniconda3-latest-MacOSX-x86_64.sh
$ export PATH=/Users/<username>/miniconda3/bin:$PATH
```

Create an environment yaml file ``environment.yml``:

```
name: drone-planner
channels:
    - conda-forge
dependencies:
    - python==3.6.3
    - matplotlib==2.1.1
    - jupyter==1.0.0
    - future==0.16.0
    - lxml==4.1.1
    - networkx==2.1
    - scikit-image==0.13.1
    - scipy==1.0.0
    - shapely==1.6.4
    - scikit-learn==0.19.1
    - pip:
        - git+https://github.com/udacity/udacidrone.git
        - visdom==0.1.7
        - bresenham==0.2
        - msgpack==0.5.6
```

Download the dependencies as defined in the yaml file.

```
$ conda env create -f environment.yml
# useful commands:
# source activate drone-planner
# source deactivate
# conda env remove -n drone-planner
# conda info --envs
# conda clean -tp
```

Once Finished, it would look like

![Step2_Environment](./images/Step2_Environment.png)


## Step 3. Repository

Clone the repository to the local destination.

```
$ git clone https://github.com/udacity/FCND-Motion-Planning
```

Integrated into the project with some modifications as below:

![Step3_Reposity](./images/Step3_Repository.png)

## Step 4. Verification

Activate the environement created at step 2, and run the ``backyard_flyer_solution.py``
to test the setup.

```
$ source activate drone-planner
$ python backyard_flyer_solution.py
Logs/TLog.txt
Logs/NavLog.txt
starting connection
arming transition
takeoff transition
Setting Home
waypoint transition
target position [10.0, 0.0, 3.0]
waypoint transition
target position [10.0, 10.0, 3.0]
waypoint transition
target position [0.0, 10.0, 3.0]
waypoint transition
target position [0.0, 0.0, 3.0]
landing transition
disarm transition
manual transition
Closing connection ...
```

As expected, the quadcopter take off, fly a square rule and land.

![Step4_Verification](./images/Step4_Verification.png)

## Step 5. Inspection

Inspect the relevant files:

```
Relevant files:
- motion_planning.py          # the motion planning script, student task in plan_path()
- planning_utils.py           # the functions of planning utilities
- colliders.csv               # the data of 2.5D map
```
