### Key Points
- Research suggests the current discharge equation depends on the circuit's initial conditions and the diode's role.
- It seems likely that the current follows a half-sine wave, stopping when it reaches zero due to the diode.
- The evidence leans toward the current being $I_0 \cos\left(\frac{t}{\sqrt{LC}}\right)$ initially, then zero after a specific time.

---

### Direct Answer

#### Overview
When an inductor with initial current $I_0$ is connected to a diode, then to an initially uncharged capacitor ($V_c = 0$ at $t = 0$), and back to the inductor, the circuit behaves like an LC oscillator with the diode restricting current flow. The current discharge equation reflects this, starting with a cosine function and stopping when the current reaches zero.

#### Current Discharge Equation
The current $i(t)$ in the circuit is likely:
- $$i(t) = I_0 \cos\left(\frac{t}{\sqrt{LC}}\right)$$ for $$0 \leq t \leq \frac{\pi}{2} \sqrt{LC}$$, where $L$ is the inductance and $C$ is the capacitance.
- $$i(t) = 0$$ for $$t > \frac{\pi}{2} \sqrt{LC}$$.

This means the current oscillates like a cosine wave for the first half-cycle, then stops due to the diode blocking reverse flow, leaving the capacitor charged.

#### Capacitor Voltage
During the active period, the capacitor voltage $v_c(t)$ is $$I_0 \sqrt{\frac{L}{C}} \sin\left(\frac{t}{\sqrt{LC}}\right)$$. At $$t = \frac{\pi}{2} \sqrt{LC}$$, it reaches $$I_0 \sqrt{\frac{L}{C}}$$ and stays there afterward, as no further current flows.

