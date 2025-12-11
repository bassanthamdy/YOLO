# drone_sim.py

class Drone:
    """A simplified 1D vertical dynamics model (altitude) with a PID controller."""

    def __init__(self):
        self.z = 0.0   # altitude
        self.v = 0.0   # vertical velocity
        self.m = 1.0   # mass
        self.g = 9.81  # gravity
        self.dt = 0.01

    def reset(self):
        """Reset drone state"""
        self.z = 0.0
        self.v = 0.0

    def dynamics_step(self, thrust):
        """Compute next state given thrust"""
        # simple vertical dynamics: a = (thrust - mg)/m
        a = (thrust - self.m * self.g) / self.m
        self.v += a * self.dt
        self.z += self.v * self.dt
        return self.z, self.v
