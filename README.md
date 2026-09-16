# Purnima Pathak

**Measurement-first ML / NLP researcher** — data-centric interpretability, model reliability, and
on-device efficiency. I study *how the data and interventions applied to a model change its behavior*
(memorization, factuality), and I hold my own results to a hard standard: I report nulls and correct
my own false positives.

🔗 [Website](https://pupa3066.github.io) · [LinkedIn](https://www.linkedin.com/in/purnima-pathak-86597b296/)

## Featured research

**[quant-memorization-study](https://github.com/pupa3066/quant-memorization-study)** — Does
quantization change what a model memorizes and how reliably it recalls facts? Uses efficiency
(INT8/INT4) as the independent variable and model behavior as the dependent variable, extending
black-box memorization probing (Ravichander et al., arXiv:2503.12072). Result across **6 models**:
INT4 leaves factual accuracy unchanged (replicated null); memorization is driven by model scale, not
precision. A pilot false positive was caught and corrected by scaling — measure, don't assert.

**[context-configuration-builder](https://github.com/pupa3066/context-configuration-builder)** —
Turns a published negative result on repository context files (ETH, arXiv:2602.11988) into a
pre-registered controlled study: does access-pattern-tiered context recover coding-agent task success
at lower cost? Real SWE-bench test-execution grading + from-scratch statistics (McNemar, bootstrap
CIs, non-inferiority, CMH, permutation). Shares one principle with the quantization work — *spend the
expensive resource only where it changes behavior* — wired together in code.

## Approach
Pre-register hypotheses · use only measured facts, label everything unverified · build the instrument
correctly (I document the bugs) · prefer an honest null or a characterized tradeoff over an inflated number.

## Background
M.S. Telecommunications, University of Colorado Boulder (2019). Prior: 5 yrs at Cisco (VPN dataplane
PKI/AAA, TLS/DTLS traffic analysis), systems/migration engineering (Unisys, TATA Power). Now
independent research in hardware-efficient ML + NLP interpretability.
