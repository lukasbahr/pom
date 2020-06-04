\ Model Hospital NetwORk
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  100 a_h1_k1 + 200 a_h1_k2 + 600 a_h1_k3 - 10 a_h2_k1 + 150 a_h2_k3
   + 150 a_h3_k1 + 350 a_h3_k2 + 400 a_h3_k3 + 180 a_h4_k1 + 200 a_h4_k2
   + 480 a_h4_k3 + 200 a_h5_k1 + 300 a_h5_k2 + 400 a_h5_k3 + 200 a_h6_k2
   + 500 a_h6_k3 + 100 a_h7_k1 + 150 a_h7_k2 + 200 a_h7_k3 - 100 Constant
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
 R18: 11.18033988749895 x_h2_c1 - 20 a_h2_k1 - 20 a_h2_k2 - 30 a_h2_k3
   <= 0
 R19: 15.8113883008419 x_h2_c2 - 20 a_h2_k1 - 20 a_h2_k2 - 30 a_h2_k3 <= 0
 R20: 18.02775637731995 x_h2_c3 - 20 a_h2_k1 - 20 a_h2_k2 - 30 a_h2_k3
   <= 0
 R21: 15.8113883008419 x_h2_c5 - 20 a_h2_k1 - 20 a_h2_k2 - 30 a_h2_k3 <= 0
 R22: 28.2842712474619 x_h2_c7 - 20 a_h2_k1 - 20 a_h2_k2 - 30 a_h2_k3 <= 0
 R23: 14.14213562373095 x_h2_c9 - 20 a_h2_k1 - 20 a_h2_k2 - 30 a_h2_k3
   <= 0
 R24: 10 x_h2_c10 - 20 a_h2_k1 - 20 a_h2_k2 - 30 a_h2_k3 <= 0
 R25: 5 x_h2_c11 - 20 a_h2_k1 - 20 a_h2_k2 - 30 a_h2_k3 <= 0
 R26: 15 x_h3_c3 - 20 a_h3_k1 - 20 a_h3_k2 - 30 a_h3_k3 <= 0
 R27: 15.8113883008419 x_h3_c5 - 20 a_h3_k1 - 20 a_h3_k2 - 30 a_h3_k3 <= 0
 R28: 28.2842712474619 x_h3_c9 - 20 a_h3_k1 - 20 a_h3_k2 - 30 a_h3_k3 <= 0
 R29: 26.92582403567252 x_h3_c11 - 20 a_h3_k1 - 20 a_h3_k2 - 30 a_h3_k3
   <= 0
 R30: 20.6155281280883 x_h4_c1 - 20 a_h4_k1 - 20 a_h4_k2 - 30 a_h4_k3 <= 0
 R31: 15.8113883008419 x_h4_c2 - 20 a_h4_k1 - 20 a_h4_k2 - 30 a_h4_k3 <= 0
 R32: 10 x_h4_c6 - 20 a_h4_k1 - 20 a_h4_k2 - 30 a_h4_k3 <= 0
 R33: 22.3606797749979 x_h4_c7 - 20 a_h4_k1 - 20 a_h4_k2 - 30 a_h4_k3 <= 0
 R34: 22.3606797749979 x_h4_c9 - 20 a_h4_k1 - 20 a_h4_k2 - 30 a_h4_k3 <= 0
 R35: 15 x_h5_c1 - 20 a_h5_k1 - 20 a_h5_k2 - 30 a_h5_k3 <= 0
 R36: 15.8113883008419 x_h5_c2 - 20 a_h5_k1 - 20 a_h5_k2 - 30 a_h5_k3 <= 0
 R37: 20.6155281280883 x_h5_c3 - 20 a_h5_k1 - 20 a_h5_k2 - 30 a_h5_k3 <= 0
 R38: 15.8113883008419 x_h5_c5 - 20 a_h5_k1 - 20 a_h5_k2 - 30 a_h5_k3 <= 0
 R39: 20 x_h5_c6 - 20 a_h5_k1 - 20 a_h5_k2 - 30 a_h5_k3 <= 0
 R40: 14.14213562373095 x_h5_c7 - 20 a_h5_k1 - 20 a_h5_k2 - 30 a_h5_k3
   <= 0
 R41: - 20 a_h5_k1 - 20 a_h5_k2 - 30 a_h5_k3 <= 0
 R42: 22.3606797749979 x_h5_c10 - 20 a_h5_k1 - 20 a_h5_k2 - 30 a_h5_k3
   <= 0
 R43: 11.18033988749895 x_h5_c11 - 20 a_h5_k1 - 20 a_h5_k2 - 30 a_h5_k3
   <= 0
 R44: 10 x_h6_c4 - 20 a_h6_k1 - 20 a_h6_k2 - 30 a_h6_k3 <= 0
 R45: 20 x_h6_c6 - 20 a_h6_k1 - 20 a_h6_k2 - 30 a_h6_k3 <= 0
 R46: 14.14213562373095 x_h6_c7 - 20 a_h6_k1 - 20 a_h6_k2 - 30 a_h6_k3
   <= 0
 R47: 25 x_h6_c8 - 20 a_h6_k1 - 20 a_h6_k2 - 30 a_h6_k3 <= 0
 R48: 28.2842712474619 x_h6_c9 - 20 a_h6_k1 - 20 a_h6_k2 - 30 a_h6_k3 <= 0
 R49: 11.18033988749895 x_h7_c4 - 20 a_h7_k1 - 20 a_h7_k2 - 30 a_h7_k3
   <= 0
 R50: 26.92582403567252 x_h7_c6 - 20 a_h7_k1 - 20 a_h7_k2 - 30 a_h7_k3
   <= 0
 R51: 25 x_h7_c7 - 20 a_h7_k1 - 20 a_h7_k2 - 30 a_h7_k3 <= 0
 R52: 15.8113883008419 x_h7_c8 - 20 a_h7_k1 - 20 a_h7_k2 - 30 a_h7_k3 <= 0
 R53: x_h1_c1 + x_h1_c2 + x_h1_c3 + x_h1_c5 + x_h1_c9 + x_h1_c10 + x_h1_c11
   - 3 a_h1_k1 - 3 a_h1_k2 - 8 a_h1_k3 <= 0
 R54: x_h2_c1 + x_h2_c2 + x_h2_c3 + x_h2_c5 + x_h2_c7 + x_h2_c9 + x_h2_c10
   + x_h2_c11 - 3 a_h2_k1 - 3 a_h2_k2 - 5 a_h2_k3 <= 0
 R55: x_h3_c3 + x_h3_c5 + x_h3_c9 + x_h3_c11 - 3 a_h3_k1 - 3 a_h3_k2
   - 5 a_h3_k3 <= 0
 R56: x_h4_c1 + x_h4_c2 + x_h4_c6 + x_h4_c7 + x_h4_c9 - 3 a_h4_k1
   - 4 a_h4_k2 - 5 a_h4_k3 <= 0
 R57: x_h5_c1 + x_h5_c2 + x_h5_c3 + x_h5_c5 + x_h5_c6 + x_h5_c7 + x_h5_c9
   + x_h5_c10 + x_h5_c11 - 3 a_h5_k1 - 4 a_h5_k2 - 5 a_h5_k3 <= 0
 R58: x_h6_c4 + x_h6_c6 + x_h6_c7 + x_h6_c8 + x_h6_c9 - a_h6_k1 - 2 a_h6_k2
   - 4 a_h6_k3 <= 0
 R59: x_h7_c4 + x_h7_c6 + x_h7_c7 + x_h7_c8 - a_h7_k1 - 2 a_h7_k2
   - 2 a_h7_k3 <= 0
 R60: x_h1_c1 - a_h1_k2 - a_h1_k3 = 0
 R61: x_h1_c3 - a_h1_k2 - a_h1_k3 = 0
 R62: x_h2_c1 - a_h2_k2 - a_h2_k3 = 0
 R63: x_h2_c3 - a_h2_k2 - a_h2_k3 = 0
 R64: x_h3_c3 - a_h3_k2 - a_h3_k3 = 0
 R65: x_h4_c1 - a_h4_k2 - a_h4_k3 = 0
 R66: x_h4_c6 - a_h4_k2 - a_h4_k3 = 0
 R67: x_h5_c1 - a_h5_k2 - a_h5_k3 = 0
 R68: x_h5_c3 - a_h5_k2 - a_h5_k3 = 0
 R69: x_h5_c6 - a_h5_k2 - a_h5_k3 = 0
 R70: x_h6_c6 - a_h6_k2 - a_h6_k3 = 0
 R71: x_h6_c8 - a_h6_k2 - a_h6_k3 = 0
 R72: x_h7_c6 - a_h7_k2 - a_h7_k3 = 0
 R73: x_h7_c8 - a_h7_k2 - a_h7_k3 = 0
 R74: a_h1_k1 + a_h1_k2 + a_h1_k3 <= 1
 R75: a_h2_k1 + a_h2_k2 + a_h2_k3 <= 1
 R76: a_h3_k1 + a_h3_k2 + a_h3_k3 <= 1
 R77: a_h4_k1 + a_h4_k2 + a_h4_k3 <= 1
 R78: a_h5_k1 + a_h5_k2 + a_h5_k3 <= 1
 R79: a_h6_k1 + a_h6_k2 + a_h6_k3 <= 1
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
