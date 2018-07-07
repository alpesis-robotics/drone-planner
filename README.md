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

## Step 6. Motion

In ``backyard_flyer_solution.py`` and ``motion_planning.py``, the process of the missions is
the same as

```
arm -> takeoff -> transition -> landing -> disarm -> manual
```

However, the drone flies a box path at the backyard, while a jerky route in the city, is because
the waypoints setup as a box (function ``calculate_box()``) in the ``backyard_flyer_solution.py``,
while as a jerky path (function ``plan_path()``) in the ``motion_planning.py``. The waypoints
define what kind of the path the drone would fly.

### How motion planning works

Let's detail the steps in ``plan_path()``:

- Step 1. Update the ``flight_state`` as ``PLANNING``, and print out ``Searching for a path ...`` on
the console;
- Step 2. Initialize the target position: ``TARGET_ALTITUDE``, ``SAFETY_DISTANCE``, ``self.target_position[2]``;
- Step 3. Print out the initialized positions: ``global_home``, ``global_position``, ``local_position``;
- Step 4. Read the waypoints from ``colliders.csv`` by skipping the first two rows;
- Step 5. Create a grid representation of a 2D configuration space by calling the function ``create_grid()``,
and extract the ``north_offset`` and ``east_offset`` values, then print them out on the console;
- Step 6. Setup the ``grid_start`` and ``grid_goal`` by the ``north_offset`` and ``east_offset``;
- Step 7. Generate a path from A\* search by the extracted grid, start position, goal position and heuristic
function using the function ``a_star()`` and ``heuristic()``;
- Step 8. Extract waypoints from a given path at step 7 and assign back to ``self.waypoints``;
- Step 9. Send the waypoints back by ``self.send_waypoints()``.


### Key function descriptions

Key steps in ``motion_planning.py``:

```
# initialize the drone that contains the values:
# - target_position: numpy array, default value [0.0, 0.0, 0.0];
# - waypoints: a list, default value [];
# - in_mission: boolean, default value true;
# - check_state: a dictionary, default value {};
# - flight_state: an enum class of states, default value States.MANUAL
# - register_callback(): the callback functions of the events, here are local position,
# local velocity and state, the events would be responded to the state updated correspondingly.
drone = MotionPlanning()

# update the flying path
drone.plan_path()
```

Functions provided in ``planning_utils.py``:

- ``create_grid()``: creates a grid representation of a 2D configuration space based on given
obstacle data, drone altitude and safety distance;
- ``a_star()``: A* algorithm for searching the path;
    - ``heuristic()``: the heursitic function;
    - ``valid_actions()``: a list of valid actions based on a given grid and current node;
        - ``Action()``: the action of the directions west, east, north and south that contains the
value of the current grid position and its cost.


### Simulation

Run the script ``motion_planning.py``:

```
$ source activate drone-planner
$ python motion_planning.py
```

The console shows the logs:

```
Logs/TLog.txt
Logs/NavLog.txt
starting connection
arming transition
Searching for a path ...
global home [-122.39745   37.79248    0.     ], position [-122.3974516   37.7924789    0.156    ], local position [-0.11443461 -0.1506926  -0.1565406 ]
North offset = -316, east offset = -445
Local Start and Goal:  (316, 445) (326, 455)
Found a path.
Sending waypoints to simulator ...
takeoff transition
waypoint transition
target position [0, 0, 5, 0]
waypoint transition
target position [0, 1, 5, 0]
waypoint transition
target position [1, 1, 5, 0]
waypoint transition
target position [1, 2, 5, 0]
waypoint transition
target position [2, 2, 5, 0]
waypoint transition
target position [2, 3, 5, 0]
waypoint transition
target position [3, 3, 5, 0]
waypoint transition
target position [3, 4, 5, 0]
waypoint transition
target position [4, 4, 5, 0]
waypoint transition
target position [4, 5, 5, 0]
waypoint transition
target position [5, 5, 5, 0]
waypoint transition
target position [5, 6, 5, 0]
waypoint transition
target position [6, 6, 5, 0]
waypoint transition
target position [6, 7, 5, 0]
waypoint transition
target position [7, 7, 5, 0]
waypoint transition
target position [7, 8, 5, 0]
waypoint transition
target position [8, 8, 5, 0]
waypoint transition
target position [8, 9, 5, 0]
waypoint transition
target position [9, 9, 5, 0]
waypoint transition
target position [9, 10, 5, 0]
waypoint transition
target position [10, 10, 5, 0]
landing transition
disarm transition
manual transition
Closing connection ...
```

Therefore, at the current case, 21 waypoints are extracted from the path searching from a given grid,
start position and goal position using heuristic function. The quadcopter flies a jerky path of these
waypoints to the northeast for about 10m then land.


![Step6_Motion](./images/Step6_Motion.png)

## Step 7. Planner

![Step7_Planning](./images/Step7_Planning.gif)
