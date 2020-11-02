from filter import Filter


class FilterSetup(object):
    def __init__(self):
        self.sample_frequency = 700

        self.Adata= []
        self.Normdata = []

        self.Notchdata = []
        self.Highdata = []
        self.Absdata = []
        #self.Ydata = []

        """
        Notch filter
        """
        na0 = 1.0
        na1 = -1.7905
        na2 = 0.9873
        nb0 = 0.9936
        nb1 = -1.7905
        nb2 = 0.9936
        """
        High-Pass filter
        """
        ha0 = 1.0
        ha1 = -1.2084
        ha2 = 0.4722
        hb0 = 0.6549
        hb1 = -1.3098
        hb2 = 0.6549
        """
        Low-Pass filter
        """
        la0 = 1.0
        la1 = -1.8240
        la2 = 0.8414
        lb0 = 0.0043
        lb1 = 0.0085
        lb2 = 0.0043


        """
        filters
        """
        self.NotchFilter=Filter(na0, na1, na2, nb0, nb1, nb2)
        self.HighPassFilter=Filter(ha0, ha1, ha2, hb0, hb1, hb2)
        self.LowPassFilter=Filter(la0, la1, la2, lb0, lb1, lb2)

        return
    
    def run(self, data):
        self.data=data
        self.mean_data = sum(self.data)/len(self.data)

        self.meanandnormalize()

        self.data=self.NotchFilter.filter(self.sample_frequency, self.data)
        self.data=self.HighPassFilter.filter(self.sample_frequency, self.data)
        
        self.Adata = []

        for num in self.data:
            abso = abs(num)
            self.Adata.append(abso)
        self.data=self.LowPassFilter.filter(self.sample_frequency, self.Adata)
        return(self.data)

    def meanandnormalize(self):
        print("mean...")
        for num in self.data:
            n_unit_data = num-(self.mean_data)
            self.Adata.append(n_unit_data)

        max_data = max(self.Adata)
        self.data = []
        print("normalize...")

        for num in self.Adata:
            unit = num/max_data
            self.data.append(unit)
        return


