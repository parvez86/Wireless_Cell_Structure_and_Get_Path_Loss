import math


class HataModel:
    def __init__(self, carrier_frequency, height_transmitter, height_receiver, link_distance, city_size_val, area_type_val):
        self.carrier_freq = carrier_frequency
        self.height_transmitter = height_transmitter
        self.height_receiver = height_receiver
        self.link_distance = link_distance
        self.city_size_val = city_size_val
        self.area_type_val = area_type_val
        self.corr_factor = 0.0
        self.antenna_corr_factor()
        self.path_loss = 0.0
        self.get_path_loss()
        self.count_loss_variance()

    # Antenna height correlation factor
    def antenna_corr_factor(self):
        if self.city_size_val == 1:
            self.corr_factor = (0.8 + ((1.1 * math.log10(self.carrier_freq) - 0.7)*self.height_receiver) - (1.56 * math.log10(self.carrier_freq)))

        else:
            if (self.carrier_freq >= 150) and (self.carrier_freq <= 200):
                self.corr_factor = (8.29 * (math.pow(math.log10(1.54 * self.height_receiver), 2))) - 1.1
            else:
                self.corr_factor = (3.2 * (math.pow(math.log10(11.75 * self.height_receiver), 2))) - 4.97

    # Urbane path loss
    def get_path_loss(self):
        self.path_loss = 69.55 + (26.16 * math.log10(self.carrier_freq)) - (13.82 * math.log10(self.height_transmitter)) - self.corr_factor + ((44.9 - (6.55 * math.log10(self.height_transmitter))) * math.log10(self.link_distance))

    # Additional path loss for Sub urban and Open Area
    def count_loss_variance(self):
        diff_loss = 0.0
        if self.area_type_val == 2:
            diff_loss = (2 * math.pow(math.log10((self.carrier_freq/28)), 2)) + 5.4
        elif self.area_type_val == 3:
            diff_loss = (4.78 * math.pow(math.log10(self.carrier_freq), 2)) - (18.733 * math.log10(self.carrier_freq)) + 40.94

        self.path_loss -= diff_loss
