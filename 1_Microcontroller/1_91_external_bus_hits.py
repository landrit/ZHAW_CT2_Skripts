"""
INPUT
"""
internal_memory_width = 8  # bits
external_bus_width = 16  # bits
operation_type = "read"  # "read" or "write"
value_width = 32  # 8, 16, or 32 bits
"""
END OF INPUT
"""


def memory_operation(internal_memory_width, external_bus_width, operation_type, value_width):
    num_bus_hits = (value_width + external_bus_width - 1) // external_bus_width

    if operation_type == "read":
        cpu_waits = True
    elif operation_type == "write":
        cpu_waits = False
    else:
        raise ValueError("Invalid operation type. Must be 'read' or 'write'.")

    return num_bus_hits, cpu_waits


num_bus_hits, cpu_waits = memory_operation(internal_memory_width, external_bus_width, operation_type, value_width)

print(f"Number of bus hits / Anzahl Buszugriffe: {num_bus_hits}")
print(f"CPU waits?: {cpu_waits}")
