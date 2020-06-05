\ Model Hospital NetwORk
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  100 a_h1_k1 + 200 a_h1_k2 + 600 a_h1_k3 + 90 a_h2_k1 + 100 a_h2_k2
   + 250 a_h2_k3 + 50 a_h3_k1 + 250 a_h3_k2 + 300 a_h3_k3 + 180 a_h4_k1
   + 200 a_h4_k2 + 480 a_h4_k3 + 200 a_h5_k1 + 300 a_h5_k2 + 400 a_h5_k3
   + 50 a_h6_k1 + 250 a_h6_k2 + 550 a_h6_k3 + 100 a_h7_k1 + 150 a_h7_k2
   + 200 a_h7_k3 - 150 Constant
Subject To
 R0: x_h1_c1 + x_h2_c1 + x_h4_c1 + x_h5_c1 = 1
 R1: x_h1_c2 + x_h2_c2 + x_h4_c2 + x_h5_c2 = 1
 R2: x_h1_c3 + x_h2_c3 + x_h3_c3 + x_h5_c3 = 1
 R3: x_h6_c4 + x_h7_c4 = 1
 R4: x_h1_c5 + x_h2_c5 + x_h3_c5 + x_h5_c5 = 1
 R5: x_h4_c6 + x_h5_c6 + x_h6_c6 + x_h7_c6 = 1
 R6: x_h2_c7 + x_h4_c7 + x_h5_c7 + x_h6_c7 + x_h7_c7 = 1
 R7: x_h6_c8 + x_h7_c8 = 1
 R8: x_h1_c9 + x_h2_c9 + x_h3_c9 + x_h4_c9 + x_h5_c9 + x_h6_c9 = 1
 R9: x_h1_c10 + x_h2_c10 + x_h5_c10 = 1
 R10: x_h1_c11 + x_h2_c11 + x_h3_c11 + x_h5_c11 = 1
 R11: 20.6155281280883 x_h1_c1 - 20 a_h1_k1 - 20 a_h1_k2 - 30 a_h1_k3 <= 0
 R12: 25.49509756796392 x_h1_c2 - 20 a_h1_k1 - 20 a_h1_k2 - 30 a_h1_k3
   <= 0
 R13: 15 x_h1_c3 - 20 a_h1_k1 - 20 a_h1_k2 - 30 a_h1_k3 <= 0
 R14: 15.8113883008419 x_h1_c5 - 20 a_h1_k1 - 20 a_h1_k2 - 30 a_h1_k3 <= 0
 R15: 22.3606797749979 x_h1_c9 - 20 a_h1_k1 - 20 a_h1_k2 - 30 a_h1_k3 <= 0
 R16: 14.14213562373095 x_h1_c10 - 20 a_h1_k1 - 20 a_h1_k2 - 30 a_h1_k3
   <= 0
 R17: 11.18033988749895 x_h1_c11 - 20 a_h1_k1 - 20 a_h1_k2 - 30 a_h1_k3
   <= 0
 R18: x_h1_c1 + x_h1_c2 + x_h1_c3 + x_h1_c5 + x_h1_c9 + x_h1_c10 + x_h1_c11
   - 3 a_h1_k1 - 3 a_h1_k2 - 8 a_h1_k3 <= 0
 R19: x_h1_c1 - a_h1_k2 - a_h1_k3 = 0
 R20: x_h1_c3 - a_h1_k2 - a_h1_k3 = 0
 R21: a_h1_k1 + a_h1_k2 + a_h1_k3 <= 1
 R22: 11.18033988749895 x_h2_c1 - 20 a_h2_k1 - 20 a_h2_k2 - 30 a_h2_k3
   <= 0
 R23: 15.8113883008419 x_h2_c2 - 20 a_h2_k1 - 20 a_h2_k2 - 30 a_h2_k3 <= 0
 R24: 18.02775637731995 x_h2_c3 - 20 a_h2_k1 - 20 a_h2_k2 - 30 a_h2_k3
   <= 0
 R25: 15.8113883008419 x_h2_c5 - 20 a_h2_k1 - 20 a_h2_k2 - 30 a_h2_k3 <= 0
 R26: 28.2842712474619 x_h2_c7 - 20 a_h2_k1 - 20 a_h2_k2 - 30 a_h2_k3 <= 0
 R27: 14.14213562373095 x_h2_c9 - 20 a_h2_k1 - 20 a_h2_k2 - 30 a_h2_k3
   <= 0
 R28: 10 x_h2_c10 - 20 a_h2_k1 - 20 a_h2_k2 - 30 a_h2_k3 <= 0
 R29: 5 x_h2_c11 - 20 a_h2_k1 - 20 a_h2_k2 - 30 a_h2_k3 <= 0
 R30: x_h2_c1 + x_h2_c2 + x_h2_c3 + x_h2_c5 + x_h2_c7 + x_h2_c9 + x_h2_c10
   + x_h2_c11 - 3 a_h2_k1 - 3 a_h2_k2 - 5 a_h2_k3 <= 0
 R31: x_h2_c1 - a_h2_k2 - a_h2_k3 = 0
 R32: x_h2_c3 - a_h2_k2 - a_h2_k3 = 0
 R33: a_h2_k1 + a_h2_k2 + a_h2_k3 <= 1
 R34: 15 x_h3_c3 - 20 a_h3_k1 - 20 a_h3_k2 - 30 a_h3_k3 <= 0
 R35: 15.8113883008419 x_h3_c5 - 20 a_h3_k1 - 20 a_h3_k2 - 30 a_h3_k3 <= 0
 R36: 28.2842712474619 x_h3_c9 - 20 a_h3_k1 - 20 a_h3_k2 - 30 a_h3_k3 <= 0
 R37: 26.92582403567252 x_h3_c11 - 20 a_h3_k1 - 20 a_h3_k2 - 30 a_h3_k3
   <= 0
 R38: x_h3_c3 + x_h3_c5 + x_h3_c9 + x_h3_c11 - 3 a_h3_k1 - 3 a_h3_k2
   - 5 a_h3_k3 <= 0
 R39: x_h3_c3 - a_h3_k2 - a_h3_k3 = 0
 R40: a_h3_k1 + a_h3_k2 + a_h3_k3 <= 1
 R41: 20.6155281280883 x_h4_c1 - 20 a_h4_k1 - 20 a_h4_k2 - 30 a_h4_k3 <= 0
 R42: 15.8113883008419 x_h4_c2 - 20 a_h4_k1 - 20 a_h4_k2 - 30 a_h4_k3 <= 0
 R43: 10 x_h4_c6 - 20 a_h4_k1 - 20 a_h4_k2 - 30 a_h4_k3 <= 0
 R44: 22.3606797749979 x_h4_c7 - 20 a_h4_k1 - 20 a_h4_k2 - 30 a_h4_k3 <= 0
 R45: 22.3606797749979 x_h4_c9 - 20 a_h4_k1 - 20 a_h4_k2 - 30 a_h4_k3 <= 0
 R46: x_h4_c1 + x_h4_c2 + x_h4_c6 + x_h4_c7 + x_h4_c9 - 3 a_h4_k1
   - 4 a_h4_k2 - 5 a_h4_k3 <= 0
 R47: x_h4_c1 - a_h4_k2 - a_h4_k3 = 0
 R48: x_h4_c6 - a_h4_k2 - a_h4_k3 = 0
 R49: a_h4_k1 + a_h4_k2 + a_h4_k3 <= 1
 R50: 15 x_h5_c1 - 20 a_h5_k1 - 20 a_h5_k2 - 30 a_h5_k3 <= 0
 R51: 15.8113883008419 x_h5_c2 - 20 a_h5_k1 - 20 a_h5_k2 - 30 a_h5_k3 <= 0
 R52: 20.6155281280883 x_h5_c3 - 20 a_h5_k1 - 20 a_h5_k2 - 30 a_h5_k3 <= 0
 R53: 15.8113883008419 x_h5_c5 - 20 a_h5_k1 - 20 a_h5_k2 - 30 a_h5_k3 <= 0
 R54: 20 x_h5_c6 - 20 a_h5_k1 - 20 a_h5_k2 - 30 a_h5_k3 <= 0
 R55: 14.14213562373095 x_h5_c7 - 20 a_h5_k1 - 20 a_h5_k2 - 30 a_h5_k3
   <= 0
 R56: - 20 a_h5_k1 - 20 a_h5_k2 - 30 a_h5_k3 <= 0
 R57: 22.3606797749979 x_h5_c10 - 20 a_h5_k1 - 20 a_h5_k2 - 30 a_h5_k3
   <= 0
 R58: 11.18033988749895 x_h5_c11 - 20 a_h5_k1 - 20 a_h5_k2 - 30 a_h5_k3
   <= 0
 R59: x_h5_c1 + x_h5_c2 + x_h5_c3 + x_h5_c5 + x_h5_c6 + x_h5_c7 + x_h5_c9
   + x_h5_c10 + x_h5_c11 - 3 a_h5_k1 - 4 a_h5_k2 - 5 a_h5_k3 <= 0
 R60: x_h5_c1 - a_h5_k2 - a_h5_k3 = 0
 R61: x_h5_c3 - a_h5_k2 - a_h5_k3 = 0
 R62: x_h5_c6 - a_h5_k2 - a_h5_k3 = 0
 R63: a_h5_k1 + a_h5_k2 + a_h5_k3 <= 1
 R64: 10 x_h6_c4 - 20 a_h6_k1 - 20 a_h6_k2 - 30 a_h6_k3 <= 0
 R65: 20 x_h6_c6 - 20 a_h6_k1 - 20 a_h6_k2 - 30 a_h6_k3 <= 0
 R66: 14.14213562373095 x_h6_c7 - 20 a_h6_k1 - 20 a_h6_k2 - 30 a_h6_k3
   <= 0
 R67: 25 x_h6_c8 - 20 a_h6_k1 - 20 a_h6_k2 - 30 a_h6_k3 <= 0
 R68: 28.2842712474619 x_h6_c9 - 20 a_h6_k1 - 20 a_h6_k2 - 30 a_h6_k3 <= 0
 R69: x_h6_c4 + x_h6_c6 + x_h6_c7 + x_h6_c8 + x_h6_c9 - a_h6_k1 - 2 a_h6_k2
   - 4 a_h6_k3 <= 0
 R70: x_h6_c6 - a_h6_k2 - a_h6_k3 = 0
 R71: x_h6_c8 - a_h6_k2 - a_h6_k3 = 0
 R72: a_h6_k1 + a_h6_k2 + a_h6_k3 <= 1
 R73: 11.18033988749895 x_h7_c4 - 20 a_h7_k1 - 20 a_h7_k2 - 30 a_h7_k3
   <= 0
 R74: 26.92582403567252 x_h7_c6 - 20 a_h7_k1 - 20 a_h7_k2 - 30 a_h7_k3
   <= 0
 R75: 25 x_h7_c7 - 20 a_h7_k1 - 20 a_h7_k2 - 30 a_h7_k3 <= 0
 R76: 15.8113883008419 x_h7_c8 - 20 a_h7_k1 - 20 a_h7_k2 - 30 a_h7_k3 <= 0
 R77: x_h7_c4 + x_h7_c6 + x_h7_c7 + x_h7_c8 - a_h7_k1 - 2 a_h7_k2
   - 2 a_h7_k3 <= 0
 R78: x_h7_c6 - a_h7_k2 - a_h7_k3 = 0
 R79: x_h7_c8 - a_h7_k2 - a_h7_k3 = 0
 R80: a_h7_k1 + a_h7_k2 + a_h7_k3 <= 1
