### **Used Equations with Explanations and Calculations**

#### **1. Voltage Divider Equation for $ V_{\text{point}} $**  
$$V_{\text{point,DC}} = V_{\text{in}} \cdot \frac{R_2}{R_1 + R_2} = 3.3\,\text{V} \cdot \frac{10\,\text{k}\Omega}{1.2\,\text{k}\Omega + 10\,\text{k}\Omega} = 2.95\,\text{V}$$  
**Explanation**: This calculates the steady-state voltage at $ V_{\text{point}} $ during the high phase of the square wave.

---

#### **2. RC Time Constants**  
- **Charging**:  
  $$\tau_{\text{charge}} = R_1 C_1 = 1.2\,\text{k}\Omega \cdot 100\,\text{nF} = 0.12\,\text{ms}$$  
- **Discharging**:  
  $$\tau_{\text{discharge}} = R_2 C_1 = 10\,\text{k}\Omega \cdot 100\,\text{nF} = 1\,\text{ms}$$  
**Explanation**: These time constants govern the exponential rise/fall of $ V_{\text{point}}(t) $ due to the RC filter.

---

#### **3. MOSFET Drain Current**  
$$i_p(t) = K(V_{\text{GS}}(t) - V_{\text{th}})^2 = 5\,\text{A/V}^2 \cdot (V_{\text{point}}(t) - 2\,\text{V})^2$$  
**Explanation**: The primary current depends on the gate-source voltage $ V_{\text{GS}}(t) $, which follows $ V_{\text{point}}(t) $. This creates a nonlinear relationship between $ i_p(t) $ and $ V_{\text{point}}(t) $.

---

#### **4. Transformer Inductances**  
- **Primary inductance**:  
  $$L_1 = \frac{\mu N_1^2 A}{l} = \frac{(4\pi \times 10^{-7}) \cdot 2000 \cdot 3^2 \cdot 3.71 \times 10^{-4}}{0.2055} = 40.8\,\mu\text{H}$$  
- **Secondary inductance**:  
  $$L_2 = \frac{\mu N_2^2 A}{l} = \frac{(4\pi \times 10^{-7}) \cdot 2000 \cdot 45^2 \cdot 3.71 \times 10^{-4}}{0.2055} = 9.18\,\text{mH}$$  
- **Mutual inductance**:  
  $$M = \sqrt{L_1 L_2} = \sqrt{40.8 \times 10^{-6} \cdot 9.18 \times 10^{-3}} = 612\,\mu\text{H}$$  
**Explanation**: These depend on the core geometry ($ A = 3.71 \times 10^{-4}\,\text{m}^2 $, $ l = 0.2055\,\text{m} $), permeability ($ \mu = \mu_0 \mu_r $), and turns ($ N_1 = 3 $, $ N_2 = 45 $).

---

#### **5. Secondary Current Integral Equation**  
$$i_2(t) = \frac{M}{L_2} \int_0^t e^{-\frac{R}{L_2}(t - \tau)} \left(-\frac{di_p(\tau)}{d\tau}\right) d\tau$$  
Substituting $ R = 200\,\Omega $, $ L_2 = 9.18\,\text{mH} $, and $ M = 612\,\mu\text{H} $:  
$$i_2(t) = -0.0667 \int_0^t e^{-21786(t - \tau)} \frac{di_p(\tau)}{d\tau} d\tau$$  
**Explanation**: This convolution integral accounts for the exponential decay of secondary current due to the $ 200\,\Omega $ load.

---

### **Circuit Parts and Connections**  
1. **Square Wave Source**:  
   - Drives $ R_1 = 1.2\,\text{k}\Omega $, forming a voltage divider with $ R_2 = 10\,\text{k}\Omega $.

2. **RC Filter**:  
   - $ C_1 = 100\,\text{nF} $ smooths $ V_{\text{point}} $, creating exponential rise/fall transitions.

3. **MOSFET (IRF540)**:  
   - Gate voltage $ V_{\text{GS}}(t) = V_{\text{point}}(t) $.  
   - Conducts when $ V_{\text{GS}}(t) > V_{\text{th}} = 2\,\text{V} $, generating $ i_p(t) $.

4. **Transformer**:  
   - **Primary**: 3 turns, $ L_1 = 40.8\,\mu\text{H} $, driven by $ i_p(t) $.  
   - **Secondary**: 45 turns, $ L_2 = 9.18\,\text{mH} $, with mutual inductance $ M = 612\,\mu\text{H} $.  
   - **Load**: $ 200\,\Omega $ resistor on secondary side.

5. **Waveforms**:  
   - $ V_{\text{point}}(t) $: Exponential rise/fall (RC filter).  
   - $ i_p(t) $: Non-square pulses due to delayed MOSFET turn-on/turn-off.  
   - $ i_2(t) $: Exponentially decaying pulses from transformer dynamics.

---

### **Key Observations**  
- **Nonlinear Effects**: The MOSFET’s $ i_p(t) $ is nonlinear due to $ (V_{\text{GS}} - V_{\text{th}})^2 $.  
- **Transient Behavior**: $ V_{\text{point}}(t) $’s exponential transitions narrow the MOSFET conduction window.  
- **Secondary Current**: Peaks at $ \sim 300\,\text{mA} $ but decays within $ 45.9\,\mu\text{s} $ ($ \tau = L_2/R $).

This analysis integrates Ohm’s law, RC filtering, MOSFET physics, and transformer theory to model the circuit’s behavior.
