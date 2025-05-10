### **Equations for $P_{\text{max}}$, $V_p$, and $I_p$**  

#### **1. Maximum Power ($P_{\text{max}}$)**  
$$P_{\text{max}} = 2.22 \cdot K_w \cdot J \cdot B_{\text{max}} \cdot f \cdot A_e \cdot W_a$$  
**Parameters:**  
- $K_w = 0.5$: Window utilization factor (typical for toroids) .  
- $J = 3 \times 10^6 \, \text{A/m}^2$: Current density (standard for power transformers) .  
- $B_{\text{max}} = 0.182 \, \text{T}$: Adjusted flux density (within ferrite core limits) .  
- $f = 10,\!000 \, \text{Hz}$: Operating frequency (suitable for SMPS) .  
- $A_e = 3.71 \times 10^{-4} \, \text{m}^2$: Effective core area .  
- $W_a = 5.08 \times 10^{-4} \, \text{m}^2$: Window area .  

---

#### **2. Primary Voltage ($V_p$)**  
$$V_p = 4.44 \cdot f \cdot B_{\text{max}} \cdot A_e \cdot N_p$$  
**Parameters:**  
- $N_p = 4$: Primary turns (rounded to integer) .  
- $B_{\text{max}} = 0.182 \, \text{T}$: Adjusted flux density .  
- $f = 10,\!000 \, \text{Hz}$: Frequency .  
- $A_e = 3.71 \times 10^{-4} \, \text{m}^2$: Core area .  
Derived from Faraday’s law of electromagnetic induction for sinusoidal waveforms .  

---

#### **3. Primary Current ($I_p$)**  
$$I_p = \frac{J \cdot K_w \cdot W_a}{N_p}$$  
**Parameters:**  
- $J = 3 \times 10^6 \, \text{A/m}^2$: Current density .  
- $K_w = 0.5$: Window utilization factor .  
- $W_a = 5.08 \times 10^{-4} \, \text{m}^2$: Window area .  
- $N_p = 4$: Primary turns .  
Derived from the relationship $P_{\text{max}} = V_p \cdot I_p$ and the area product method .  

---

### **Key References**  
- **Area Product Method**: $P_{\text{max}}$ formula aligns with transformer design handbooks .  
- **Faraday’s Law**: $V_p$ derivation matches standard electromagnetic induction principles .  
- **Power Relationship**: $I_p$ uses $P = VI$ and winding geometry constraints .  
