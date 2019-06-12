##############################################################################
Drone Planner
##############################################################################

::

    $ git clone https://github.com/alpesis-robotics/drone-planner.git
    $ cd drone-planner

    $ # download miniconda at https://conda.io/miniconda.html
    $ conda env create -f environment.yml    # if env has not created yet
    $ source activate drone-planner   # if env has been created

    # download the simulator at https://github.com/udacity/FCND-Simulator-Releases/releases
    # double click to open the simulator
    # choose the scenario: motion planning
    $ cd planner
    $ python motion_planning.py
