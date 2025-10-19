# algorithms/round_robin.py
class RoundRobin:
    def __init__(self, time_quantum=4):
        self.sim = None
        self.time_quantum = time_quantum

    def schedule(self):
        if self.sim.current_process_on_cpu:
            self.sim.time_quantum_slice += 1
            if self.sim.time_quantum_slice >= self.time_quantum:
                process_to_move = self.sim.current_process_on_cpu
                self.sim.current_process_on_cpu = None
                self.sim.ready_queue.append(process_to_move)

        if self.sim.current_process_on_cpu is None and self.sim.ready_queue:
            self.sim.current_process_on_cpu = self.sim.ready_queue.popleft()
            self.sim.time_quantum_slice = 0