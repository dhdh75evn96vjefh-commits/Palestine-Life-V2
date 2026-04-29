import time
import random
from enum import Enum

class DayPhase(Enum):
    DAWN = "فجر"
    MORNING = "صباح"
    NOON = "ظهر"
    AFTERNOON = "عصر"
    EVENING = "مساء"
    NIGHT = "ليل"

class Weather(Enum):
    CLEAR = "صافي"
    CLOUDY = "غائم"
    RAINY = "ممطر"
    FOGGY = "ضباب"

class WorldClock:
    def __init__(self, time_scale=60):
        self.time_scale = time_scale
        self.current_hour = 6
        self.current_minute = 0
        self.weather = Weather.CLEAR
        self.last_weather_change = time.time()

    def update(self):
        real_seconds = time.time()
        game_hours = (real_seconds % (24 * self.time_scale)) / self.time_scale
        self.current_hour = int(game_hours)
        self.current_minute = int((game_hours % 1) * 60)

        if time.time() - self.last_weather_change > 600:
            self._change_weather()
            self.last_weather_change = time.time()

    def _change_weather(self):
        weights = [0.5, 0.3, 0.15, 0.05]
        self.weather = random.choices(
            list(Weather), weights=weights
        )[0]

    def get_phase(self) -> DayPhase:
        h = self.current_hour
        if 5 <= h < 7:
            return DayPhase.DAWN
        elif 7 <= h < 11:
            return DayPhase.MORNING
        elif 11 <= h < 13:
            return DayPhase.NOON
        elif 13 <= h < 17:
            return DayPhase.AFTERNOON
        elif 17 <= h < 20:
            return DayPhase.EVENING
        else:
            return DayPhase.NIGHT

    def get_global_state(self):
        return {
            "hour": self.current_hour,
            "minute": self.current_minute,
            "phase": self.get_phase(),
            "weather": self.weather
}
