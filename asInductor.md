### **Key Equations for DC DC Booster Converter Output Power ($P_{\text{out}}$)**

1. **Toroid Inductance**:  
   $$L = \frac{\mu_0 \mu_r N^2 A}{2\pi r_{\text{avg}}}$$  
2. **Peak Current (Saturation Limit)**:  
   $$I_{\text{peak}} = \frac{2\pi r_{\text{avg}} B_{\text{max}}}{\mu_0 \mu_r N}$$  
Higher input current than peak current at inductor will be ignored because of saturation magnetic flux density limitation.
3. **Energy per Cycle**:  
   $$E_{\text{cycle}} = \frac{1}{2} L I_{\text{peak}}^2$$  
4. **Choosing Optimized Switching Period**:  
   $$T_{\text{sw}} = t_{\text{switch}} + t_{\text{on}} + t_{\text{off}}$$  
   Where:  
   - $t_{\text{on}} = \frac{L}{R_{\text{switch}}}$  
   - $t_{\text{off}} = 5 \cdot \frac{L}{R_{\text{load}}}$  
`5T` role for full discharging. 
5. **Choosing Optimized Switching Frequency**:  
   $$f_{\text{sw}} = \frac{1}{T_{\text{sw}}} = \frac{1}{t_{\text{switch}} + \frac{L}{R_{\text{switch}}} + \frac{5L}{R_{\text{load}}}}$$  
6. **Optimized Output Power**:  
   $$P_{\text{out}}$$ = $$E_{\text{cycle}} \cdot f_{\text{sw}}$$ = $$\frac{\pi r_{\text{avg}} B_{\text{max}}^2 A}{\mu_0 \mu_r} \cdot \frac{1}{t_{\text{switch}} + \frac{\mu_0 \mu_r N^2 A}{2\pi r_{\text{avg}} R_{\text{switch}}} + \frac{5 \mu_0 \mu_r N^2 A}{2\pi r_{\text{avg}} R_{\text{load}}}}$$  
7. **Optimized Output Voltage**
   $$V_{\text{out}} = \sqrt{P_{\text{out}} \cdot R_{\text{load}}}$$
8. **Needed Input Voltage**
   $$V_{\text{in}} = I_{\text{peak}} R_{\text{switch}}$$

### **Variables**  
- $N$: Number of turns  
- $A$: Cross-sectional area of toroid  
- $B_{\text{max}}$: Maximum flux density  
- $r_{\text{avg}}$: Average radius of toroid  
- $R_{\text{switch}}$: MOSFET switch resistance  
- $R_{\text{load}}$: Load resistance  
- $t_{\text{switch}}$: Switching transition time  

### **Simplified Output Power Equation (assume that $t_{\text{switch}} = 0$ for better analysis)**

$$
P_{\text{out}} = \frac{2\pi^2 r_{\text{avg}}^2 B_{\text{max}}^2}{\mu_0^2 \mu_r^2 N^2} \cdot \frac{R_{\text{switch}} R_{\text{load}}}{R_{\text{load}} + 5 R_{\text{switch}}}
$$

---

### **Variable Definitions**  
1. **Core Parameters**:  
   - $N$: Number of turns  
   - $B_{\text{max}}$: Saturation flux density (T)  
   - $r_{\text{avg}}$: Average radius of the toroid (m)  
   - $\mu_0 = 4\pi \times 10^{-7} \, \text{H/m}$: Vacuum permeability  
   - $\mu_r$: Relative permeability  

2. **Circuit Parameters**:  
   - $R_{\text{switch}}$: MOSFET on-resistance ($\Omega$)  
   - $R_{\text{load}}$: Load resistance ($\Omega$)  

---

### **Key Observations**  
- Output power $\propto B_{\text{max}}^2$, $r_{\text{avg}}^2$, and $\frac{1}{N^2}$ at optimized frequency.  
- Output voltage $\propto P_{\text{out}}^½$ (Or $\propto B_{\text{max}}$, $r_{\text{avg}}$, and $\frac{1}{N}$) at optimized frequency.
- Higher $R_{\text{switch}}$ and $R_{\text{load}}$ will increase the power and voltage at optimized frequency.
- Energy of each cycle $\propto B_{\text{max}}^2$, $r_{\text{avg}}$, and $A$.  
