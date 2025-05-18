To determine the equations for a DC-DC boost converter when replacing a toroidal core with an EI core made of silicon steel, we need to consider the differences in geometry and material properties between the two core types and how these affect the key equations provided in the document. The toroid is a doughnut-shaped core characterized by its average radius $r_{\text{avg}}$, while the EI core, composed of E-shaped and I-shaped laminations, has a different magnetic path length denoted as $l$. Additionally, silicon steel has specific material properties, such as relative permeability $\mu_r$ and saturation flux density $B_{\text{max}}$, which must be used in the equations. Below, we adapt each equation step-by-step.

---

### **1. Inductance ($L$)**
For the toroid, the inductance is given by:
$$L = \frac{\mu_0 \mu_r N^2 A}{2\pi r_{\text{avg}}}$$
where:
- $\mu_0 = 4\pi \times 10^{-7} \, \text{H/m}$ is the vacuum permeability,
- $\mu_r$ is the relative permeability of the core material,
- $N$ is the number of turns,
- $A$ is the cross-sectional area,
- $2\pi r_{\text{avg}}$ is the magnetic path length of the toroid.

For an EI core, the magnetic path length is the effective length $l$, determined by its geometry (e.g., the perimeter of the magnetic circuit through the E and I sections). The inductance formula becomes:
$$L = \frac{\mu_0 \mu_r N^2 A}{l}$$
**Change**: Replace $2\pi r_{\text{avg}}$ with $l$, and use the $\mu_r$ specific to silicon steel.

---

### **2. Peak Current ($I_{\text{peak}}$)**
The peak current at saturation for the toroid is:
$$I_{\text{peak}} = \frac{2\pi r_{\text{avg}} B_{\text{max}}}{\mu_0 \mu_r N}$$
This arises from the saturation condition where the magnetic flux $\Phi = B_{\text{max}} A$, and the magnetomotive force $N I_{\text{peak}} = H l$, with $H = \frac{B_{\text{max}}}{\mu_0 \mu_r}$ and $l = 2\pi r_{\text{avg}}$ for the toroid.

For the EI core, the magnetic path length is $l$, so:
$$I_{\text{peak}} = \frac{l B_{\text{max}}}{\mu_0 \mu_r N}$$
**Change**: Replace $2\pi r_{\text{avg}}$ with $l$, and use the $B_{\text{max}}$ of silicon steel.

---

### **3. Energy per Cycle ($E_{\text{cycle}}$)**
The energy stored per cycle is:
$$E_{\text{cycle}} = \frac{1}{2} L I_{\text{peak}}^2$$
For the toroid:
$$E_{\text{cycle}} = \frac{1}{2} \left( \frac{\mu_0 \mu_r N^2 A}{2\pi r_{\text{avg}}} \right) \left( \frac{2\pi r_{\text{avg}} B_{\text{max}}}{\mu_0 \mu_r N} \right)^2$$
$$= \frac{1}{2} \left( \frac{\mu_0 \mu_r N^2 A}{2\pi r_{\text{avg}}} \right) \left( \frac{4\pi^2 r_{\text{avg}}^2 B_{\text{max}}^2}{\mu_0^2 \mu_r^2 N^2} \right) = \frac{\pi r_{\text{avg}} B_{\text{max}}^2 A}{\mu_0 \mu_r}$$

For the EI core:
$$E_{\text{cycle}} = \frac{1}{2} \left( \frac{\mu_0 \mu_r N^2 A}{l} \right) \left( \frac{l B_{\text{max}}}{\mu_0 \mu_r N} \right)^2$$
$$= \frac{1}{2} \left( \frac{\mu_0 \mu_r N^2 A}{l} \right) \left( \frac{l^2 B_{\text{max}}^2}{\mu_0^2 \mu_r^2 N^2} \right) = \frac{1}{2} \frac{A B_{\text{max}}^2 l}{\mu_0 \mu_r}$$
**Change**: The expression reflects the new $L$ and $I_{\text{peak}}$, with $l$ instead of $2\pi r_{\text{avg}}$.

