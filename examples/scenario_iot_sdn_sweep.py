"""
examples/scenario_iot_sdn_sweep.py

Parameter-sweep experiment for the IoT & SDN capacity model.

Generates two charts:
- Blocking vs control load
- Retry load vs control load

Use this script to demonstrate how the model behaves under increasing
control/management traffic in an IoT + SDN environment.
"""

import matplotlib.pyplot as plt

from iot_sdn_capacity_model import IoTSdnCapacityParameters, solve_iot_sdn_capacity


def run_sweep():
    # Base configuration of the SDN-controlled IoT domain
    capacity_units = 500
    A_telemetry = 200.0
    A_bulk = 40.0
    bulk_units = 2
    retry_factor = 0.3
    p_ext = 0.1

    # Sweep control/management load from 10 to 100 Erlangs
    control_loads = list(range(10, 101, 10))

    blocking = []
    retries = []

    for A_control in control_loads:
        params = IoTSdnCapacityParameters(
            capacity_units=capacity_units,
            A_telemetry=A_telemetry,
            A_control=float(A_control),
            A_bulk=A_bulk,
            bulk_units=bulk_units,
            retry_factor=retry_factor,
            external_failure_prob=p_ext,
        )
        res = solve_iot_sdn_capacity(params)
        blocking.append(res.blocking_prob)
        retries.append(res.retry_load)

    # Chart 1: Blocking vs Control Load
    plt.figure()
    plt.plot(control_loads, blocking)
    plt.xlabel("Control Load (Erlangs)")
    plt.ylabel("Blocking Probability (Erlang-B)")
    plt.title("Blocking vs Control Load (IoT & SDN)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("examples/blocking_vs_control_load.png", dpi=200)

    # Chart 2: Retry Load vs Control Load
    plt.figure()
    plt.plot(control_loads, retries)
    plt.xlabel("Control Load (Erlangs)")
    plt.ylabel("Retry Load (Erlangs)")
    plt.title("Retry Load vs Control Load (IoT & SDN)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("examples/retry_vs_control_load.png", dpi=200)

    print("Charts generated:")
    print(" - examples/blocking_vs_control_load.png")
    print(" - examples/retry_vs_control_load.png")


if __name__ == "__main__":
    run_sweep()
