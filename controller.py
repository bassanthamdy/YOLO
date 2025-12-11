# controller.py

class Controller:
    """Simple PID controller for altitude"""

    def __init__(self, dt, kp=10.0, ki=0.5, kd=2.0):
        self.dt = dt
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.integral = 0.0
        self.prev_error = 0.0

    def reset(self):
        self.integral = 0.0
        self.prev_error = 0.0

    def compute(self, setpoint, measurement):
        error = setpoint - measurement
        self.integral += error * self.dt
        derivative = (error - self.prev_error) / self.dt
        self.prev_error = error
        u = self.kp * error + self.ki * self.integral + self.kd * derivative
        return u
