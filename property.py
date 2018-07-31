from collections import deque


class Leg:
    def __init__(self, rate=None, time=None, distance=None):
        self._changes = deque(maxlen=2)

        self.rate = rate
        self.time = time
        self.distance = distance

    @property
    def rate(self):
        return self._rate

    @property
    def time(self):
        return self._time

    @property
    def distance(self):
        return self._distance

    @rate.setter
    def rate(self, value):
        self._rate = value
        if value:
            self._calculate('rate')

    @time.setter
    def time(self, value):
        self._time = value
        if value:
            self._calculate('time')

    @distance.setter
    def distance(self, value):
        self._distance = value
        if value:
            self._calculate('distance')

    def calc_distance(self):
        self._distance = self._time * self._rate

    def calc_time(self):
        self._time = self._distance / self._rate

    def calc_rate(self):
        self._rate = self._distance / self._time

    def _calculate(self, change):
        if change not in self._changes:
            self._changes.append(change)
        compute = {'rate', 'time', 'distance'} - set(self._changes)
        if len(compute) == 1:
            name = compute.pop()
            method = getattr(self, 'calc_'+name)
            method()
