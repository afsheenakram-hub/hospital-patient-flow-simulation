# Hospital Patient Flow Simulation

Installation

```bash
pip3 install -r requirements.txt
```

## Usage

```bash
python3 simulation.py
```

Outputs a performance report to console and `simulation_report.txt`.

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

- Patient throughput times
- Queue lengths (prep, surgery, recovery)
- Resource utilization (prep rooms, operating theatre, recovery rooms)
- Operating theatre blocking statistics

## Project Structure

- `simulation.py`: Main simulation logic
- `config.py`: Configuration parameters
- `monitoring.py`: Statistics collection
- `requirements.txt`: Dependencies
