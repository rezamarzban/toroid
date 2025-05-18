The **inductor current discharge equation** describes how the current through anductor decays when the energy stored in its magnetic field is released, typically in an RL (resistor-inductor) circuit. During discharge, the inductor acts as a current source, and the current decreases exponentially over time. The equation is:

$$i(t) = I_0 \cdot e^{-\frac{R}{L}t}$$

Where:  
- $i(t)$ = instantaneous current at time $t$ (in amperes),  
- $I_0$ = initial current through the inductor at $t = 0$ (in amperes),  
- $R$ = resistance in the circuit (in ohms),  
- $L$ = inductance (in henries),  
- $t$ = time (in seconds).  

This equation arises from solving the differential equation $L \frac{di}{dt} + Ri = 0$ using Kirchhoff’s Voltage Law (KVL) for a discharging RL circuit. The term $\frac{L}{R}$ is the **time constant** ($\tau$), which determines the rate of decay.  

Key points:  
1. The voltage across the inductor during discharge is governed by $v = L \frac{di}{dt}$, reflecting the inductor's opposition to changes in current.  
2. The current decays to ~36.8% of its initial value after one time constant ($\tau = \frac{L}{R}$) and approaches zero as $t \to \infty$.  
3. Discharging occurs when the inductor supplies current to the load, as described in RL circuit analysis.  

For example, if $I_0 = 1 \, \text{A}$, $R = 10 \, \Omega$, and $L = 1 \, \text{H}$, the current at $t = 0.1 \, \text{s}$ would be $i(0.1) = e^{-10 \cdot 0.1} \approx 0.368 \, \text{A}$.

To solve for $V_{\text{spike}} = -L \frac{di}{dt}$ given $i(t) = I_0 e^{-\frac{R}{L}t}$, follow these steps:

1. **Differentiate the current $i(t)$:**  
$$
\frac{di}{dt} = \frac{d}{dt} \left( I_0 e^{-\frac{R}{L}t} \right) = -\frac{R}{L} I_0 e^{-\frac{R}{L}t}.
$$
This derivative reflects the exponential decay of current in an RL circuit, consistent with solving the differential equation $L \frac{di}{dt} + Ri = 0$.

2. **Substitute $\frac{di}{dt}$ into $V_{\text{spike}}$:**  
$$
V_{\text{spike}} = -L \left( -\frac{R}{L} I_0 e^{-\frac{R}{L}t} \right) = R I_0 e^{-\frac{R}{L}t}.
$$
The negative sign in $V_{\text{spike}}$ accounts for the inductor’s back EMF opposing the change in current, resulting in a positive voltage spike during discharge.

3. **Interpretation of the result:**  
The voltage spike decays exponentially with the same time constant $\tau = \frac{L}{R}$ as the current, as noted in RL circuit analysis. At $t = 0$, $V_{\text{spike}} = R I_0$, and it decreases to ~36.8% of its initial value after one time constant ($\tau$).

**Final Answer:**  
$$V_{\text{spike}} = R I_0 e^{-\frac{R}{L}t} \quad \text{(Volts)}.$$
