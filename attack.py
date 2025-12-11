# attack.py

class SlowModificationAttack:
    """Attack that slowly corrupts the actuator command over multiple control cycles."""

    def __init__(self, required_time, dt, max_bias):
        self.required_time = required_time
        self.dt = dt
        self.max_bias = max_bias
        self.elapsed = 0.0

    def reset(self):
        self.elapsed = 0.0

    def step(self, time, thrust):
        # Apply bias slowly over time
        self.elapsed += self.dt
        if self.elapsed >= self.required_time:
            return thrust + self.max_bias
        return thrust


class InstantOverrideAttack:
    """Attack that instantly overrides actuator output at a specified start time."""

    def __init__(self, override_value, start_time):
        self.override_value = override_value
        self.start_time = start_time

    def reset(self):
        pass

    def step(self, time, thrust):
        if time >= self.start_time:
            return self.override_value
        return thrust
