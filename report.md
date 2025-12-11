# YOLO: Frequently Resetting Cyber-Physical Systems for Security


## 1. Introduction
This project implements a simplified demonstration of the YOLO defense mechanism: frequently resetting the cyber components of a cyber-physical system (a drone) to limit attacker dwell time. We build a 1D altitude control simulation and an attacker model that requires time to corrupt actuator commands. The goal is to study the trade-off between security (attack mitigation) and safety (control stability) as reset frequency increases.


## 2. Background
(Short literature summary... mention YOLO paper and relevant CPS security concepts.)


## 3. System Model
- Drone: 1D vertical dynamics, mass m, gravity g.
- Controller: PID controlling thrust to track altitude.
- Reset model: periodic software resets that clear controller internals and reset attack progress; resets cause a short downtime where controller outputs are not updated.
- Attack model: slow-modification attack with required dwell time to reach full effect; instant override as worst-case.


## 4. Implementation
Describe the Python modules and simulation parameters (dt, PID gains, reset durations).


## 5. Experiments
List experiments: no reset, 2s, 1s, 0.5s, 0.2s with each attack type.


## 6. Results
Include plots saved in `results/` and quantitative tabl