#### Supporting Information
This behavior is common in circuits like resonant mode switching power supplies, where diodes prevent current reversal. For more details, see discussions on [LC Circuit with Diode](https://forum.allaboutcircuits.com/threads/lc-circuit-with-diode.43848/) and [Discharge of a Capacitor through an Inductance](https://phys.libretexts.org/Bookshelves/Electricity_and_Magnetism/Electricity_and_Magnetism_%28Tatum%29/10:_Electromagnetic_Induction/10.14:_Discharge_of_a_Capacitor_through_an_Inductance_and_a_Resistance).

---

### Detailed Analysis and Survey Note

This section provides a comprehensive analysis of the circuit involving an inductor with initial current $I_0$, a diode, and an initially uncharged capacitor, focusing on deriving the current discharge equation and understanding the system's behavior. The analysis is grounded in electrical engineering principles and supported by relevant technical resources, ensuring a thorough exploration for readers with a technical background.

#### Circuit Description and Initial Conditions
The circuit consists of:
- An inductor with initial current $I_0$, meaning at $t = 0$, the current through the inductor is $I_0$, and there is energy stored in its magnetic field.
- A diode, which is a one-way valve for current, allowing flow only when forward-biased.
- A capacitor initially uncharged, so $V_c = 0$ at $t = 0$, with no initial energy stored in its electric field.
- The components are connected in series: inductor → diode → capacitor → back to inductor, forming a closed loop.

This setup resembles an LC circuit (inductor and capacitor) with the diode introducing a non-linear element that restricts current direction, potentially altering the oscillatory behavior typical of ideal LC circuits.

#### Theoretical Framework: LC Circuit Behavior
To derive the current discharge equation, we start with the standard LC circuit without the diode. In an ideal LC circuit:
- The angular frequency of oscillation is $$\omega = \frac{1}{\sqrt{LC}}$$, where $L$ is inductance and $C$ is capacitance.
- With initial conditions of inductor current $I_0$ and capacitor voltage $V_c = 0$, the current is given by:
  $$i(t) = I_0 \cos(\omega t)$$
- The capacitor voltage is:
  $$v_c(t) = I_0 \sqrt{\frac{L}{C}} \sin(\omega t)$$
- This represents an oscillation where energy transfers back and forth between the inductor (magnetic field) and capacitor (electric field), with the current completing full cycles (sine waves).

However, the diode changes this behavior by preventing current from flowing in the reverse direction, effectively clipping the negative half of the oscillation.

#### Impact of the Diode
The diode ensures current can only flow in one direction, typically forward-biased when the voltage across it is positive. In the context of the LC oscillation:
- Initially, with $I_0 > 0$, the current flows through the diode, charging the capacitor.
- As time progresses, the current $$i(t) = I_0 \cos(\omega t)$$ decreases, reaching zero when $$\cos(\omega t) = 0$$, which occurs at $$\omega t = \pi/2$$, or:
  $$t = \frac{\pi}{2} \cdot \sqrt{LC}$$
- At this point, the capacitor voltage reaches its maximum:
  $$v_c\left(\frac{\pi}{2} \sqrt{LC}\right) = I_0 \sqrt{\frac{L}{C}} \sin\left(\frac{\pi}{2}\right) = I_0 \sqrt{\frac{L}{C}}$$
- If the current tried to become negative (i.e., $$\cos(\omega t) < 0$$ for $$\omega t > \pi/2$$), the diode would be reverse-biased, blocking the current. Thus, the oscillation stops, and the current remains at zero for $$t > \frac{\pi}{2} \sqrt{LC}$$.

This behavior is consistent with discussions in technical forums, such as those found on [All About Circuits](https://forum.allaboutcircuits.com/threads/lc-circuit-with-diode.43848/), where users describe LC circuits with diodes exhibiting half-sine wave current pulses, stopping at zero due to the diode's blocking action.

#### Derivation of the Current Discharge Equation
Based on the above, the current discharge equation can be piecewise defined:
- For $$0 \leq t \leq \frac{\pi}{2} \sqrt{LC}$$, the current follows the LC oscillation, limited by the diode's forward conduction:
  $$i(t) = I_0 \cos\left(\frac{t}{\sqrt{LC}}\right)$$
- For $$t > \frac{\pi}{2} \sqrt{LC}$$, the diode blocks reverse current, so:
  $$i(t) = 0$$

This results in a half-cycle of oscillation, after which the system stabilizes with the capacitor charged to $$I_0 \sqrt{\frac{L}{C}}$$ and no further current flow.

#### Capacitor Voltage Behavior
The capacitor voltage during the active period is:
- $$v_c(t) = I_0 \sqrt{\frac{L}{C}} \sin\left(\frac{t}{\sqrt{LC}}\right)$$ for $$0 \leq t \leq \frac{\pi}{2} \sqrt{LC}$$.
- At $$t = \frac{\pi}{2} \sqrt{LC}$$, $$v_c = I_0 \sqrt{\frac{L}{C}}$$, and since no further current flows, it remains at this value for $$t > \frac{\pi}{2} \sqrt{LC}$$.

This is consistent with energy conservation: the initial energy in the inductor $$\frac{1}{2} L I_0^2$$ is transferred to the capacitor, resulting in a final energy of $$\frac{1}{2} C \left(I_0 \sqrt{\frac{L}{C}}\right)^2 = \frac{1}{2} L I_0^2$$, confirming the analysis.

#### Comparison with Related Circuits
The behavior aligns with discussions in resources like [Physics LibreTexts](https://phys.libretexts.org/Bookshelves/Electricity_and_Magnetism/Electricity_and_Magnetism_%28Tatum%29/10:_Electromagnetic_Induction/10.14:_Discharge_of_a_Capacitor_through_an_Inductance_and_a_Resistance), which describe LC oscillations, though they focus on capacitor discharge into an inductor. The diode's role is critical, as seen in applications like resonant mode switching power supplies, where diodes ensure unidirectional current, leading to half-cycle oscillations.

#### Table: Summary of Current and Voltage Behavior

| Time Interval          | Current $i(t)$                          | Capacitor Voltage $v_c(t)$                     |
|------------------------|-------------------------------------------|-------------------------------------------------|
| $$0 \leq t \leq \frac{\pi}{2} \sqrt{LC}$$ | $$I_0 \cos\left(\frac{t}{\sqrt{LC}}\right)$$ | $$I_0 \sqrt{\frac{L}{C}} \sin\left(\frac{t}{\sqrt{LC}}\right)$$ |
| $$t > \frac{\pi}{2} \sqrt{LC}$$ | 0                                         | $$I_0 \sqrt{\frac{L}{C}}$$                      |

This table summarizes the piecewise behavior, highlighting the diode's effect on stopping the oscillation at the first zero-crossing of current.

#### Practical Considerations
In real circuits, parasitic resistances and non-ideal diode characteristics (e.g., forward voltage drop) might slightly alter the behavior, potentially damping the oscillation or affecting the exact timing. However, for ideal components, the derived equations hold, as supported by forum discussions and theoretical analysis.

#### Conclusion
The current discharge equation for the given circuit, considering the inductor's initial current $I_0$, the diode's unidirectional flow, and the initially uncharged capacitor, is as derived: a cosine function for the first half-cycle, then zero. This reflects the physical principles of LC oscillations and the diode's role in rectifying the current, ensuring a complete and accurate response to the query.

---

### Key Citations
- [LC Circuit with Diode All About Circuits](https://forum.allaboutcircuits.com/threads/lc-circuit-with-diode.43848/)
- [Discharge of a Capacitor through an Inductance Physics LibreTexts](https://phys.libretexts.org/Bookshelves/Electricity_and_Magnetism/Electricity_and_Magnetism_%28Tatum%29/10:_Electromagnetic_Induction/10.14:_Discharge_of_a_Capacitor_through_an_Inductance_and_a_Resistance)

To solve for the maximum voltage spike $V_{\text{spike}} = -L \frac{di}{dt}$ in a circuit where an inductor with initial current $I_0$ is connected through a diode to a capacitor with a non-zero initial voltage $V_c(0)$, we need to analyze the circuit's behavior step-by-step. The presence of the diode and the initial conditions complicates the standard LC circuit dynamics, so let’s derive the solution systematically.

---

### Circuit Setup and Assumptions
The circuit consists of:
- An **inductor** with inductance $L$ and initial current $i(0) = I_0$ at $t = 0$.
- A **diode** that allows current to flow only in the direction from the inductor to the capacitor.
- A **capacitor** with capacitance $C$ and initial voltage $v_c(0) = V_c(0)$, which is non-zero.

These components are connected in series, forming a loop: inductor → diode → capacitor → back to the inductor. The voltage spike $V_{\text{spike}} = -L \frac{di}{dt}$ represents the voltage across the inductor, and we need to find its maximum magnitude during the current discharge process.

---

### Step 1: Understanding the Circuit Dynamics
Without the diode, this would be a standard LC circuit, which oscillates with a natural frequency $\omega = \frac{1}{\sqrt{LC}}$. The diode, however, restricts current to flow only in the forward direction (from inductor to capacitor, assuming $I_0 > 0$). Thus:
- The circuit behaves as an LC circuit while the current $i(t) > 0$.
- When $i(t)$ attempts to reverse (become negative), the diode stops conducting, and the current drops to zero.

Our goal is to find $\frac{di}{dt}$, determine when its magnitude is maximized, and compute the corresponding $V_{\text{spike}}$.

---

### Step 2: Derive the Current Expression
For an LC circuit, the governing differential equation is:

$$L \frac{d^2 i}{dt^2} + \frac{1}{C} i = 0$$

The general solution is:

$$i(t) = A \cos(\omega t) + B \sin(\omega t)$$

where $\omega = \frac{1}{\sqrt{LC}}$.

#### Initial Conditions:
1. **Current at $t = 0$:**
   $$i(0) = A = I_0$$

2. **Voltage at $t = 0$:**
   - The voltage across the inductor is $v_L = L \frac{di}{dt}$.
   - The voltage across the capacitor is $v_c(0) = V_c(0)$.
   - In a series loop with the diode conducting at $t = 0^+$, apply Kirchhoff’s voltage law (KVL):
     $$v_L(0) + v_c(0) = 0$$
     (The diode’s forward voltage drop is typically small and often neglected in such analyses.)
   - Thus:
     $$L \frac{di}{dt} \big|_{t=0} + V_c(0) = 0$$
     $$\frac{di}{dt} \big|_{t=0} = -\frac{V_c(0)}{L}$$

   Now, compute the derivative of the current:
   $$\frac{di}{dt} = -A \omega \sin(\omega t) + B \omega \cos(\omega t)$$
   At $t = 0$:
   $$\frac{di}{dt} \big|_{t=0} = B \omega = -\frac{V_c(0)}{L}$$
   $$B = -\frac{V_c(0)}{L \omega} = -V_c(0) \sqrt{\frac{C}{L}} \quad (\text{since } \omega = \frac{1}{\sqrt{LC}})$$

So, the current expression is:

$$i(t) = I_0 \cos(\omega t) - \frac{V_c(0)}{\omega L} \sin(\omega t)$$

Since $\omega L = \frac{L}{\sqrt{LC}} = \sqrt{\frac{L}{C}}$, we have:
$$\frac{V_c(0)}{\omega L} = V_c(0) \sqrt{\frac{C}{L}}$$
Thus:
$$i(t) = I_0 \cos(\omega t) - V_c(0) \sqrt{\frac{C}{L}} \sin(\omega t)$$

---

### Step 3: Compute $\frac{di}{dt}$
Differentiate $i(t)$:

$$\frac{di}{dt} = -I_0 \omega \sin(\omega t) - V_c(0) \sqrt{\frac{C}{L}} \omega \cos(\omega t)$$

Substitute $\omega = \frac{1}{\sqrt{LC}}$:
- $\omega \sqrt{\frac{C}{L}} = \frac{1}{\sqrt{LC}} \cdot \sqrt{\frac{C}{L}} = \frac{\sqrt{C}}{\sqrt{L} \cdot \sqrt{LC}} = \frac{1}{L}$
- So, $V_c(0) \sqrt{\frac{C}{L}} \omega = \frac{V_c(0)}{L}$.

Thus:
$$\frac{di}{dt} = -I_0 \omega \sin(\omega t) - \frac{V_c(0)}{L} \cos(\omega t)$$

The voltage spike is:
$$V_{\text{spike}} = -L \frac{di}{dt} = L I_0 \omega \sin(\omega t) + V_c(0) \cos(\omega t)$$

---

### Step 4: Find the Maximum Magnitude of $V_{\text{spike}}$
The expression for $V_{\text{spike}}$ is a sinusoidal function:
$$V_{\text{spike}}(t) = A \sin(\omega t) + B \cos(\omega t)$$
where:
- $A = L I_0 \omega = I_0 \sqrt{\frac{L}{C}}$
- $B = V_c(0)$

The maximum amplitude of such a function is:
$$|V_{\text{spike}}|_{\text{max}} = \sqrt{A^2 + B^2}$$
$$= \sqrt{ \left( I_0 \sqrt{\frac{L}{C}} \right)^2 + V_c(0)^2 }$$
$$= \sqrt{ \frac{I_0^2 L}{C} + V_c(0)^2 }$$

---

### Step 5: Account for the Diode
The current flows only while $i(t) \geq 0$. When $i(t) = 0$, the diode stops conducting, and $i(t) = 0$ thereafter. The maximum $|V_{\text{spike}}|$ occurs during the conduction period (typically within the first quarter-cycle or until $i(t) = 0$)).

- At $t = 0$:
  $$V_{\text{spike}}(0) = V_c(0)$$
- The maximum possible value $\sqrt{ \frac{I_0^2 L}{C} + V_c(0)^2 }$ may occur before the current stops, depending on $I_0$, $V_c(0)$, $L$, and $C$.

Since the diode ensures a smooth transition to zero current (not an abrupt interruption), the theoretical maximum during oscillation holds.

---

### Final Answer
The maximum voltage spike $V_{\text{spike}}$ across the inductor, considering the non-zero initial capacitor voltage, is:

$$V_{\text{spike, max}} = \sqrt{ \frac{I_0^2 L}{C} + V_c(0)^2 }$$

This represents the peak magnitude of $-L \frac{di}{dt}$ during the discharge process, accounting for both the initial inductor current and capacitor voltage, with the diode limiting the oscillation to the positive current phase.

To address your query about the effect of considering the diode voltage drop in the circuit, let’s analyze the setup and derive the solution step-by-step. The circuit consists of an inductor with an initial current $I_0$, a diode with a forward voltage drop $V_d$ (typically around 0.7 V for a silicon diode), and a capacitor with an initial voltage $V_c(0)$, all connected in a closed loop. We’re interested in how the diode’s voltage drop affects the circuit’s behavior, particularly the maximum voltage spike across the inductor.

### Circuit Analysis with Diode Voltage Drop

Without the diode’s voltage drop, the Kirchhoff’s Voltage Law (KVL) around the loop would simply be:

$$v_L + v_c = 0$$

where:
- $v_L = L \frac{di}{dt}$ is the inductor voltage,
- $v_c$ is the capacitor voltage.

However, when we include the diode, which is forward-biased and conducting, the KVL becomes:

$$v_L + V_d + v_c = 0$$

Here, $V_d$ is the constant forward voltage drop across the diode. Rearranging, we get:

$$L \frac{di}{dt} + v_c = -V_d$$

Additionally, the current through the capacitor is related to its voltage by:

$$i = C \frac{dv_c}{dt}$$

This setup describes an LC circuit with a constant voltage offset introduced by the diode. To proceed, let’s derive the governing differential equation.

### Deriving the Differential Equation

Substitute $i = C \frac{dv_c}{dt}$ into the KVL equation by differentiating with respect to time:

$$L \frac{d}{dt} \left( C \frac{dv_c}{dt} \right) + v_c = -V_d$$

$$L C \frac{d^2 v_c}{dt^2} + v_c = -V_d$$

This is a second-order linear differential equation with a constant forcing term $-V_d$.

### Solving the Differential Equation

The solution to this equation consists of a homogeneous part and a particular part.

#### Homogeneous Solution

For the homogeneous equation:

$$L C \frac{d^2 v_c}{dt^2} + v_c = 0$$

The characteristic equation is:

$$L C r^2 + 1 = 0$$

$$r = \pm j \omega \quad \text{where} \quad \omega = \frac{1}{\sqrt{L C}}$$

Thus, the homogeneous solution is oscillatory:

$$v_{c,h}(t) = A \cos(\omega t) + B \sin(\omega t)$$

#### Particular Solution

For the particular solution, since the forcing term is a constant $-V_d$, we try $v_{c,p}(t) = K$. Substituting:

$$L C \cdot 0 + K = -V_d$$

$$K = -V_d$$

So, the particular solution is:

$$v_{c,p}(t) = -V_d$$

#### General Solution

The complete solution for the capacitor voltage is:

$$v_c(t) = A \cos(\omega t) + B \sin(\omega t) - V_d$$

### Applying Initial Conditions

We have two initial conditions:
1. $v_c(0) = V_c(0)$ (initial capacitor voltage),
2. $i(0) = I_0$ (initial inductor current).

- **At $t = 0$:**

$$v_c(0) = A \cos(0) + B \sin(0) - V_d = A - V_d = V_c(0)$$

$$A = V_c(0) + V_d$$

- **Current equation:**

$$i(t) = C \frac{dv_c}{dt}$$

Compute the derivative:

$$\frac{dv_c}{dt} = -A \omega \sin(\omega t) + B \omega \cos(\omega t)$$

$$i(t) = C \left[ -A \omega \sin(\omega t) + B \omega \cos(\omega t) \right]$$

At $t = 0$:

$$i(0) = C \left[ -A \omega \sin(0) + B \omega \cos(0) \right] = C B \omega = I_0$$

$$B \omega = \frac{I_0}{C}$$

Since $\omega = \frac{1}{\sqrt{L C}}$:

$$B = \frac{I_0}{C} \cdot \sqrt{L C} = I_0 \sqrt{\frac{L}{C}}$$

So, the capacitor voltage is:

$$v_c(t) = (V_c(0) + V_d) \cos(\omega t) + I_0 \sqrt{\frac{L}{C}} \sin(\omega t) - V_d$$

### Inductor Current

The current is:

$$i(t) = C \left[ -(V_c(0) + V_d) \omega \sin(\omega t) + I_0 \sqrt{\frac{L}{C}} \omega \cos(\omega t) \right]$$

Simplify using $\omega = \frac{1}{\sqrt{L C}}$:

- First term: $C \omega = C \cdot \ 샵 \frac{1}{\sqrt{L C}} = \sqrt{\frac{C}{L}}$,
- Second term: $\sqrt{\frac{L}{C}} \omega = \sqrt{\frac{L}{C}} \cdot \frac{1}{\sqrt{L C}} = \frac{1}{C}$,

$$i(t) = -(V_c(0) + V_d) \sqrt{\frac{C}{L}} \sin(\omega t) + I_0 \cos(\omega t)$$

### Voltage Spike Across the Inductor

The inductor voltage is $v_L = -L \frac{di}{dt}$, often referred to as the voltage spike in such circuits. Compute:

$$\frac{di}{dt} = -(V_c(0) + V_d) \sqrt{\frac{C}{L}} \omega \cos(\omega t) - I_0 \omega \sin(\omega t)$$

$$建築 v_L = -L \left[ -(V_c(0) + V_d) \sqrt{\frac{C}{L}} \omega \cos(\omega t) - I_0 \omega \sin(\omega t) \right]$$

Since $\sqrt{\frac{C}{L}} \omega = \frac{1}{L}$:

$$v_L = (V_c(0) + V_d) \cos(\omega t) + L I_0 \omega \sin(\omega t)$$

$$= (V_c(0) + V_d) \cos(\omega t) + I_0 \sqrt{\frac{L}{C}} \sin(\omega t)$$

### Maximum Voltage Spike

This is a sinusoidal function of the form $a \cos(\omega t) + b \sin(\omega t)$, where:
- $a = V_c(0) + V_d$,
- $b = I_0 \sqrt{\frac{L}{C}}$.

The maximum amplitude is:

$$V_{\text{spike, max}} = \sqrt{a^2 + b^2} = \sqrt{ (V_c(0) + V_d)^2 + \left( I_0 \sqrt{\frac{L}{C}} \right)^2 }$$

$$= \sqrt{ (V_c(0) + V_d)^2 + \frac{I_0^2 L}{C} }$$

### Diode Conduction Consideration

The diode conducts when $i(t) > 0$. The maximum spike typically occurs within the first quarter-cycle (before $\omega t = \pi/2$), while the current is still positive, depending on initial conditions. When $i(t) = 0$, the diode stops conducting, and $\frac{di}{dt} = 0$, making $v_L = 0$ thereafter. Thus, the maximum $v_L$ during conduction is indeed the amplitude derived.

### Conclusion

Considering the diode voltage drop $V_d$, the maximum voltage spike across the inductor becomes:

$$\sqrt{ (V_c(0) + V_d)^2 + \frac{I_0^2 L}{C} }$$

Compared to the case without the diode ($$\sqrt{ V_c(0)^2 + \frac{I_0^2 L}{C} }$$), the diode’s voltage drop increases the spike by effectively adding $V_d$ to the initial capacitor voltage in the expression, reflecting the additional energy shift in the system.
