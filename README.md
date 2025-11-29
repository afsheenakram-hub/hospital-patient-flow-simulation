# Hospital Patient Flow Simulation

Installation

```bash
pip3 install -r requirements.txt
```

## Usage
Main Simulation

```bash
python3 simulation.py
```

Outputs a performance report to console and `simulation_report.txt`.

## Running Assignment 3 Experiments

The `experiments.py` script runs all statistical experiments required for Assignment 3:

- 20 independent simulation runs per configuration  
- 3 system configurations: `3p4r`, `3p5r`, `4p5r`  
- Paired-run comparisons using shared seeds  
- 95% confidence intervals  
- Blocking probability analysis  
- Preparation queue length analysis  
- Recovery saturation probability  

### Run All Experiments

```bash
python experiments.py
```

## Configuration

Edit `config.py` to change parameters:

- `num_prep_rooms`: Number of preparation rooms (default: 3)
- `num_recovery_rooms`: Number of recovery rooms (default: 3)
- `interarrival_mean`: Mean inter-arrival time (default: 25.0)
- `prep_time_mean`: Mean preparation time (default: 40.0)
- `surgery_time_mean`: Mean surgery time (default: 20.0)
- `recovery_time_mean`: Mean recovery time (default: 40.0)
- `simulation_time`: Simulation duration (default: 10000.0)

## Output Metrics

System Metrics
- Preparation queue length
- Surgery queue length
- Recovery queue length
- Utilization of all resources
- Operating room blocking probability
- Recovery-room full-state probability

Patient-Level Metrics
- Throughput time of each patient
- Average urgent vs routine throughput

## Project Structure

- `simulation.py`: Main simulation logic
- `config.py`: Configuration parameters
- `monitoring.py`: Statistics collection
- `experiments.py`: Independent and Paired Analysis
- `requirements.txt`: Dependencies
