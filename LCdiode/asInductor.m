V_c0 = 0.0;
V_d = 0.7;
I_0 = 1.0;
L = 0.001;
C = 1e-6;
term1 = (V_c0 + V_d)^2;
term2 = (I_0^2 * L) / C;
V_c = sqrt(term1 + term2)
