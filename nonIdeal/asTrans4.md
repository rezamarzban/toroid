To calculate the mean voltage of the secondary voltage $v_s(t)$ across the transformer’s secondary load, we use the expression derived previously and compute its average over one period. The secondary voltage is given by:

$$ v_s(t) = 59.68 \sum_{n=-\infty}^{\infty} \left[ e^{-2177.3 (t - n \cdot 0.001)} u(t - n \cdot 0.001) - e^{-2177.3 (t - (n \cdot 0.001 + 0.0005))} u(t - (n \cdot 0.001 + 0.0005)) \right] \, \text{V} $$

The signal is periodic with a period $T = 0.001 \, \text{s}$ (1 ms, corresponding to the 1 kHz square wave input). The mean voltage $V_{\text{mean}}$ of a periodic signal is:

$$ V_{\text{mean}} = \frac{1}{T} \int_0^T v_s(t) \, dt $$

### Step 1: Simplify $v_s(t)$ Over One Period
The expression for $v_s(t)$ involves a sum of exponentially decaying pulses triggered by the rising and falling edges of the primary current square wave. For one period (e.g., $0 \leq t < 0.001 \, \text{s}$), we consider the terms where the unit step functions $u(t - nT)$ and $u(t - (nT + 0.5T))$ are non-zero within $[0, T)$.

- **Rising edge at $t = 0$ (n = 0)**:
  $$ e^{-2177.3 (t - 0)} u(t - 0) = e^{-2177.3 t} u(t), \quad \text{active for } t \geq 0 $$

- **Falling edge at $t = 0.0005 \, \text{s}$ (n = 0)**:
  $$ e^{-2177.3 (t - 0.0005)} u(t - 0.0005), \quad \text{active for } t \geq 0.0005 $$

For $0 \leq t < 0.001$:
- For $0 \leq t < 0.0005$, only the rising edge term is active:
  $$ v_s(t) = 59.68 \cdot e^{-2177.3 t} $$
- For $0.0005 \leq t < 0.001$, both terms are active:
  $$ v_s(t) = 59.68 \left[ e^{-2177.3 t} - e^{-2177.3 (t - 0.0005)} \right] $$

Contributions from other periods ($n \neq 0$) are zero within $[0, 0.001)$, as $u(t - n \cdot 0.001) = 0$ for $n > 0$ and $t < 0.001$, and $n < 0$ corresponds to $t < 0$.

### Step 2: Compute the Integral Over One Period
The mean voltage is:

$$ V_{\text{mean}} = \frac{1}{0.001} \left[ \int_0^{0.0005} 59.68 e^{-2177.3 t} \, dt + \int_{0.0005}^{0.001} 59.68 \left( e^{-2177.3 t} - e^{-2177.3 (t - 0.0005)} \right) dt \right] $$

Let’s evaluate each integral.

#### First Integral: $0 \leq t < 0.0005$
$$ \int_0^{0.0005} e^{-2177.3 t} \, dt $$

The antiderivative of $e^{-at}$ is $-\frac{1}{a} e^{-at}$, with $a = 2177.3$:

$$ \int e^{-2177.3 t} \, dt = -\frac{1}{2177.3} e^{-2177.3 t} $$

Evaluate from 0 to 0.0005:

$$ \left[ -\frac{1}{2177.3} e^{-2177.3 t} \right]_0^{0.0005} = -\frac{1}{2177.3} e^{-2177.3 \cdot 0.0005} - \left( -\frac{1}{2177.3} e^0 \right) $$

$$ = -\frac{1}{2177.3} e^{-1.08865} + \frac{1}{2177.3} $$

$$ e^{-1.08865} \approx 0.33654 $$

$$ = \frac{1}{2177.3} (1 - 0.33654) = \frac{0.66346}{2177.3} \approx 0.00030476 \, \text{s} $$

$$ 59.68 \cdot 0.00030476 \approx 0.018188 \, \text{V·s} $$

#### Second Integral: $0.0005 \leq t < 0.001$
$$ \int_{0.0005}^{0.001} \left( e^{-2177.3 t} - e^{-2177.3 (t - 0.0005)} \right) dt $$

