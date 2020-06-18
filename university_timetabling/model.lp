\ Model University Timetabling
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  0.1 y_curr_(c0001_c0002)_(0,0) + 0.1 y_curr_(c0002_c0003)_(0,0)
   + 0.1 y_curr_(c0001_c0003)_(0,0) + 0.1 y_days_c0001 + 0.1 y_days_c0002
   + 0.1 y_days_c0003 + 0.1 y_days_c0004
Subject To
 R0: x_c0001_(0,0) = 1
 R1: - z_c0001_0 + x_c0001_(0,0) <= 0
 R2: - z_c0001_0 + x_c0001_(0,0) >= 0
 R3: - z_c0001_0 - y_days_c0001 <= -1
 R4: x_c0002_(0,0) = 1
 R5: - z_c0002_0 + x_c0002_(0,0) <= 0
 R6: - z_c0002_0 + x_c0002_(0,0) >= 0
 R7: - z_c0002_0 - y_days_c0002 <= -1
 R8: x_c0003_(0,0) = 1
 R9: - z_c0003_0 + x_c0003_(0,0) <= 0
 R10: - z_c0003_0 + x_c0003_(0,0) >= 0
 R11: - z_c0003_0 - y_days_c0003 <= -1
 R12: x_c0004_(0,0) = 1
 R13: - z_c0004_0 + x_c0004_(0,0) <= 0
 R14: - z_c0004_0 + x_c0004_(0,0) >= 0
 R15: - z_c0004_0 - y_days_c0004 <= -1
 R16: x_c0001_(0,0) + x_c0002_(0,0) - y_curr_(c0001_c0002)_(0,0) <= 1
 R17: x_c0002_(0,0) + x_c0003_(0,0) - y_curr_(c0002_c0003)_(0,0) <= 1
 R18: x_c0001_(0,0) + x_c0003_(0,0) - y_curr_(c0001_c0003)_(0,0) <= 1
Bounds
Binaries
 z_c0001_0 z_c0002_0 z_c0003_0 z_c0004_0 x_c0001_(0,0) x_c0002_(0,0)
 x_c0003_(0,0) x_c0004_(0,0)
Generals
 y_curr_(c0001_c0002)_(0,0) y_curr_(c0002_c0003)_(0,0)
 y_curr_(c0001_c0003)_(0,0) y_days_c0001 y_days_c0002 y_days_c0003
 y_days_c0004
End
