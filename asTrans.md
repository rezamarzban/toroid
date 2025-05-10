### **Core Geometry**
1. **Effective Core Area (Ae):**  
   $$A_e = (OD - ID) \cdot HT$$  
   Where $OD$ = outside diameter, $ID$ = inside diameter, $HT$ = height of the core (https://coil32.net/ferrite-toroid-core.html).

2. **Window Area (Wa):**  
   $$W_a = \pi \cdot \left(\frac{ID}{2}\right)^2$$  
   Represents the area available for windings inside the toroid (https://coil32.net/ferrite-toroid-core.html).

---

### **Turns Calculation**
3. **Primary Turns (Np):**  
   $$N_p = \frac{V_p}{4.44 \cdot f \cdot B_{\text{max}} \cdot A_e}$$  
   Derived from Faraday’s law of electromagnetic induction ($V = N \cdot \frac{d\Phi}{dt}$) (https://www.quora.com/How-is-the-number-of-turns-of-a-transformer-determined-if-the).

4. **Adjusted Flux Density (B_max):**  
   $$B_{\text{max}} = \frac{V_p}{4.44 \cdot f \cdot N_p \cdot A_e}$$  
   Recalculated after rounding $N_p$ to ensure feasibility (https://www.mag-inc.com/Design/Design-Guides/Transformer-Design-with-Magnetics-Ferrite-Cores).

5. **Secondary Turns (Ns):**  
   $$N_s = N_p \cdot \frac{V_s}{V_p}$$  
   Based on the voltage ratio assumption for ideal transformers (https://www.allaboutcircuits.com/technical-articles/calculating-the-turns-ratio-of-a-transformer/).

---

### **Power Handling Capacity**
6. **Maximum Power (P_max):**  
   $$P_{\text{max}} = 2.22 \cdot K_w \cdot J \cdot B_{\text{max}} \cdot f \cdot A_e \cdot W_a$$  
   Uses the **area product method** to estimate power capacity, where:  
   - $K_w$ = window utilization factor (0.5 for toroids),  
   - $J$ = current density ($3 \times 10^6 \, \text{A/m}^2$),  
   - $B_{\text{max}}$ = adjusted flux density,  
   - $f$ = frequency (10 kHz) (https://www.mag-inc.com/Design/Design-Guides/Transformer-Design-with-Magnetics-Ferrite-Cores).

---

### **Power Loss Limitations**
7. **Core Loss (Steinmetz Equation):**  
   $$P_{\text{core}} = k \cdot f^\alpha \cdot B^\beta \cdot V_c$$  
   Requires material-specific constants ($k, \alpha, \beta$) and core volume ($V_c$), which were omitted due to missing data (https://www.homemade-circuits.com/how-to-design-and-calculate-ferrite-core-transformers-for-inverters/).

8. **Copper Loss:**  
   $$P_{\text{copper}} = I_p^2 \cdot R_{\text{DC}} \cdot (1 + \text{AC resistance factor})$$  
   Depends on wire gauge, length, and skin/proximity effects at high frequencies, not calculated here (https://www.homemade-circuits.com/how-to-design-and-calculate-ferrite-core-transformers-for-inverters/).

---

### **Key Constants and Assumptions**
- **Frequency (f):** 10 kHz (typical for SMPS applications) (https://www.mag-inc.com/Design/Design-Guides/Transformer-Design-with-Magnetics-Ferrite-Cores).  
- **Current Density (J):** $3 \times 10^6 \, \text{A/m}^2$ (standard for power transformers) (https://www.mag-inc.com/Design/Design-Guides/Transformer-Design-with-Magnetics-Ferrite-Cores).  
- **Window Utilization (Kw):** 0.5 (conservative estimate for toroids) (https://www.mag-inc.com/Design/Design-Guides/Transformer-Design-with-Magnetics-Ferrite-Cores).  

---

### **Summary of Unused Equations**
- **Slope Formula:** $ \text{Slope} = \frac{y_2 - y_1}{x_2 - x_1} $ (not relevant here) (https://www.indeed.com/career-advice/career-development/types-of-equations).  
- **kVA Rating:** $ \text{kVA} = \frac{V \cdot I}{1000} $ (used for sizing transformers but not in this design) (https://www.ia.omron.com/data_pdf/cat/transformer-sizing-guide.pdf).  

These equations were omitted as they pertain to unrelated contexts (e.g., graphing, kVA sizing) or require data not provided (e.g., core material properties).  