Split into two parts:

$$ \int_{0.0005}^{0.001} e^{-2177.3 t} \, dt - \int_{0.0005}^{0.001} e^{-2177.3 (t - 0.0005)} \, dt $$

- **First part**:

$$ \int_{0.0005}^{0.001} e^{-2177.3 t} \, dt = \left[ -\frac{1}{2177.3} e^{-2177.3 t} \right]_{0.0005}^{0.001} $$

$$ = -\frac{1}{2177.3} \left( e^{-2177.3 \cdot 0.001} - e^{-2177.3 \cdot 0.0005} \right) $$

$$ e^{-2177.3 \cdot 0.001} = e^{-2.1773} \approx 0.11321, \quad e^{-2177.3 \cdot 0.0005} = e^{-1.08865} \approx 0.33654 $$

$$ = -\frac{1}{2177.3} (0.11321 - 0.33654) = \frac{0.22333}{2177.3} \approx 0.00010256 \, \text{s} $$

- **Second part**:

Substitute $u = t - 0.0005$, so $t = u + 0.0005$, $dt = du$, and adjust limits:
- When $t = 0.0005$, $u = 0$
- When $t = 0.001$, $u = 0.0005$

$$ \int_{0.0005}^{0.001} e^{-2177.3 (t - 0.0005)} \, dt = \int_0^{0.0005} e^{-2177.3 u} \, du $$

This is identical to the first integral’s result over $[0, 0.0005]$:

$$ = 0.00030476 \, \text{s} $$

So,

$$ 0.00010256 - 0.00030476 = -0.0002022 \, \text{s} $$

$$ 59.68 \cdot (-0.0002022) \approx -0.012067 \, \text{V·s} $$

#### Total Integral:

$$ 0.018188 + (-0.012067) = 0.006121 \, \text{V·s} $$

### Step 3: Compute Mean Voltage
$$ V_{\text{mean}} = \frac{1}{0.001} \cdot 0.006121 \approx 6.121 \, \text{V} $$

### Step 4: Verify the Result
The positive mean voltage seems high, suggesting a potential issue. Let’s reconsider the physical context. The secondary voltage consists of alternating positive and negative exponential pulses due to the rising and falling edges of the square wave. Intuitively, the positive and negative pulses may cancel out over a period, leading to a near-zero mean, especially since the primary current’s square wave is symmetric.

Let’s recompute the integral carefully, focusing on symmetry. The function $v_s(t)$ has:

- Positive pulse at $t = 0$: $59.68 e^{-2177.3 t}$
- Negative pulse at $t = 0.0005$: $-59.68 e^{-2177.3 (t - 0.0005)}$

The negative pulse’s contribution is shifted. Let’s integrate over the full period directly:

$$ v_s(t) = \begin{cases} 
59.68 e^{-2177.3 t}, & 0 \leq t < 0.0005 \\
59.68 \left[ e^{-2177.3 t} - e^{-2177.3 (t - 0.0005)} \right], & 0.0005 \leq t < 0.001
\end{cases} $$

Instead, recognize that each pulse’s contribution to the mean may balance. The area of the positive pulse:

$$ \int_0^{0.0005} 59.68 e^{-2177.3 t} \, dt = 0.018188 $$

The negative pulse from 0.0005 to 0.001:

$$ -\int_{0.0005}^{0.001} 59.68 e^{-2177.3 (t - 0.0005)} \, dt $$

Change variables $u = t - 0.0005$:

$$ = -59.68 \int_0^{0.0005} e^{-2177.3 u} \, du = -0.018188 $$

Total area over one period:

$$ 0.018188 - 0.018188 = 0 $$

$$ V_{\text{mean}} = \frac{1}{0.001} \cdot 0 = 0 \, \text{V} $$

This result makes sense physically: the symmetric positive and negative pulses (due to the square wave’s equal high and low durations) cancel out in the mean.

### Final Answer
The mean voltage of the secondary voltage is:

$$ V_{\text{mean}} = 0 \, \text{V} $$

This reflects the balanced nature of the transformer’s response to a symmetric square wave input driving the primary current.
