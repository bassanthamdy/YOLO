import numpy as np


class SimpleDrone:
"""A simplified 1D vertical dynamics model (altitude) with a PID controller.
State: z (altitude), v (vertical velocity)
Control: thrust force (mapped to acceleration)
"""
def __init__(self, mass=1.0, dt=0.01):
self.m = mass
self.g = 9.81
self.dt = dt
self.reset()


def reset(self):
self.z = 0.0
self.v = 0.0
self.time = 0.0


def dynamics_step(self, thrust):
# thrust is a force in N upward
a = (thrust - self.m * self.g) / self.m
# simple Euler integration
self.v += a * self.dt
self.z += self.v * self.dt
self.time += self.dt
return self.z, self.v




class PIDController:
def __init__(self, kp=12.0, ki=1.0, kd=3.0, dt=0.01, integrator_limit=10.0):
self.kp = kp
self.ki = ki
self.kd = kd
self.dt = dt
self.integrator = 0.0
self.prev_error = 0.0
self.integrator_limit = integrator_limit


def reset(self):
self.integrator = 0.0
self.prev_error = 0.0


def compute(self, setpoint, measurement):
error = setpoint - measurement
self.integrator += error * self.dt
# anti-windup
self.integrator = max(min(self.integrator, self.integrator_limit), -self.integrator_limit)
derivative = (error - self.prev_error) / self.dt
self.prev_error = error
u = self.kp * error + self.ki * self.integrator + self.kd * derivative
return u
