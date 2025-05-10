import math

# Constants
mu_0 = 4e-7 * math.pi  # Permeability of free space (H/m)

# Input Parameters (example values - adjust as needed)
N = 1                  # Number of turns
h = 10e-3               # Toroid height (m)
r_inner = 10e-3         # Inner radius (m)
r_outer = 20e-3         # Outer radius (m)
mu_r = 2000             # Relative permeability
B_max = 0.4             # Maximum flux density (T)
V_in = 12               # Input voltage (V)
R_switch = 0.75          # MOSFET switch resistance (Ω)
R_load = 200           # Load resistance (Ω)
t_switch = 200e-9       # MOSFET switching transition time (s)

# Derived Geometry
r_avg = (r_inner + r_outer) / 2
A = h * (r_outer - r_inner)  # Cross-sectional area (m²)

# 1. Calculate Inductance (L)
L = (mu_0 * mu_r * N**2 * A) / (2 * math.pi * r_avg)

# 2. Calculate Peak Current (I_peak) from Core Saturation
I_peak = (2 * math.pi * r_avg * B_max) / (mu_0 * mu_r * N)

# 3. Timing Parameters
t_on = L / R_switch          # Charging time (s)
t_off = 5 * L / R_load       # Discharging time (s)
T_sw = t_switch + t_on + t_off  # Total switching period (s)

# 4. Duty Cycle (D) and Switching Frequency (f_sw)
D = (t_switch + t_on) / T_sw
f_sw = 1 / T_sw

# 5. Output Power (P_out)
P_out = f_sw * (math.pi * r_avg * B_max**2 * A) / (mu_0 * mu_r)

# 6. Output Voltage (V_out) from P = V²/R Equation
V_out = (P_out * R_load) ** 0.5

# 7. Spike Voltage (V_spike) during MOSFET Turn-Off
delta_t = t_off  # Using discharge time as Δt
V_spike = L * (I_peak / delta_t)

# Print Results
print(f"Inductance (L): {L * 1e6:.2f} μH")
print(f"Peak Current (I_peak): {I_peak:.3f} A")
print(f"Switching Frequency (f_sw): {f_sw / 1e3:.2f} kHz")
print(f"Duty Cycle (D): {D:.3f}")
print(f"Output Voltage (V_out): {V_out:.2f} V")
print(f"Output Power (P_out): {P_out:.2f} W")
print(f"Spike Voltage (V_spike): {V_spike:.2f} V")
