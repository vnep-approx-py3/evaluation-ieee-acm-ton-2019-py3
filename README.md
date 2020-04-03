
# Overview

This repository contains the **Python 3.X** evaluation code as well as the raw results presented in our IEEE/ACM Transactions on Networking paper [1]. The original **Python 2.7** code can be found in the repository **[https://github.com/vnep-approx/evaluation-ieee-acm-ton-2019](https://github.com/vnep-approx/evaluation-ieee-acm-ton-2019)**.

The implementation of the respective algorithms can be found in our separate python packages: 
- **[alib](https://github.com/vnep-approx-py3/alib)**, providing for example the data model and the Mixed-Integer Program for the classic multi-commodity formulation), as well as
- **[vnep_approx](https://github.com/vnep-approx-py3/vnep_approx)**, providing the novel Linear Programming (LP) formulation for cactus graphs -- and beyond these (see [3]) -- as well
as our proposed Randomized Rounding algorithms

Due to the size of the respective pickle-files, the generated scenarios and the full results for the algorithms is not contained in the repository but can be made accessible 
to anyone interested (see contact at the end of the page). The data for plotting -- containing the most essential information -- together with the plots
are stored within the **[results](results)** folder. 
**Note:** As the results were generated using the Python 2.7 implementation, we cannot guarantee that the contained pickle files can be fully used in Python 3.7.

Furthermore, for testing out the framework, we provide the folder **[sample](sample)** with the bash script **[run_samples.sh](sample/run_samples.sh)**
to 
1. generate a small set of scenarios,
2. solve these using the classic multi-commodity flow Mixed-Integer Program (MIP) and our randomized rounding algorithms, and
3. evaluate these tiny examples by plotting the respective plots (see below for detailed discussion).

## Papers

**[1]** Matthias Rost, Stefan Schmid: Virtual Network Embedding Approximations:
Leveraging Randomized Rounding. IEEE/ACM Transactions on Networking. 2019 (to appear)

# Dependencies and Requirements

The **evaluation_ieee_acm_ton_2019** library requires Python 3.X. Required python libraries are gurobipy, numpy, matplotlib, click,  **[alib](https://github.com/vnep-approx-py3/alib)**,  **[vnep-approx](https://github.com/vnep-approx-py3/vnep-approx)**, **[evaluation-ifip-networking-2018](https://github.com/vnep-approx-py3/evaluation-ifip-networking-2018)**.

Gurobi must be installed and the .../gurobi64/lib directory added to the environment variable LD_LIBRARY_PATH.

For generating and executing (etc.) experiments, the environment variable **ALIB_EXPERIMENT_HOME** should be set to a path,
such that the subfolders input/ output/ and log/ exist. If this environment variable is not set, the current working directory is traversed upwards until a directory containing input/, output/, and log/ is found.

**Note**: Our source was tested on Linux (specifically Ubuntu 14 and Ubuntu 16) and Mac OS X 10.15.  

# Installation

To install **evaluation_ieee_acm_ton_2019**, we provide a setup script. Simply execute from within evaluation_ifip_networking_2018's root directory: 

```
pip install .
```

Furthermore, if the code base will be edited by you, we propose to install it as editable:
```
pip install -e .
```
When choosing this option, sources are not copied during the installation but the local sources are used: changes to
the sources are directly reflected in the installed package.

We generally propose to install **evaluation_ifip_networking_2018** into a virtual environment (together with **vnep_approx** and **alib**).

# Usage

You may either use our code via our API by importing the library or via our command line interface:

```
python -m evaluation_ieee_acm_ton_2019.cli
Usage: cli.py [OPTIONS] COMMAND [ARGS]...

  This command-line interface allows you to access major parts of the VNEP-
  Approx framework developed by Matthias Rost, Elias Döhne, Alexander
  Elvers, and Tom Koch. In particular, it allows to reproduce the results
  presented in the paper:

  "Virtual Network Embedding Approximations: Leveraging Randomized
  Rounding", Matthias Rost and Stefan Schmid (IEEE/ACM TON 2019)

  Note that each commands provides a detailed help page. To access the help,
  simply type the commmand and --help.

Options:
  --help  Show this message and exit.

Commands:
  evaluate-results                create plots for baseline and randround
                                  solution

  generate-scenarios              generate scenarios according to yaml
                                  specification

  pretty-print                    pretty print contents of pickle file
  reduce-to-plotdata-baseline-pickle
                                  extracts data to be plotted for baseline
                                  (MCF)

  reduce-to-plotdata-randround-pickle
                                  extracts data to be plotted for randomized
                                  rounding alg (Triumvirate)

  start-experiment                compute solutions to scenarios
```

# Step-by-Step Manual to Reproduce Results

The following worked on Ubuntu 16.04, but depending on the operating system or Linux variant,
some minor changes might be necessary. In the following, we outline the general idea of our framework
based on the example provided in the **[sample](sample)** folder. In fact, the steps discussed below
can all be found in the file **[run_samples](sample/run_samples.sh)**, which can be executed after having created
the virtual environment for the project.


## Creating a Virtual Environment and Installing Packages

First, create and activate a novel virtual environment for python3.7. 

```
python3.7 -m venv venv          #create new virtual environment in folder venv 
source venv/bin/activate        #activate the virtual environment
```

With the virtual environment still active, install the python extensions of [Gurobi](http://www.gurobi.com/) within the
virtual environment. Note that you need to first download and install a license of Gurobi (which is free for academic use). 
```
cd ~/programs/gurobi751/linux64/    #change to the directory of gurobi
python setup.py install             #install gurobipy within (!) the virtual environment
```

Then, assuming that all packages, i.e. **alib, vnep_approx**, and **evaluation_ifip_networking_2018**, are downloaded 
/ cloned to the same directory, simply execute the following within each of the packages' root directories:

```
pip install -e .
```

## Generate Scenarios
First, to use our framework, make sure that you set the environment variable **ALIB_EXPERIMENT_HOME** to a directory
containing (initially empty) folders **input/**, **output/**, and **log/**. Having said that, and activated the 
virtual environment created above, you can execute the following command to generate scenarios according to the parameters
specified in the file **[sample_scenarios.yml](sample/sample_scenarios.yml)**. Most of the parameters of the file
**[sample_scenarios.yml](sample/sample_scenarios.yml)** should be quite self-explanatory and you might read-up on the
meaning of the parameters in the **alib**.
```
python -m evaluation_ifip_networking_2018.cli generate-scenarios sample_scenarios.yml sample_scenarios.pickle
```
If no error occured (check the log file in the log-folder!), you can move the generated pickle file to the **input/** folder 
and clean the **log/**-folder.

## Run Algorithms

To run the respective algorithms, you can execute the following commands. 

```
python -m evaluation_ifip_networking_2018.cli start-experiment sample_mip_execution.yml 0 10000 --concurrent 2
python -m evaluation_ifip_networking_2018.cli start-experiment sample_randround_execution.yml 0 10000 --concurrent 2
```

Note that 2 processes are used for the computation and 
that afer each execution the log-folder must be cleared and that the outputs must be placed into the input folder for
the next steps.

Furthermore, note that the input and output files for the experiment are stored in the respective **yaml** files.
Besides the input and output names, the yaml files **[sample_mip_execution.yml](sample/sample_mip_execution.yml)** and 
**[sample_randround_execution.yml](sample/sample_randround_execution.yml)** specify the algorithm to be executed and 
its parameters.


## Reduce Data to Plot Data
The result pickles of both algorithm contain a lot of details: besides the scenarios, they also contain all mappings found
together with extensive information on the algorithm's execution. Due to the large size of these pickles, data to be plotted
must be extracted before plotting it. This not only saves time when loading the data but also reduces the memory footprint 
by a lot.
 

```
python -m evaluation_ifip_networking_2018.cli reduce-to-plotdata-baseline-pickle sample_scenarios_results_mip.pickle 
python -m evaluation_ifip_networking_2018.cli reduce-to-plotdata-randround-pickle sample_scenarios_results_randround.pickle
```

Again, after executing each of these commands, the **log/**-folder must be cleared and the resulting (reduced) pickled must be placed
into the **input/-folder**.

## Plotting Data

In the last steps, the data can be plotted using the **evaluate_results* commands. It expects as first arguments the 
reduced pickles of the MIP and the randomized rounding algorithm, and the output path.

```
mkdir -p ./plots
python -m evaluation_ifip_networking_2018.cli evaluate_results sample_scenarios_results_mip_reduced.pickle sample_scenarios_results_randround_reduced.pickle ./plots --overwrite --output_filetype png --non-papermode  --filter_max_depth 0
```

Via many additional parameters, the output can be controlled:

```
python -m evaluation_ieee_acm_ton_2019.cli evaluate-results --help
Usage: cli.py evaluate-results [OPTIONS] BASELINE_PICKLE_NAME
                               RANDROUND_PICKLE_NAME OUTPUT_DIRECTORY

Options:
  --baseline_algorithm_id TEXT    algorithm id of baseline algorithm; if not
                                  given it will be asked for.

  --baseline_execution_config INTEGER
                                  execution (configuration) id of baseline
                                  alg; if not given it will be asked for.

  --randround_algorithm_id TEXT   algorithm id of randround algorithm; if not
                                  given it will be asked for.

  --randround_execution_config INTEGER
                                  execution (configuration) id of randround
                                  alg; if not given it will be asked for.

  --exclude_generation_parameters TEXT
                                  generation parameters that shall be
                                  excluded. Must ge given as python evaluable
                                  list of dicts. Example format:
                                  "{'number_of_requests': [20]}"

  --filter_parameter_keys TEXT    generation parameters whose values will
                                  represent filters. Must be given as string
                                  detailing a python list containing
                                  strings.Example: "['number_of_requests',
                                  'edge_resource_factor',
                                  'node_resource_factor']"

  --filter_max_depth INTEGER      Maximal recursive depth up to which
                                  permutations of filters are considered.

  --overwrite / --no_overwrite    overwrite existing files?
  --papermode / --non-papermode   output 'paper-ready' figures or figures
                                  containing additional statistical data?

  --output_filetype [png|pdf|eps]
                                  the filetype which shall be created
  --log_level_print TEXT          log level for stdout
  --log_level_file TEXT           log level for stdout
  --help                          Show this message and exit.
```

Specifically, note that the **algorithm id** as well as the **execution config** can be passed to this command. While the
**algorithm id** refers to the ids specified in the yaml files (e.g. **ID: ClassicMCF**), the **execution config** is a numerical
value indexing the configuration in the list. For example, by setting **timelimit: [600,10800]** for the **ClassicMCF** algorithm,
the algorithm would be executed twice: once with a time limit of 10 minutes and once with a time limit of 3 hours. 

# Contact and Acknowledgement

If you have any questions, either open up an issue on GitHub or write a mail to mrost<AT>inet.tu-berlin<DOT>de.

Major parts of this code were developed under the support of the **German BMBF Software Campus grant 01IS1205** from 2016 to 2018.