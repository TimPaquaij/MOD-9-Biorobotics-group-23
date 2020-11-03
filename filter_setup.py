from filter import Filter


class FilterSetup(object):
    def __init__(self):
        self.sample_frequency = 400

        self.Adata= []
        self.Normdata = []

        self.Ndata = []
        self.Hdata = []
        self.Absdata = []
        #self.Ydata = []
        

        """
        Notch filter
        """
        na0 = 1.0
        na1 = -1.3985
        na2 = 0.9778
        nb0 = 0.9889
        nb1 = -1.3985
        nb2 = 0.9889
        """
        High-Pass filter
        """
        ha0 = 1.0
        ha1 = -1.8695
        ha2 = 0.8794
        hb0 = 0.9159
        hb1 = -1.8318
        hb2 = 0.9159
        """
        Low-Pass filter
        """
        la0 = 1.0
        la1 = 0.5136
        la2 = 0.2706
        lb0 = 0.4359
        lb1 = 0.8718
        lb2 = 0.4359


        """
        filters
        """
        self.NotchFilter=Filter(na0, na1, na2, nb0, nb1, nb2)
        self.HighPassFilter=Filter(ha0, ha1, ha2, hb0, hb1, hb2)
        self.LowPassFilter=Filter(la0, la1, la2, lb0, lb1, lb2)

        return
    
    def run(self, data):
        self.data=data

        

        self.Ndata=self.NotchFilter.filter(self.sample_frequency, self.data)
        self.Hdata=self.HighPassFilter.filter(self.sample_frequency, self.Ndata)

        self.Absdata = []
        for num in self.Hdata:
            abso = abs(num)
            self.Absdata.append(abso)
        self.Ldata=self.LowPassFilter.filter(self.sample_frequency, self.Absdata)
        return(self.Ldata)

    

