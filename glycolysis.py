import time
import random


dG_dt = 1  # µM/ms
dGin_dt = 0 # µM/ms
dATP_dt = 0 # µM/ms


# Initial state vector:
class Conc:
    __slots__ = ('G', 'ADP', 'ATP')
    def __init__(self, G, ADP, ATP):
        self.G = G
        self.ADP = ADP
        self.ATP = ATP
    def __str__(self):
        return f'G:{self.G};ADP:{self.ADP},ATP:{self.ATP}'
    def check_ATP(self):
        if self.ATP < 1:
            return False
        return True


c = Conc(10.0, 100.0, 1000.0)  # µM
ms0 = time.perf_counter_ns()


def loop():
    global ms0, dG_dt, dGin_dt, dATP_dt
    while True:
        ms = (time.perf_counter_ns() - ms0) / 1_000_000
        if ms < 1:
            continue
        ms0 = ms
        c.G += dGin_dt
        if c.G > dG_dt and c.ADP > dG_dt*2:
            c.G -= dG_dt
            c.ADP -= dG_dt*2
            c.ATP += dG_dt*2
        else:
            pass
        dATP_dt = random.uniform(0.5, 2.0)
        dGin_dt = dATP_dt/2
        if c.ATP > dATP_dt:
            c.ADP += dATP_dt
            c.ATP -= dATP_dt
        else:
            print("Energy Failure")
            quit()
        print(c)


if __name__ == "__main__":
    loop()
