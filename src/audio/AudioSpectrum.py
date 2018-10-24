# The class AudioSpectrum is responsible for storing information about the decoded audio spectrum.


class AudioSpectrum:

    def __init__(self, test_int):
        self.test_int = test_int

    # ========== TEST FUNCTIONS ==========

    def get_int(self):
        return self.test_int

    def set_int(self, test_int):
        self.test_int = test_int

    def print_int(self):
        print(self.test_int)
