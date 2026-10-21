# quant-lab

**Exploring quantitative finance through numerical methods, Monte Carlo simulations, and high-performance computing.**

An evolving, reproducible portfolio of numerical finance projects, starting with Monte Carlo pricing and expanding toward numerical optimization, CPU/GPU performance engineering, and systematic strategy research.

## First project: Monte Carlo option pricing

The initial goal is to price European options by simulating geometric Brownian motion, validate against the Black–Scholes formula, measure sampling error and convergence, and then explore CPU and GPU optimization.

**Status:** project scaffolding ready; pricing implementation not yet started. See [the roadmap](docs/ROADMAP.md).

## Getting started

Requirements: Python 3.11+ and Git.

```bash
git clone https://github.com/GarridoIgnacioM/quant-lab.git
cd quant-lab
python -m venv .venv
```

Activate the environment:

- Windows PowerShell: `.venv\Scripts\Activate.ps1`
- Linux/macOS: `source .venv/bin/activate`

Install and check:

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m pytest
ruff check .
```

## Layout

```text
src/quant_lab/     Python library source
tests/             Automated tests
docs/              Roadmap and technical documentation
.github/workflows/ CI checks
```

Additional `experiments/`, `benchmarks/`, and `results/` directories will be created when they contain reproducible work.

## Private data and reproducibility

Local `private/` and `tracking/` directories are ignored by Git, along with `.env` files and generated output. Do **not** commit API keys, personal account details, or confidential datasets. Note that `.gitignore` does not remove anything already committed; inspect staged changes with `git status` before every push.

Public benchmark configurations and synthetic example datasets should remain versioned when they help others reproduce the results.

## Disclaimer

This repository is for research and learning. It does not constitute investment advice.
