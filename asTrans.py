import math

# Core Dimensions (in meters)
HT = 0.0254    # Height (1 inch)
ID = 0.0254    # Inside Diameter (1 inch)
OD = 0.04      # Outside Diameter (4 cm)

# Transformer Specifications
Vp = 12        # Primary Voltage (V)
Vs = 220       # Secondary Voltage (V)
P_out = 250    # Output Power (W)
f = 10_000     # Frequency (Hz)
B_max_initial = 0.2  # Initial Flux Density (T)
Kw = 0.5       # Window Utilization Factor
J = 3e6        # Current Density (A/m²)

# Core Geometry
Ae = (OD - ID) * HT  # Effective Core Area (m²)
Wa = math.pi * (ID / 2)**2  # Window Area (m²)

# Turns Calculation
Np_initial = Vp / (4.44 * f * B_max_initial * Ae)
Np = round(Np_initial)  # Round to nearest integer
B_max_actual = Vp / (4.44 * f * Np * Ae)  # Recalculate B_max
Ns = round(Np * Vs / Vp)  # Secondary Turns

# Maximum Power Capacity
P_max = 2.22 * Kw * J * B_max_actual * f * Ae * Wa

# Results
print(f"Core Geometry:")
print(f"  Effective Area (Ae): {Ae:.6f} m² ({Ae*1e4:.4f} cm²)")
print(f"  Window Area (Wa): {Wa:.6f} m² ({Wa*1e4:.4f} cm²)\n")

print(f"Turns Calculation:")
print(f"  Primary Turns (Np): {Np}")
print(f"  Adjusted B_max: {B_max_actual:.4f} T")
print(f"  Secondary Turns (Ns): {Ns}\n")

print(f"Power Handling Capacity:")
print(f"  Max Power (P_max): {P_max:.0f} W")
