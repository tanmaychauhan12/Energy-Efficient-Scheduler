# Energy-Efficient-Scheduler
OS Project (Course Work)

# Team Roles and Responsibilities

# - Tanmay Chauhan (Team Lead & Simulator Architect)
  - Primary Role: Designs and builds the core simulation engine—the "world" where the CPU and processes exist. He is responsible for the main time loop, process state transitions, and the energy consumption model.
    - OS Algorithm: Implements the Round Robin (RR) scheduler. This is a foundational, preemptive algorithm that introduces the concept of a time quantum.

# - Riya (Performance Algorithm Specialist)
  - Primary Role: Focuses on a classic high-performance scheduling algorithm to serve as a key benchmark. She will also be responsible for implementing the core performance metrics (Turnaround Time, Wait Time).
    - OS Algorithm: Implements the Shortest Remaining Time First (SRTF) scheduler. This is a more complex preemptive algorithm that requires constantly checking for shorter jobs.

# - Palak Bisht (Priority & UI Integration Lead)
  - Primary Role: Handles scheduling based on process priority and leads the integration of the backend simulator with the frontend UI.
    - OS Algorithm: Implements the Preemptive Priority scheduler. This algorithm introduces the concept of process priority levels and how they trigger context switches.

# - Muskan Bhatt (Energy-Aware Algorithm & Data Analyst)
    - Primary Role: Develops the project's central innovation—the custom energy-aware scheduler. She is also responsible for creating test workloads and analyzing the final data to prove the project's hypothesis.
    - OS Algorithm: Implements the Custom Energy-Aware (CEA) scheduler, using the composite score to balance performance and power.
