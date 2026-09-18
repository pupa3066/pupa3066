# Purnima Pathak

Measurement-first ML / NLP researcher: data-centric interpretability, model reliability, and on-device efficiency. I study how the data and interventions applied to a model change its behavior (memorization, factuality), and I hold my own results to a hard standard: I report nulls and correct my own false positives.

Website · LinkedIn · ORCID 0009-0000-6441-7962

## Featured research

**quant-memorization-study** — Does quantization change what a model memorizes and how reliably it recalls facts? Uses efficiency (INT8/INT4) as the independent variable and model behavior as the dependent variable, extending black-box memorization probing (Ravichander et al., 2025, arXiv:2503.12072). Result across 6 models: INT4 leaves factual accuracy unchanged (a replicated null); memorization is driven by model scale, not precision. A pilot false positive was caught and corrected by scaling; measure, do not assert. Released as a Figshare preprint, DOI: 10.6084/m9.figshare.33858859. Cross-hardware replication (NVIDIA CUDA) by Akshay Upadhyay.

**context-configuration-builder (Consistent Context Kit)** — Turns a published negative result on repository context files (ETH, arXiv:2602.11988) into a pre-registered controlled study: does access-pattern-tiered context recover coding-agent task success at lower cost? Real SWE-bench test-execution grading plus from-scratch statistics (McNemar, bootstrap CIs, non-inferiority, CMH, permutation). Shares one principle with the quantization work, spend the expensive resource only where it changes behavior, wired together in code. BSL 1.1.

## Approach

Pre-register hypotheses. Use only measured facts; label everything unverified. Build the instrument correctly (I document the bugs). Prefer an honest null or a characterized tradeoff over an inflated number.

## Background

M.S. Telecommunications, University of Colorado Boulder (2019). A decade in software and systems engineering since 2013: Cisco (VPN dataplane PKI/AAA, TLS/DTLS traffic analysis), plus systems and migration engineering at Unisys and TATA Power. Now independent research in hardware-efficient ML and NLP interpretability.
