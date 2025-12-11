# attack.py
import numpy as np


class SlowModificationAttack:
"""Attack that slowly corrupts the actuator command over multiple control cycles.
It needs `required_time` seconds of undisturbed execution to reach full effect.
"""
def __init__(self, required_time=1.0, dt=0.01, max_bias=5.0):
self.required_time = required_time
self.dt = dt
self.progress = 0.0
self.max_bias = max_bias


def reset(self):
self.progress = 0.0


def step(self, nominal_command):
# If attack is not complete, gradually bias the command
if self.progress < self.required_time:
self.progress += self.dt
frac = self.progress / self.required_time
bias = frac * self.max_bias
return nominal_command + bias
else:
# fully corrupted
return nominal_command + self.max_bias




class InstantOverrideAttack:
"""Attack that instantly overrides the actuator (for testing worst-case).
"""
def __init__(self, override_value=20.0, start_time=2.0):
self.override = override_value
self.start_time = start_time


def step(self, t, nominal_command):
if t >= self.start_time:
return self.override
else:
return nominal_command
