class FrequencyTracker:

    def __init__(self):
        self.count = {}      
        self.freq = {}      

    def _inc_freq(self, f):
        self.freq[f] = self.freq.get(f, 0) + 1

    def _dec_freq(self, f):
        if f > 0:
            self.freq[f] -= 1
            if self.freq[f] == 0:
                del self.freq[f]

    def add(self, number: int) -> None:
        old = self.count.get(number, 0)
        new = old + 1
        self.count[number] = new
        self._dec_freq(old)
        self._inc_freq(new)

    def deleteOne(self, number: int) -> None:
        if number not in self.count:
            return
        old = self.count[number]
        new = old - 1
        self._dec_freq(old)
        if new == 0:
            del self.count[number]
        else:
            self.count[number] = new
            self._inc_freq(new)

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq.get(frequency, 0) > 0
