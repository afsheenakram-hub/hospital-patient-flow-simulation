from dataclasses import dataclass
from typing import Callable
import random


@dataclass
class SimulationConfig:
    num_prep_rooms: int = 3
    num_operating_theatres: int = 1
    num_recovery_rooms: int = 3
    interarrival_mean: float = 25.0
    prep_time_mean: float = 40.0
    surgery_time_mean: float = 20.0
    recovery_time_mean: float = 40.0
    simulation_time: float = 10000.0
    monitoring_interval: float = 1.0
    random_seed: int = None
    
    def get_interarrival_generator(self) -> Callable[[], float]:
        def generator():
            return random.expovariate(1.0 / self.interarrival_mean)
        return generator
    
    def get_prep_time_generator(self) -> Callable[[], float]:
        def generator():
            return random.expovariate(1.0 / self.prep_time_mean)
        return generator
    
    def get_surgery_time_generator(self) -> Callable[[], float]:
        def generator():
            return random.expovariate(1.0 / self.surgery_time_mean)
        return generator
    
    def get_recovery_time_generator(self) -> Callable[[], float]:
        def generator():
            return random.expovariate(1.0 / self.recovery_time_mean)
        return generator
    
    def initialize_random_seed(self):
        if self.random_seed is not None:
            random.seed(self.random_seed)


DEFAULT_CONFIG = SimulationConfig(
    num_prep_rooms=3,
    num_recovery_rooms=3,
    interarrival_mean=25.0,
    prep_time_mean=40.0,
    surgery_time_mean=20.0,
    recovery_time_mean=40.0,
    simulation_time=10000.0,
    monitoring_interval=1.0,
    random_seed=42
)