---

### **4. Switching Period ($T_{\text{sw}}$)**
The switching period is:
$$T_{\text{sw}} = t_{\text{switch}} + t_{\text{on}} + t_{\text{off}}$$
where:
- $t_{\text{on}} = \frac{L}{R_{\text{switch}}}$,
- $t_{\text{off}} = 5 \frac{L}{R_{\text{load}}}$.

For the toroid:
$$T_{\text{sw}} = t_{\text{switch}} + \frac{\mu_0 \mu_r N^2 A}{2\pi r_{\text{avg}} R_{\text{switch}}} + \frac{5 \mu_0 \mu_r N^2 A}{2\pi r_{\text{avg}} R_{\text{load}}}$$

For the EI core:
$$T_{\text{sw}} = t_{\text{switch}} + \frac{\mu_0 \mu_r N^2 A}{l R_{\text{switch}}} + \frac{5 \mu_0 \mu_r N^2 A}{l R_{\text{load}}}$$
**Change**: Replace $2\pi r_{\text{avg}}$ with $l$.

---

### **5. Switching Frequency ($f_{\text{sw}}$)**
$$f_{\text{sw}} = \frac{1}{T_{\text{sw}}}$$
For the EI core:
$$f_{\text{sw}} = \frac{1}{t_{\text{switch}} + \frac{\mu_0 \mu_r N^2 A}{l R_{\text{switch}}} + \frac{5 \mu_0 \mu_r N^2 A}{l R_{\text{load}}}}$$
**Change**: Consistent with the updated $T_{\text{sw}}$.

---

### **6. Optimized Output Power ($P_{\text{out}}$)**
$$P_{\text{out}} = E_{\text{cycle}} \cdot f_{\text{sw}}$$
For the EI core:
$$P_{\text{out}} = \left( \frac{1}{2} \frac{A B_{\text{max}}^2 l}{\mu_0 \mu_r} \right) \cdot \left( \frac{1}{t_{\text{switch}} + \frac{\mu_0 \mu_r N^2 A}{l R_{\text{switch}}} + \frac{5 \mu_0 \mu_r N^2 A}{l R_{\text{load}}}} \right)$$
$$= \frac{\frac{1}{2} \frac{A B_{\text{max}}^2 l}{\mu_0 \mu_r}}{t_{\text{switch}} + \frac{\mu_0 \mu_r N^2 A}{l R_{\text{switch}}} + \frac{5 \mu_0 \mu_r N^2 A}{l R_{\text{load}}}}$$
**Change**: Uses the EI core’s $E_{\text{cycle}}$ and $f_{\text{sw}}$.

---

### **7. Simplified Output Power (assuming $t_{\text{switch}} = 0$)**
For the toroid:
$$P_{\text{out}} = \frac{2\pi^2 r_{\text{avg}}^2 B_{\text{max}}^2}{\mu_0^2 \mu_r^2 N^2} \cdot \frac{R_{\text{switch}} R_{\text{load}}}{R_{\text{load}} + 5 R_{\text{switch}}}$$

For the EI core, with $t_{\text{switch}} = 0$:
$$T_{\text{sw}} = \frac{\mu_0 \mu_r N^2 A}{l} \left( \frac{1}{R_{\text{switch}}} + \frac{5}{R_{\text{load}}} \right)$$
$$P_{\text{out}} = \frac{\frac{1}{2} \frac{A B_{\text{max}}^2 l}{\mu_0 \mu_r}}{\frac{\mu_0 \mu_r N^2 A}{l} \left( \frac{1}{R_{\text{switch}}} + \frac{5}{R_{\text{load}}} \right)} = \frac{\frac{1}{2} B_{\text{max}}^2 l^2}{\mu_0^2 \mu_r^2 N^2} \cdot \frac{1}{\frac{1}{R_{\text{switch}}} + \frac{5}{R_{\text{load}}}}$$
Since:
$$\frac{1}{\frac{1}{R_{\text{switch}}} + \frac{5}{R_{\text{load}}}} = \frac{R_{\text{switch}} R_{\text{load}}}{R_{\text{load}} + 5 R_{\text{switch}}}$$
$$P_{\text{out}} = \frac{\frac{1}{2} B_{\text{max}}^2 l^2}{\mu_0^2 \mu_r^2 N^2} \cdot \frac{R_{\text{switch}} R_{\text{load}}}{R_{\text{load}} + 5 R_{\text{switch}}}$$
**Change**: Replace $2\pi^2 r_{\text{avg}}^2$ with $\frac{1}{2} l^2$, reflecting the geometry and energy scaling.

