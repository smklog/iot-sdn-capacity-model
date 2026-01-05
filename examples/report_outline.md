# IoT & SDN Capacity Model — Engineering Analysis Summary

## Objective

Evaluate blocking probability, retry behavior, and carried traffic for an
SDN-controlled IoT capacity pool under mixed traffic conditions
(telemetry, control, and heavy IoT data flows).

## Methodology

- Full-availability loss system with a finite number of capacity units
- Erlang-B recursive blocking formula
- Multi-resource flows (heavy IoT data) modeled via an equivalent-load
  representation (bulk_units · A_bulk)
- Retry traffic for control sessions modeled with a fixed-point iteration
  on the retry load

## Sample Findings (example scenario)

- Blocking probability grows non-linearly as control load increases.
- Retry load amplifies congestion and can significantly contribute to the
  total offered load under high blocking conditions.
- Carried traffic saturates near the capacity limit, while blocking and
  retry effects dominate the performance characteristics.

## Engineering Value

The model provides scalable and computationally efficient estimates for:

- Capacity planning of SDN-controlled IoT domains
- Tuning admission-control policies
- Evaluating resilience against retry-driven overload
- Research and academic experimentation in IoT & SDN teletraffic modeling
