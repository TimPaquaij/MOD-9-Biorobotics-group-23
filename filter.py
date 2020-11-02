
class Filter(object):
    def __init__(self, a0, a1, a2, b0, b1, b2):
        
        """
        Definitions
        """
        self.a0 = a0
        self.a1 = a1
        self.a2 = a2

        self.b0 = b0
        self.b1 = b1
        self.b2 = b2


    def filter(self, sample_frequency, data):
        """
        Definitions
        """
        self.sample_frequency = sample_frequency
        self.data = data
        self.Ydata = []

        """
        Defining Time
        """
        self.data_length = len(self.data)
        self.duration = self.data_length/self.sample_frequency
        self.data_range = range(1,self.data_length+1,1)
        self.time= []

        for num in self.data_range:
            time_unit = num/self.sample_frequency
            self.time.append(time_unit)

        """
        Delay Register
        """
        self.Yd = [0.0,0.0]
        self.Xd = [0.0,0.0]
        self.i = 0

        while self.i<self.data_length:
            """
            Transfer function
            """

            X=self.data[self.i]
            Y = (self.b0*X+self.b1*self.Xd[0]+self.b2*self.Xd[1]-self.a1*self.Yd[0]-self.a2*self.Yd[1])/self.a0

            self.Ydata.append(Y)

            """
            change the history arrays
            """
            self.Xd[1]=self.Xd[0]
            self.Xd[0]=X

            self.Yd[1]=self.Yd[0]
            self.Yd[0]=Y

            self.i += 1
        return(self.Ydata)

