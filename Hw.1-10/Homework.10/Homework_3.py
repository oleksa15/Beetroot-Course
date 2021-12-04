# coding = UTF-8
CHANNELS = ["BBC", "Discovery", "TV100"]

class TV_Controller:
    number_current_channel = 0

    def __init__(self, channels):
        if len(channels) == 0:
            print("No chanels")
        else:
            self.channels = channels


    def first_channel(self):
        self.number_current_channel = 0
        return self.channels[0]

    def last_channel(self):
        self.number_current_channel = len(self.channels) - 1
        return self.channels[-1]

    def previous_channel(self):
        self.number_current_channel -= 1
        if self.number_current_channel < 0:
            self.number_current_channel = len(self.channels) - 1
        return self.channels[self.number_current_channel]

    def next_channel(self):
        self.number_current_channel += 1
        if self.number_current_channel >= len(self.channels):
            self.number_current_channel = 0
        return self.channels[self.number_current_channel]

    def current_channel(self):
        return self.channels[self.number_current_channel]

    def is_exist(self, number_or_name):
        if type(number_or_name) == int:
            result = 0 < number_or_name < len(self.channels)
        else:
            result = number_or_name in self.channels
        return "Yes" if result else "No"

    def turn_channel(self, number_of_channel):
        if self.is_exist(number_of_channel):
            return self.channels
        else:
            "No such channel"
