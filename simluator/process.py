class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time
        self.completion_time = None
        self.start_time = None
        self.finish_time = None

    def __repr__(self):
        return (f"Process(pid={self.pid}, arrival={self.arrival_time}, "
                f"burst={self.burst_time}, priority={self.priority})")