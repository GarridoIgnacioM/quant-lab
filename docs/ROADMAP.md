# Roadmap

## Phase 1 — Monte Carlo foundations
- [ ] Implement a reproducible pseudorandom number generation interface with explicit seeds.
- [ ] Build a vectorized European option pricer under geometric Brownian motion.
- [ ] Compare Monte Carlo results against the Black–Scholes analytical benchmark.
- [ ] Quantify sampling error, confidence intervals, and convergence rates.
- [ ] Add unit tests and document assumptions.

## Phase 2 — Performance engineering
- [ ] Benchmark vectorized NumPy and compiled CPU implementations.
- [ ] Profile runtime and memory use.
- [ ] Explore GPU acceleration with an appropriate CUDA stack.
- [ ] Publish reproducible CPU/GPU comparisons, including hardware specifications.

## Phase 3 — Strategies and simulated portfolio
- [ ] Explore data quality and avoid look-ahead bias.
- [ ] Establish a reproducible backtesting framework.
- [ ] Define transaction costs, risk metrics and a virtual portfolio.
- [ ] Keep personal journals and account-specific information in ignored local paths.

## Principles
Prioritize correctness before performance, reproducible experiments, clear benchmarks and modest claims about financial performance. This repository is educational and experimental, not financial advice.
