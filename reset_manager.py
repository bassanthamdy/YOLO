# reset_manager.py
import time


class ResetManager:
"""Manages periodic resets. In simulation, a reset re-initializes controller internal state
and optionally stalls control for `reset_duration` seconds (simulated downtime).
"""
def __init__(self, reset_interval=1.0, reset_duration=0.02):
self.reset_interval = reset_interval
self.reset_duration = reset_duration
self.last_reset = 0.0
self.next_reset = reset_interval


def should_reset(self, t):
return t >= self.next_reset


def perform_reset(self, controller, drone, attack=None):
# reset controller internals
controller.reset()
# optional: reset drone sensors/state? we choose not to reset physical state
if attack is not None:
attack.reset()
# schedule next
self.last_reset = self.next_reset
self.next_reset += self.reset_interval
return self.reset_duration
