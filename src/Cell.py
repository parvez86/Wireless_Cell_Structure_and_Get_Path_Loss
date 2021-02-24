import math


class Cell:
    def __init__(self, total_area, total_number_of_traffic_channels, radius_of_cell, frequency_reuse_factor):
        self.total_area = total_area
        self.total_number_traffic_channels = total_number_of_traffic_channels
        self.radius_of_cell = radius_of_cell
        self.frequency_reuse_factor = frequency_reuse_factor
        self.number_of_cells = self.get_number_of_cells()
        self.number_of_channels_per_cell = self.get_number_of_channels_per_cell()
        self.total_capacity = self.get_total_capacity()
        self.total_number_of_possible_concurrent_call = self.get_total_number_of_concurrent_call()

    # Number of cells required
    def get_number_of_cells(self):
        area_of_each_cell = float(1.5 * math.sqrt(3)*math.pow(self.radius_of_cell, 2))
        return int(round(self.total_area/area_of_each_cell, 0))

    # Number of channels per cell
    def get_number_of_channels_per_cell(self):
        return int(round(self.total_number_traffic_channels/self.frequency_reuse_factor, 0))

    # Total channel capacity
    def get_total_capacity(self):
        return int(round(self.number_of_cells * self.number_of_channels_per_cell,0))

    # Total number of possible concurrent call
    def get_total_number_of_concurrent_call(self):
        return self.total_capacity
