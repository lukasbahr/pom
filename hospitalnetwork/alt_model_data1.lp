\ Model Hospital NetwORk
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  100 y_1_h1 + 200 y_2_h1 + 300 y_3_h1 + 90 y_1_h2 + 100 y_2_h2 + 250 y_3_h2
   + 50 y_1_h3 + 250 y_2_h3 + 300 y_3_h3 + 180 y_1_h4 + 200 y_2_h4
   + 480 y_3_h4 + 200 y_1_h5 + 300 y_2_h5 + 400 y_3_h5 - 100 Constant
Subject To
 R0: x_h1_c1 + x_h2_c1 + x_h5_c1 = 1
 R1: x_h1_c2 + x_h2_c2 + x_h4_c2 + x_h5_c2 = 1
 R2: x_h1_c3 + x_h2_c3 + x_h3_c3 + x_h5_c3 = 1
 R3: x_h1_c4 + x_h2_c4 + x_h3_c4 + x_h5_c4 = 1
 R4: x_h1_c5 + x_h2_c5 + x_h3_c5 + x_h5_c5 = 1
 R5: x_h4_c6 + x_h5_c6 = 1
 R6: x_h2_c7 + x_h4_c7 + x_h5_c7 = 1
 R7: x_h4_c8 = 1
 R8: 7.071067811865476 x_h1_c1 - 20 y_1_h1 - 20 y_2_h1 - 30 y_3_h1 <= 0
 R9: 25 x_h1_c2 - 20 y_1_h1 - 20 y_2_h1 - 30 y_3_h1 <= 0
 R10: 11.18033988749895 x_h1_c3 - 20 y_1_h1 - 20 y_2_h1 - 30 y_3_h1 <= 0
 R11: 11.18033988749895 x_h1_c4 - 20 y_1_h1 - 20 y_2_h1 - 30 y_3_h1 <= 0
 R12: 15.8113883008419 x_h1_c5 - 20 y_1_h1 - 20 y_2_h1 - 30 y_3_h1 <= 0
 R13: x_h1_c1 + x_h1_c2 + x_h1_c3 + x_h1_c4 + x_h1_c5 - y_1_h1 - 2 y_2_h1
   - 3 y_3_h1 <= 0
 R14: x_h1_c1 - y_2_h1 - y_3_h1 = 0
 R15: x_h1_c3 - y_2_h1 - y_3_h1 = 0
 R16: y_1_h1 + y_2_h1 + y_3_h1 <= 1
 R17: 7.071067811865476 x_h2_c1 - 20 y_1_h2 - 20 y_2_h2 - 30 y_3_h2 <= 0
 R18: 15 x_h2_c2 - 20 y_1_h2 - 20 y_2_h2 - 30 y_3_h2 <= 0
 R19: 5 x_h2_c3 - 20 y_1_h2 - 20 y_2_h2 - 30 y_3_h2 <= 0
 R20: 11.18033988749895 x_h2_c4 - 20 y_1_h2 - 20 y_2_h2 - 30 y_3_h2 <= 0
 R21: 15.8113883008419 x_h2_c5 - 20 y_1_h2 - 20 y_2_h2 - 30 y_3_h2 <= 0
 R22: 28.2842712474619 x_h2_c7 - 20 y_1_h2 - 20 y_2_h2 - 30 y_3_h2 <= 0
 R23: x_h2_c1 + x_h2_c2 + x_h2_c3 + x_h2_c4 + x_h2_c5 + x_h2_c7 - y_1_h2
   - 3 y_2_h2 - 4 y_3_h2 <= 0
 R24: x_h2_c1 - y_2_h2 - y_3_h2 = 0
 R25: x_h2_c3 - y_2_h2 - y_3_h2 = 0
 R26: y_1_h2 + y_2_h2 + y_3_h2 <= 1
 R27: 26.92582403567252 x_h3_c3 - 20 y_1_h3 - 20 y_2_h3 - 30 y_3_h3 <= 0
 R28: 20.6155281280883 x_h3_c4 - 20 y_1_h3 - 20 y_2_h3 - 30 y_3_h3 <= 0
 R29: 15.8113883008419 x_h3_c5 - 20 y_1_h3 - 20 y_2_h3 - 30 y_3_h3 <= 0
 R30: x_h3_c3 + x_h3_c4 + x_h3_c5 - y_1_h3 - 2 y_2_h3 - 3 y_3_h3 <= 0
 R31: x_h3_c3 - y_2_h3 - y_3_h3 = 0
 R32: y_1_h3 + y_2_h3 + y_3_h3 <= 1
 R33: 15 x_h4_c2 - 20 y_1_h4 - 20 y_2_h4 - 30 y_3_h4 <= 0
 R34: 10 x_h4_c6 - 20 y_1_h4 - 20 y_2_h4 - 30 y_3_h4 <= 0
 R35: 22.3606797749979 x_h4_c7 - 20 y_1_h4 - 20 y_2_h4 - 30 y_3_h4 <= 0
 R36: 25 x_h4_c8 - 20 y_1_h4 - 20 y_2_h4 - 30 y_3_h4 <= 0
 R37: x_h4_c2 + x_h4_c6 + x_h4_c7 + x_h4_c8 - 2 y_1_h4 - 2 y_2_h4
   - 3 y_3_h4 <= 0
 R38: x_h4_c6 - y_2_h4 - y_3_h4 = 0
 R39: y_1_h4 + y_2_h4 + y_3_h4 <= 1
 R40: 21.21320343559643 x_h5_c1 - 20 y_1_h5 - 20 y_2_h5 - 30 y_3_h5 <= 0
 R41: 11.18033988749895 x_h5_c2 - 20 y_1_h5 - 20 y_2_h5 - 30 y_3_h5 <= 0
 R42: 11.18033988749895 x_h5_c3 - 20 y_1_h5 - 20 y_2_h5 - 30 y_3_h5 <= 0
 R43: 15 x_h5_c4 - 20 y_1_h5 - 20 y_2_h5 - 30 y_3_h5 <= 0
 R44: 15.8113883008419 x_h5_c5 - 20 y_1_h5 - 20 y_2_h5 - 30 y_3_h5 <= 0
 R45: 20 x_h5_c6 - 20 y_1_h5 - 20 y_2_h5 - 30 y_3_h5 <= 0
 R46: 14.14213562373095 x_h5_c7 - 20 y_1_h5 - 20 y_2_h5 - 30 y_3_h5 <= 0
 R47: x_h5_c1 + x_h5_c2 + x_h5_c3 + x_h5_c4 + x_h5_c5 + x_h5_c6 + x_h5_c7
   - y_1_h5 - 2 y_2_h5 - 3 y_3_h5 <= 0
 R48: x_h5_c1 - y_2_h5 - y_3_h5 = 0
 R49: x_h5_c3 - y_2_h5 - y_3_h5 = 0
 R50: x_h5_c6 - y_2_h5 - y_3_h5 = 0
 R51: y_1_h5 + y_2_h5 + y_3_h5 <= 1
Bounds
 Constant = 1
Binaries
 x_h1_c1 x_h1_c2 x_h1_c3 x_h1_c4 x_h1_c5 x_h2_c1 x_h2_c2 x_h2_c3 x_h2_c4
 x_h2_c5 x_h2_c7 x_h3_c3 x_h3_c4 x_h3_c5 x_h4_c2 x_h4_c6 x_h4_c7 x_h4_c8
 x_h5_c1 x_h5_c2 x_h5_c3 x_h5_c4 x_h5_c5 x_h5_c6 x_h5_c7 y_1_h1 y_2_h1
 y_3_h1 y_1_h2 y_2_h2 y_3_h2 y_1_h3 y_2_h3 y_3_h3 y_1_h4 y_2_h4 y_3_h4
 y_1_h5 y_2_h5 y_3_h5
End