Bounds
 Constant = 1
Binaries
 x_h1_c1 x_h1_c2 x_h1_c3 x_h1_c5 x_h1_c9 x_h1_c10 x_h1_c11 x_h2_c1 x_h2_c2
 x_h2_c3 x_h2_c5 x_h2_c7 x_h2_c9 x_h2_c10 x_h2_c11 x_h3_c3 x_h3_c5 x_h3_c9
 x_h3_c11 x_h4_c1 x_h4_c2 x_h4_c6 x_h4_c7 x_h4_c9 x_h5_c1 x_h5_c2 x_h5_c3
 x_h5_c5 x_h5_c6 x_h5_c7 x_h5_c9 x_h5_c10 x_h5_c11 x_h6_c4 x_h6_c6 x_h6_c7
 x_h6_c8 x_h6_c9 x_h7_c4 x_h7_c6 x_h7_c7 x_h7_c8 a_h1_k1 a_h1_k2 a_h1_k3
 a_h2_k1 a_h2_k2 a_h2_k3 a_h3_k1 a_h3_k2 a_h3_k3 a_h4_k1 a_h4_k2 a_h4_k3
 a_h5_k1 a_h5_k2 a_h5_k3 a_h6_k1 a_h6_k2 a_h6_k3 a_h7_k1 a_h7_k2 a_h7_k3
End
