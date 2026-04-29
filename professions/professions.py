from abc import ABC, abstractmethod
from core.world_clock import WorldClock, DayPhase, Weather

class BaseProfession(ABC):
    def __init__(self, name: str, player_id: str, world_clock: WorldClock):
        self.name = name
        self.player_id = player_id
        self.world = world_clock
        self.energy = 100

    def calculate_efficiency(self) -> float:
        state = self.world.get_global_state()
        phase = state["phase"]
        weather = state["weather"]
        efficiency = 1.0

        if phase == DayPhase.NIGHT:
            efficiency *= 0.7
        elif phase == DayPhase.DAWN:
            efficiency *= 1.2

        if weather == Weather.RAINY:
            efficiency *= 0.8
        elif weather == Weather.FOGGY:
            efficiency *= 0.9

        return max(0.0, efficiency)

    @abstractmethod
    def work(self):
        pass
