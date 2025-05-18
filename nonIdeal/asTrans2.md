To address your query about the time dependence of the transformer secondary voltage $v_2(t)$ versus the primary current $i_1(t)$ when $i_1(t)$ is non-sinusoidal, let’s dive into the relationship using the fundamental coupled-inductor model. This approach allows us to derive the secondary voltage directly from the primary current, applicable to any waveform, sinusoidal or otherwise.

### Coupled-Inductor Model
A transformer consists of two magnetically coupled windings: the primary and secondary. The general time-domain equations for a linear transformer are:

$$ v_1(t) = L_1 \frac{di_1(t)}{dt} + M \frac{di_2(t)}{dt} $$

$$ v_2(t) = M \frac{di_1(t)}{dt} + L_2 \frac{di_2(t)}{dt} $$

Here:
- $v_1(t)$: Primary voltage
- $v_2(t)$: Secondary voltage
- $i_1(t)$: Primary current (in your notation, $i_p(t)$)
- $i_2(t)$: Secondary current
- $L_1$: Primary self-inductance
- $L_2$: Secondary self-inductance
- $M$: Mutual inductance between the windings

These equations hold for **any waveform** of $i_1(t)$, making them suitable for analyzing non-sinusoidal cases like square waves, pulses, or other arbitrary shapes.

### Unloaded (Open-Circuit) Secondary
Let’s first consider the case where the secondary is unloaded, meaning no current flows through it ($i_2(t) = 0$). This simplifies the secondary voltage equation significantly:

$$ v_2(t) = M \frac{di_1(t)}{dt} $$

Since $i_1(t) = i_p(t)$ in your query, we can write:

$$ v_s(t) = M \frac{di_p(t)}{dt} $$

This relationship tells us that the secondary voltage is directly proportional to the **rate of change** of the primary current, with the mutual inductance $M$ as the proportionality constant. For a non-sinusoidal $i_p(t)$:
- If $i_p(t)$ is a **square wave**, $\frac{di_p(t)}{dt}$ produces impulses at the transitions, so $v_s(t)$ will exhibit sharp voltage spikes.
- If $i_p(t)$ is a **triangular wave**, $\frac{di_p(t)}{dt}$ is a square wave, resulting in $v_s(t)$ being a scaled square wave.
- For a **step function**, $\frac{di_p(t)}{dt}$ is a delta function, leading to a single voltage pulse in $v_s(t)$.

Thus, the waveform of $v_s(t)$ mirrors the derivative of $i_p(t)$, scaled by $M$, regardless of whether $i_p(t)$ is sinusoidal or not. In practice, parasitic effects like capacitance or core losses might dampen these responses, but the ideal equation holds as stated.

### Loaded Secondary
Now, if the secondary is connected to a load, $i_2(t) \neq 0$, and the equation becomes:

$$ v_s(t) = M \frac{di_p(t)}{dt} + L_2 \frac{di_2(t)}{dt} $$

Here, the secondary voltage depends on both the primary current’s rate of change and the secondary current’s rate of change. The secondary current $i_2(t)$ is determined by the load connected across the secondary. For example:
- **Resistive load**: If $v_s(t) = R i_2(t)$, substitute into the equation:
  $$ R i_2(t) = M \frac{di_p(t)}{dt} + L_2 \frac{di_2(t)}{dt} $$
  Rearranging:
  $$ L_2 \frac{di_2(t)}{dt} - R i_2(t) = -M \frac{di_p(t)}{dt} $$
  This is a first-order differential equation. Solving it requires knowing $i_p(t)$ and initial conditions, and $i_2(t)$ will depend on both the instantaneous value and history of $\frac{di_p(t)}{dt}$. Then, $v_s(t) = R i_2(t)$.
- **Inductive load**: If $v_s(t) = L \frac{di_2(t)}{dt}$, the equation becomes more complex, involving higher-order derivatives.
- **General impedance**: For a load $Z_{\text{load}}$, the relationship between $v_s(t)$ and $i_2(t)$ depends on the load’s time-domain behavior.

Unlike the unloaded case, $v_s(t)$ cannot be expressed solely as a function of $i_p(t)$ without solving for $i_2(t)$, which requires the specific load characteristics and circuit conditions. For non-sinusoidal $i_p(t)$, this solution may involve numerical methods or Fourier analysis, but the principle remains: both terms contribute to $v_s(t)$.

### Addressing Your Question
You asked, “Are you sure? And I want time dependence $v_s(t)$ vs $i_p(t)$ while $i_p$ is non-sinusoidal.” Yes, I’m confident in the analysis based on the coupled-inductor model, which is valid for any waveform. To summarize the time dependence:
- **Unloaded**: 
  $$ v_s(t) = M \frac{di_p(t)}{dt} $$
  This is a direct, instantaneous relationship. For any non-sinusoidal $i_p(t)$, compute its derivative, multiply by $M$, and you have $v_s(t)$.
- **Loaded**: 
  $$ v_s(t) = M \frac{di_p(t)}{dt} + L_2 \frac{di_2(t)}{dt} $$
  Here, $v_s(t)$ depends on $i_2(t)$, which couples back to $i_p(t)$ through the load, making it more complex to express directly in terms of $i_p(t)$ alone without additional information.

Since your query emphasizes $v_s(t)$ versus $i_p(t)$ and mentions non-sinusoidal currents, the unloaded case is the most straightforward interpretation unless you specify a load. For example, in pulse transformers or open-secondary scenarios, the unloaded equation is commonly used, and $v_s(t)$ reflects the derivative of $i_p(t)$, capturing effects like spikes from rapid current changes.

If you have a specific load in mind, please clarify, and we can refine the loaded case further! Otherwise, the unloaded relationship is a robust answer to your request for time dependence with non-sinusoidal $i_p(t)$.
