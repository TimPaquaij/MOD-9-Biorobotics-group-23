import numpy as np
import math



Q1 = -0.25
Q2 = Q1 + 1.5
C= 150.455
B= 80
D= np.array([B*math.sin(math.radians(30)), B*math.cos(math.radians(30)), 0])
L0=np.array([-173.2071, -100.0012])
R0=np.array([173.2071, -100.0012])
T0=np.array([0, 200.0023])
Dp=np.array([10, 10, 0])
Ja1 =np.array([0, 0, 1])
Ja2 =np.array([0, 0, 1])
LA=np.array([B*math.cos(math.radians(Q1))+L0[0], B*math.sin(math.radians(Q1))+L0[1], 0])
L1=np.array([B*math.cos(math.radians(Q2))+LA[0], B*math.sin(math.radians(Q2))+LA[1], 0])
EP=np.array([L1[0]+D[0], L1[1]+D[1], 0])


while EP[0] != Dp[0] or EP[1]!= Dp[1]:
   
    LA=np.array([B*math.cos(math.radians(Q1))+L0[0], B*math.sin(math.radians(Q1))+L0[1], 0])
    L1=np.array([B*math.cos(math.radians(Q2))+LA[0], B*math.sin(math.radians(Q2))+LA[1], 0])
    EP=np.array([L1[0]+D[0], L1[1]+D[1], 0])
    
    H00= np.array([EP[0], EP[1], 0])
   
    Lv1 = np.array([L0[0], L0[1], 0])
    Lv2 = np.array([LA[0], LA[1], 0])
    Lg1 = np.cross(Lv1, Ja1)
    Lg2 = np.cross(Lv2, Ja2)

    
    DeltaP = (Dp-H00)
    Deltaf =numerical.flip(DeltaP, axis=0)
    print(Deltaf)
    LJa = np.array([[Lg1[0], Lg2[0], 0], [Lg1[0], Lg2[1], 0], [Lg1[0], Lg2[1], 0]])
    LInja = linalg.inv(LJa)
    LVel = LInja * DeltaP
    Q1 =Q1+(LVel[0])
    Q2 =Q2+(LVel[1])
    