---

### **8. Output Voltage ($V_{\text{out}}$)**
$$V_{\text{out}} = \sqrt{P_{\text{out}} \cdot R_{\text{load}}}$$
This remains unchanged in form, using the updated $P_{\text{out}}$.

---

### **9. Input Voltage ($V_{\text{in}}$)**
$$V_{\text{in}} = I_{\text{peak}} R_{\text{switch}} = \frac{l B_{\text{max}} R_{\text{switch}}}{\mu_0 \mu_r N}$$
**Change**: Uses the EI core’s $I_{\text{peak}}$.

---

### **Material Considerations**
Silicon steel typically has:
- High $\mu_r$ (e.g., 2000–4000), compared to other core materials,
- $B_{\text{max}}$ around 1.5–2 T, depending on the grade.
These values should be substituted into the equations based on the specific silicon steel used.

---

### **Summary of Equations for EI Core**
1. **Inductance**:
$$L = \frac{\mu_0 \mu_r N^2 A}{l}$$
2. **Peak Current**:
$$I_{\text{peak}} = \frac{l B_{\text{max}}}{\mu_0 \mu_r N}$$
3. **Energy per Cycle**:
$$E_{\text{cycle}} = \frac{1}{2} \frac{A B_{\text{max}}^2 l}{\mu_0 \mu_r}$$
4. **Switching Period**:
$$T_{\text{sw}} = t_{\text{switch}} + \frac{\mu_0 \mu_r N^2 A}{l R_{\text{switch}}} + \frac{5 \mu_0 \mu_r N^2 A}{l R_{\text{load}}}$$
5. **Switching Frequency**:
$$f_{\text{sw}} = \frac{1}{t_{\text{switch}} + \frac{\mu_0 \mu_r N^2 A}{l R_{\text{switch}}} + \frac{5 \mu_0 \mu_r N^2 A}{l R_{\text{load}}}}$$
6. **Output Power**:
$$P_{\text{out}} = \frac{\frac{1}{2} \frac{A B_{\text{max}}^2 l}{\mu_0 \mu_r}}{t_{\text{switch}} + \frac{\mu_0 \mu_r N^2 A}{l R_{\text{switch}}} + \frac{5 \mu_0 \mu_r N^2 A}{l R_{\text{load}}}}$$
7. **Simplified Output Power ($t_{\text{switch}} = 0$)**:
$$P_{\text{out}} = \frac{\frac{1}{2} B_{\text{max}}^2 l^2}{\mu_0^2 \mu_r^2 N^2} \cdot \frac{R_{\text{switch}} R_{\text{load}}}{R_{\text{load}} + 5 R_{\text{switch}}}$$
8. **Output Voltage**:
$$V_{\text{out}} = \sqrt{P_{\text{out}} \cdot R_{\text{load}}}$$
9. **Input Voltage**:
$$V_{\text{in}} = \frac{l B_{\text{max}} R_{\text{switch}}}{\mu_0 \mu_r N}$$

The equations for the EI core are analogous to those for the toroid, with the magnetic path length $l$ replacing $2\pi r_{\text{avg}}$, and the material properties $\mu_r$ and $B_{\text{max}}$ of silicon steel applied accordingly.
