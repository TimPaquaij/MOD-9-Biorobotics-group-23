import ulab as np
import math

class Angles (object):

    def __init__(self):
        self.psi0 = np.array([0,0])
        self.psiEE0 = self.psi0

        self.psiB1 = np.array([-173.2051, -100])
        self.psiB2 = np.array([173.2051, -100])
        self.psiB3 = np.array([0, 200])

        self.dMotoAng = np.array([1.29239258, 3.3867875, -0.80200278])

        self.lastMotoang = self.dMotoAng
        return

    def go_moving(self,amount):
        if abs(amount) == 1:
            self.go_horizontal(amount)
        elif abs(amount) == 2:
            self.go_vertical(amount/2)
        else:
            self.change = np.array([0,0,0])
            self.dMotoAng = self.lastMotoang
        print(self.dMotoAng)
        print(self.change)
        return self.change

    def go_vertical(self, amount):
        self.psiEE0[1] += amount
        self.change = self.calc_moto_angle_change()
        self.lastMotoang = self.dMotoAng
        return


    def go_horizontal(self, amount):
        self.psiEE0[0] += amount
        self.change = self.calc_moto_angle_change()
        self.lastMotoang = self.dMotoAng
        return
    

    def calc_moto_angle_change(self):

        #calculating the needed angle change to reach desired angles

        vec_a1, vec_a2, vec_a3 = self.calc_vec_a()

        self.dMotoAng = self.calc_alpha_des( self.calc_alpha(self.calc_lenght_a(vec_a1, vec_a2, vec_a3)),      self.calc_vec_alpha(vec_a1, vec_a2, vec_a3, self.calc_lenght_a(vec_a1, vec_a2, vec_a3)) )

        return np.array([self.dMotoAng[0] - self.lastMotoang[0], self.dMotoAng[1] - self.lastMotoang[1], self.dMotoAng[2] - self.lastMotoang[2]])
    

    def calc_alpha_des(self, alpha, vec_alpha):
        
        #calculating the desired motor angle in respect to x axes from psi0
        
        return (alpha + vec_alpha)
    

    def calc_vec_alpha(self, vec_a1, vec_a2, vec_a3, lenght_a): 
        
        #calculating vector a's orientation in respect to x axes from psi0
        
        self.vecAlpha = np.array([0, 0, 0])
        
        if vec_a1[1] >= 0:
            self.vecAlpha[0] = math.acos(vec_a1[0]/lenght_a[0])
        else:
            self.vecAlpha[0] = -(math.acos(vec_a1[0]/lenght_a[0]))
        
        if vec_a2[1] >= 0:
            self.vecAlpha[1] = math.acos(vec_a2[0]/lenght_a[1])
        else:
            self.vecAlpha[1] = -(math.acos(vec_a2[0]/lenght_a[1]))

        if vec_a3[1] >= 0:
            self.vecAlpha[2] = math.acos(vec_a3[0]/lenght_a[2])
        else:
            self.vecAlpha[2] = -(math.acos(vec_a3[0]/lenght_a[2]))
            
        return self.vecAlpha


    def calc_alpha(self, lenght_a): 
        
        #calculating angle alpha (on motorjoint) from the triangle beeing built by the arms and vector a
        
        return np.array([math.acos(lenght_a[0]/160), math.acos(lenght_a[1]/160), math.acos(lenght_a[2]/160)])


    def calc_lenght_a(self, vec_a1, vec_a2, vec_a3): 

        #calculating the vectors lenght
        
        return np.array([math.sqrt(vec_a1[0]**2 + vec_a1[1]**2), math.sqrt(vec_a2[0]**2 + vec_a2[1]**2), math.sqrt(vec_a3[0]**2 + vec_a3[1]**2)])


    def calc_vec_a(self): 
        
        #calculating the vectors from basejoints to sunjoints
        
        self.psiEE1 = self.psiEE0 + np.array([-73.6122, -42.5])
        self.psiEE2 = self.psiEE0 + np.array([73.6122, -42.5])
        self.psiEE3 = self.psiEE0 + np.array([0, 85])

        return (self.psiEE1 - self.psiB1), (self.psiEE2 - self.psiB2), (self.psiEE3 - self.psiB3)

    
   

