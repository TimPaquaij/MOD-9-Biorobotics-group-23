from biquad import Biquad

class Biquad_setup(object):
    def __init__(self):

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
        ha1 = -1.8696
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

        """self.NotchFilter=Biquad((na0, na1, na2), (nb0, nb1, nb2))
        self.HighPassFilter=Biquad((ha0, ha1, ha2), (hb0, hb1, hb2))
        self.LowPassFilter=Biquad((la0, la1, la2), (lb0, lb1, lb2))"""
        self.NotchFilter=Biquad((1.0, -1.3985, 0.9778), (0.9889, -1.3985, 0.9889))
        self.HighPassFilter=Biquad((1.0, -1.8696, 0.8794), (0.9159, -1.8318, 0.9159))
        self.LowPassFilter=Biquad((1.0, 0.5136, 0.2706), (0.4359, 0.8718, 0.4359))

    def run(self, data):
        self.data=data

        self.Ndata=self.NotchFilter.step(self.data)
        self.Hdata=self.HighPassFilter.step(self.Ndata)

        self.Absdata = 0

        """for num in self.Hdata:
            abso = abs(num)
            self.Absdata.append(abso)"""
        self.Absdata = abs(self.Hdata)
        self.Ldata=self.LowPassFilter.step(self.Absdata)
        return(self.Ldata)