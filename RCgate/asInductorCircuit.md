### Circuit Components and Connections

#### **1. Capacitor (C)**  
Discharges through a resistor $ R $, governed by:  
$$V_{\text{out}} = V_0 e^{-t/(RC)}$$  
This equation describes the voltage decay across the capacitor over time [[9]].

#### **2. MOSFET (Metal-Oxide-Semiconductor Field-Effect Transistor)**  
Operates in saturation mode with drain current:  
$$I_d = K(V_{gs} - V_{\text{th}})^2$$  
Here, $ V_{gs} = V_{\text{out}} $ (capacitor voltage), and $ V_{\text{th}} $ is the threshold voltage [[4]][[6]].

#### **3. Inductor (L)**  
Generates a voltage spike during current cutoff:  
$$V_{\text{spike}} = L \frac{di}{dt}$$  
The inductor opposes sudden changes in current, leading to transient voltage spikes [[4]].

---

### **Connections**  
1. **Capacitor → MOSFET Gate-Source ($ V_{gs} $)**:  
   The capacitor voltage $ V_{\text{out}} $ directly drives the MOSFET's gate-source voltage ($ V_{gs} $).

2. **MOSFET Drain Current ($ I_d $) → Inductor**:  
   The drain current $ I_d $ flows through the inductor, creating a time-dependent current $ i = I_d $ for the inductor voltage calculation.

---

### **Combined Effect**  
Substituting $ V_{gs} = V_{\text{out}} $ and $ i = I_d $ into the inductor equation yields:  
$$V_{\text{spike}} = -\frac{2KL V_0}{RC} e^{-t/(RC)} \left(V_0 e^{-t/(RC)} - V_{\text{th}}\right)$$  
At $ t = 0 $, this simplifies to:  
$$V_{\text{spike}} = -\frac{2KL V_0 (V_0 - V_{\text{th}})}{RC}$$  
The negative sign indicates polarity inversion due to inductor back-EMF [[4]][[6]].
