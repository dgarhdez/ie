# Python for Data Analytics (PDA) Course Repository

This repository contains materials for the Python for Data Analytics course.

## Setup

This project uses [uv](https://github.com/astral-sh/uv) for fast Python package management.

### Prerequisites

Install uv:

```bash
# On macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or using pip
pip install uv
```

### Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd pda_mbads
   ```

2. Create a virtual environment called `pda_mbads` and install dependencies:

   ```bash
   # Create virtual environment named 'pda_mbads' and install packages
   uv venv pda_mbads
   source pda_mbads/bin/activate  # On Unix/macOS
   # pda_mbads\Scripts\activate   # On Windows
   uv pip install -r requirements.txt
   ```

   Or alternatively, use uv's sync command (creates `.venv` by default):

   ```bash
   # Create virtual environment and install packages
   uv sync
   ```

   Or create a custom named environment with sync:

   ```bash
   # Create environment named 'pda_mbads' and sync dependencies
   uv venv pda_mbads
   uv sync --venv pda_mbads
   ```

### Usage

Activate the virtual environment:

```bash
# uv automatically manages the virtual environment
uv run python your_script.py
```

Or activate manually:

```bash
source .venv/bin/activate  # On Unix/macOS
# .venv\Scripts\activate    # On Windows
```

### Dependencies

**Prerequisites:**

- **Python** (>=3.8): Required runtime environment

**Python Packages:**

- **pandas** (>=2.0.0): Data manipulation and analysis
- **numpy** (>=1.24.0): Numerical computing
- **plotly** (>=5.0.0): Interactive plotting
- **jupyter** (>=1.0.0): Jupyter notebook server
- **ipykernel** (>=6.0.0): IPython kernel for Jupyter
- **notebook** (>=6.0.0): Jupyter notebook interface

## Project Structure

```text
pda_mbads/
├── pda1/                    # Course Block 1 materials
│   ├── exams/              # Exam materials (ignored)
│   ├── homework/           # Homework assignments
│   ├── notebooks/          # Jupyter notebooks
│   └── slides/             # Presentation slides
├── pda2/                   # Course Block 2 materials
├── requirements.txt        # Package dependencies
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## Course Information

See `pda1/syllabus.md` for detailed course syllabus and session information.
