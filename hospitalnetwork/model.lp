\ Model Hospital NetwORk
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  100 a_h1_k1 + 200 a_h1_k2 + 300 a_h1_k3 + 90 a_h2_k1 + 100 a_h2_k2
   + 250 a_h2_k3 + 50 a_h3_k1 + 250 a_h3_k2 + 300 a_h3_k3 + 180 a_h4_k1
   + 200 a_h4_k2 + 480 a_h4_k3 + 200 a_h5_k1 + 300 a_h5_k2 + 400 a_h5_k3
   - 100 Constant
Subject To
 R0: x_h1_c1 + x_h2_c1 + x_h5_c1 = 1
 R1: x_h1_c2 + x_h2_c2 + x_h4_c2 + x_h5_c2 = 1
 R2: x_h1_c3 + x_h2_c3 + x_h3_c3 + x_h5_c3 = 1
 R3: x_h1_c4 + x_h2_c4 + x_h3_c4 + x_h5_c4 = 1
 R4: x_h1_c5 + x_h2_c5 + x_h3_c5 + x_h5_c5 = 1
 R5: x_h4_c6 + x_h5_c6 = 1
 R6: x_h2_c7 + x_h4_c7 + x_h5_c7 = 1
 R7: x_h4_c8 = 1
 R8: 7.071067811865476 x_h1_c1 - 20 a_h1_k1 - 20 a_h1_k2 - 30 a_h1_k3 <= 0
 R9: 25 x_h1_c2 - 20 a_h1_k1 - 20 a_h1_k2 - 30 a_h1_k3 <= 0
 R10: 11.18033988749895 x_h1_c3 - 20 a_h1_k1 - 20 a_h1_k2 - 30 a_h1_k3
   <= 0
 R11: 11.18033988749895 x_h1_c4 - 20 a_h1_k1 - 20 a_h1_k2 - 30 a_h1_k3
   <= 0
 R12: 15.8113883008419 x_h1_c5 - 20 a_h1_k1 - 20 a_h1_k2 - 30 a_h1_k3 <= 0
 R13: 7.071067811865476 x_h2_c1 - 20 a_h2_k1 - 20 a_h2_k2 - 30 a_h2_k3
   <= 0
 R14: 15 x_h2_c2 - 20 a_h2_k1 - 20 a_h2_k2 - 30 a_h2_k3 <= 0
 R15: 5 x_h2_c3 - 20 a_h2_k1 - 20 a_h2_k2 - 30 a_h2_k3 <= 0
 R16: 11.18033988749895 x_h2_c4 - 20 a_h2_k1 - 20 a_h2_k2 - 30 a_h2_k3
   <= 0
 R17: 15.8113883008419 x_h2_c5 - 20 a_h2_k1 - 20 a_h2_k2 - 30 a_h2_k3 <= 0
 R18: 28.2842712474619 x_h2_c7 - 20 a_h2_k1 - 20 a_h2_k2 - 30 a_h2_k3 <= 0
 R19: 26.92582403567252 x_h3_c3 - 20 a_h3_k1 - 20 a_h3_k2 - 30 a_h3_k3
   <= 0
 R20: 20.6155281280883 x_h3_c4 - 20 a_h3_k1 - 20 a_h3_k2 - 30 a_h3_k3 <= 0
 R21: 15.8113883008419 x_h3_c5 - 20 a_h3_k1 - 20 a_h3_k2 - 30 a_h3_k3 <= 0
 R22: 15 x_h4_c2 - 20 a_h4_k1 - 20 a_h4_k2 - 30 a_h4_k3 <= 0
 R23: 10 x_h4_c6 - 20 a_h4_k1 - 20 a_h4_k2 - 30 a_h4_k3 <= 0
 R24: 22.3606797749979 x_h4_c7 - 20 a_h4_k1 - 20 a_h4_k2 - 30 a_h4_k3 <= 0
 R25: 25 x_h4_c8 - 20 a_h4_k1 - 20 a_h4_k2 - 30 a_h4_k3 <= 0
 R26: 21.21320343559643 x_h5_c1 - 20 a_h5_k1 - 20 a_h5_k2 - 30 a_h5_k3
   <= 0
 R27: 11.18033988749895 x_h5_c2 - 20 a_h5_k1 - 20 a_h5_k2 - 30 a_h5_k3
   <= 0
 R28: 11.18033988749895 x_h5_c3 - 20 a_h5_k1 - 20 a_h5_k2 - 30 a_h5_k3
   <= 0
 R29: 15 x_h5_c4 - 20 a_h5_k1 - 20 a_h5_k2 - 30 a_h5_k3 <= 0
 R30: 15.8113883008419 x_h5_c5 - 20 a_h5_k1 - 20 a_h5_k2 - 30 a_h5_k3 <= 0
 R31: 20 x_h5_c6 - 20 a_h5_k1 - 20 a_h5_k2 - 30 a_h5_k3 <= 0
 R32: 14.14213562373095 x_h5_c7 - 20 a_h5_k1 - 20 a_h5_k2 - 30 a_h5_k3
   <= 0
 R33: x_h1_c1 + x_h1_c2 + x_h1_c3 + x_h1_c4 + x_h1_c5 - a_h1_k1 - 2 a_h1_k2
   - 3 a_h1_k3 <= 0
 R34: x_h2_c1 + x_h2_c2 + x_h2_c3 + x_h2_c4 + x_h2_c5 + x_h2_c7 - a_h2_k1
   - 3 a_h2_k2 - 4 a_h2_k3 <= 0
 R35: x_h3_c3 + x_h3_c4 + x_h3_c5 - a_h3_k1 - 2 a_h3_k2 - 3 a_h3_k3 <= 0
 R36: x_h4_c2 + x_h4_c6 + x_h4_c7 + x_h4_c8 - 2 a_h4_k1 - 2 a_h4_k2
   - 3 a_h4_k3 <= 0
 R37: x_h5_c1 + x_h5_c2 + x_h5_c3 + x_h5_c4 + x_h5_c5 + x_h5_c6 + x_h5_c7
   - a_h5_k1 - 2 a_h5_k2 - 3 a_h5_k3 <= 0
 R38: x_h1_c1 - a_h1_k2 - a_h1_k3 = 0
 R39: x_h1_c3 - a_h1_k2 - a_h1_k3 = 0
 R40: x_h2_c1 - a_h2_k2 - a_h2_k3 = 0
 R41: x_h2_c3 - a_h2_k2 - a_h2_k3 = 0
 R42: x_h3_c3 - a_h3_k2 - a_h3_k3 = 0
 R43: x_h4_c6 - a_h4_k2 - a_h4_k3 = 0
 R44: x_h5_c1 - a_h5_k2 - a_h5_k3 = 0
 R45: x_h5_c3 - a_h5_k2 - a_h5_k3 = 0
 R46: x_h5_c6 - a_h5_k2 - a_h5_k3 = 0
 R47: a_h1_k1 + a_h1_k2 + a_h1_k3 <= 1
 R48: a_h2_k1 + a_h2_k2 + a_h2_k3 <= 1
 R49: a_h3_k1 + a_h3_k2 + a_h3_k3 <= 1
 R50: a_h4_k1 + a_h4_k2 + a_h4_k3 <= 1
 R51: a_h5_k1 + a_h5_k2 + a_h5_k3 <= 1
Bounds
 Constant = 1
Binaries
 x_h1_c1 x_h1_c2 x_h1_c3 x_h1_c4 x_h1_c5 x_h2_c1 x_h2_c2 x_h2_c3 x_h2_c4
 x_h2_c5 x_h2_c7 x_h3_c3 x_h3_c4 x_h3_c5 x_h4_c2 x_h4_c6 x_h4_c7 x_h4_c8
 x_h5_c1 x_h5_c2 x_h5_c3 x_h5_c4 x_h5_c5 x_h5_c6 x_h5_c7 a_h1_k1 a_h1_k2
 a_h1_k3 a_h2_k1 a_h2_k2 a_h2_k3 a_h3_k1 a_h3_k2 a_h3_k3 a_h4_k1 a_h4_k2
 a_h4_k3 a_h5_k1 a_h5_k2 a_h5_k3
End
