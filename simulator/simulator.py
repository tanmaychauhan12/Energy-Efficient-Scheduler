# simulator/cpu_simulator.py
import collections
import copy  # IMPORTANT: Import the copy module

class CPUSimulator:
    """Manages the simulation environment, time, and processes."""
    def __init__(self, processes):
        # Store the original, untouched list of processes
        self.initial_processes = sorted(processes, key=lambda p: p.arrival_time)
        
        # --- These variables will be RESET for each simulation run ---
        self.ready_queue = collections.deque()
        self.finished_processes = []
        self.gantt_chart = [] 
        self.current_time = 0
        self.current_process_on_cpu = None
        self.time_quantum_slice = 0 
        self.total_energy_consumed = 0
        # --- End of reset variables ---

        # Energy Model
        self.POWER_BUSY = 10 
        self.POWER_IDLE = 1 

    def run(self, scheduler):
        """Runs the entire simulation with a given scheduling algorithm."""
        
        # --- FIX: Reset the simulator's state for a clean run ---
        process_pool = [copy.deepcopy(p) for p in self.initial_processes]
        self.finished_processes = []
        self.gantt_chart = []
        self.current_time = 0
        self.current_process_on_cpu = None
        self.ready_queue.clear()
        self.total_energy_consumed = 0
        scheduler.sim = self # Link the scheduler to this specific run's simulator instance
        # --- End of FIX ---

        while process_pool or self.ready_queue or self.current_process_on_cpu:
            # 1. Add newly arrived processes to the ready queue
            while process_pool and process_pool[0].arrival_time <= self.current_time:
                self.ready_queue.append(process_pool.pop(0))

            # 2. Let the scheduler make a decision
            scheduler.schedule()

            # 3. Update process execution and energy
            if self.current_process_on_cpu:
                if self.current_process_on_cpu.start_time == -1:
                    self.current_process_on_cpu.start_time = self.current_time

                self.gantt_chart.append(self.current_process_on_cpu.pid)
                self.current_process_on_cpu.remaining_time -= 1
                self.total_energy_consumed += self.POWER_BUSY
            else:
                self.gantt_chart.append("Idle")
                self.total_energy_consumed += self.POWER_IDLE

            # 4. Handle process completion
            if self.current_process_on_cpu and self.current_process_on_cpu.remaining_time == 0:
                self.current_process_on_cpu.finish_time = self.current_time + 1
                self.finished_processes.append(self.current_process_on_cpu)
                self.current_process_on_cpu = None

            # 5. Update wait times for all processes in the ready queue
            for proc in self.ready_queue:
                proc.wait_time += 1

            self.current_time += 1

        # Final metrics calculation
        self._calculate_final_metrics()
        
        # The run method now returns its results instead of printing
        return self.finished_processes, self.gantt_chart, self.total_energy_consumed

    def _calculate_final_metrics(self):
        for proc in self.finished_processes:
            proc.turnaround_time = proc.finish_time - proc.arrival_time


