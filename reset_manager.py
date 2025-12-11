# reset_manager.py

class ResetManager:
    """Manages periodic resets. In simulation, a reset re-initializes controller internal state."""

    def __init__(self, reset_interval):
        self.reset_interval = reset_interval
        self.last_reset_time = 0.0

    def should_reset(self, time):
        if self.reset_interval is None:
            return False
        return (time - self.last_reset_time) >= self.reset_interval

    def perform_reset(self, controller, drone, attack=None):
        """Perform a reset: reset controller, optionally reset attack, return downtime duration."""
        # For simplicity, assume downtime = 1 control step
        downtime = controller.dt
        controller.reset()
        drone.reset()
        if attack is not None:
            attack.reset()
        self.last_reset_time = self.last_reset_time + self.reset_interval
        return downtime
