# Graph Colouring — ADS Practical Session

Given a graph and `k` colours, assign a colour to every node such that no two adjacent nodes share the same colour.

## Setup

**1. Clone the repo**
```bash
git clone <repo-url>
cd <repo-name>
```

**2. Create a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install matplotlib
```

**4. Run**
```bash
python3 graph_colouring.py
```

## Files

| File | Description |
|------|-------------|
| `graph_colouring.py` | Main file — this is what we fill in during the session |
| `graph_draw.py` | Visualisation helper — pre-written, no need to touch |
| `benchmark.py` | Speed comparison between solvers |