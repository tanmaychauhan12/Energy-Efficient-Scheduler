# Energy-Efficient-Scheduler
> OS Project (Course PBL)

## Team Roles and Responsibilities

### - Tanmay Chauhan (Team Lead & Simulator Architect)
  - Primary Role: Designs and builds the core simulation engine—the "world" where the CPU and processes exist. He is responsible for the main time loop, process state transitions, and the energy consumption model.
- OS Algorithm: Implements the Round Robin (RR) scheduler. This is a foundational, preemptive algorithm that introduces the concept of a time quantum.

### - Riya (Performance Algorithm Specialist)
  - Primary Role: Focuses on a classic high-performance scheduling algorithm to serve as a key benchmark. She will also be responsible for implementing the core performance metrics (Turnaround Time, Wait Time).
- OS Algorithm: Implements the Shortest Remaining Time First (SRTF) scheduler. This is a more complex preemptive algorithm that requires constantly checking for shorter jobs.

### - Palak Bisht (Priority & UI Integration Lead)
  - Primary Role: Handles scheduling based on process priority and leads the integration of the backend simulator with the frontend UI.
- OS Algorithm: Implements the Preemptive Priority scheduler. This algorithm introduces the concept of process priority levels and how they trigger context switches.

### - Muskan Bhatt (Energy-Aware Algorithm & Data Analyst)
  - Primary Role: Develops the project's central innovation—the custom energy-aware scheduler. She is also responsible for creating test workloads and analyzing the final data to prove the project's hypothesis.
- OS Algorithm: Implements the Custom Energy-Aware (CEA) scheduler, using the composite score to balance performance and power.

## Motivation
Modern devices and data centers must balance performance with energy use. Traditional CPU schedulers (RR, SJF, Priority) ignore energy as a primary objective, causing unnecessary power draw and higher costs. This project builds an energy-aware scheduler that prioritizes processes using a composite score (estimated energy-to-finish, user priority, deadline urgency, and aging). It also uses adaptive time quanta, low-power state modeling, and a simple DVFS core model. A
Streamlit GUI will let users run experiments, view Gantt/energy timelines, and compare against standard baselines. The result is a reproducible tool to explore energy–performance tradeoffs

The Vision: An interactive web application where a user can upload a list of computing tasks, run them through four different CPU schedulers (three classic, one custom energy-aware), and instantly see a visual comparison of performance vs. energy consumption.


## Phase 0: Foundation & Setup (Target: Week 1)
Goal: Establish a professional project structure and a collaborative environment.
 1. Project Management (Tanmay):
    - Create a private repository on GitHub named Energy-Efficient-Scheduler.
    - Invite all team members as collaborators.
    - Set up a "Projects" board on GitHub with columns: Backlog, To-Do, In Progress, Done. Populate the To-Do list with the tasks from Phases 0 and 1.
 2. Environment Setup (Everyone):
    - Install Python, Git, and VS Code.
    - Clone the new repository: git clone <repository_url>
    - Create and activate a virtual environment:
