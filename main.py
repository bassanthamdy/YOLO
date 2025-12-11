# main.py
t = np.zeros(t_steps)
z_log = np.zeros(t_steps)
v_log = np.zeros(t_steps)
thrust_log = np.zeros(t_steps)
setpoint_log = np.zeros(t_steps)


setpoint = 1.0 # target altitude
drone.reset(); controller.reset();
if attack is not None:
attack.reset()


i = 0
time = 0.0
while i < t_steps:
if reset_mgr.should_reset(time):
# simulate downtime: controller reset, attack reset
downtime = reset_mgr.perform_reset(controller, drone, attack)
# advance time during downtime without control (open-loop)
# we keep thrust = 0 during downtime for simplicity
nskip = int(downtime / dt)
for _ in range(nskip):
z, v = drone.dynamics_step(0.0)
t[i] = time; z_log[i]=z; v_log[i]=v; thrust_log[i]=0.0; setpoint_log[i]=setpoint
time += dt; i+=1
if i>=t_steps: break
if i>=t_steps: break


# normal control
# measurement with small sensor noise
meas = drone.z + np.random.randn()*0.001
u = controller.compute(setpoint, meas)
# map u -> thrust (saturate)
thrust = max(0.0, min(30.0, u))


if attack is not None:
# attack modifies thrust depending on attack model
if hasattr(attack, 'step'):
# two kinds of step signatures supported
try:
thrust = attack.step(time, thrust)
except TypeError:
thrust = attack.step(thrust)


z, v = drone.dynamics_step(thrust)
t[i]=time; z_log[i]=z; v_log[i]=v; thrust_log[i]=thrust; setpoint_log[i]=setpoint
time += dt; i+=1


# compute RMSE of altitude vs setpoint
valid = ~np.isnan(z_log[:i])
rm = rmse(z_log[:i], setpoint_log[:i])
return t[:i], z_log[:i], thrust_log[:i], setpoint_log[:i], rm




if __name__ == '__main__':
reset_intervals = [None, 2.0, 1.0, 0.5, 0.2]
attacks = {
'none': None,
'slow': SlowModificationAttack(required_time=1.0, dt=0.01, max_bias=6.0),
'instant': InstantOverrideAttack(override_value=25.0, start_time=2.0)
}


for a_name, a_obj in attacks.items():
for ri in reset_intervals:
label = f'{a_name}_reset_{ri}'
print('Running', label)
if ri is None:
# simulate no resets: set a very large interval
ri_val = 1e9
else:
ri_val = ri
t,z,th,setp,rm = run_experiment(reset_interval=ri_val, attack=a_obj)
fname = os.path.join(RESULTS_DIR, f'{label}_altitude.png')
plot_time_series(t, [z, setp], ['altitude','setpoint'], f'{label} (RMSE={rm:.3f})', fname=fname)
print('Saved', fname)
