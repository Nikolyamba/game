import time

class Time:
    def __init__(self):
        self.start_time = None
        self.time_running = False

    def start(self):
        self.time_running = True
        self.start_time = time.time()

    # def stop(self):
    #     self.time_running = False
    #
    # def reset(self):
    #     self.start_time = time.time()

    def time_passed(self):
        if self.time_running and self.start_time is not None:
            return int(time.time() - self.start_time)
        return 0

    def get_sec_min_hrs(self, time_passed):
        sec = time_passed % 60
        min = time_passed // 60 % 60
        hrs = time_passed // 3600
        return f"{sec:02d}", f"{min:02d}", f"{hrs:02d}"
