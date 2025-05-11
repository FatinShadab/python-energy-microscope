import ctypes

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv
from input import __default__

# Load the shared library
fasta_lib = ctypes.CDLL(os.path.abspath("./libfasta.so"))

# Define argtypes and restype for fasta_alignment
fasta_lib.fasta_alignment.argtypes = [
    ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int,
    ctypes.c_int, ctypes.c_int, ctypes.c_int,
    ctypes.c_char_p, ctypes.c_char_p,
    ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)
]
fasta_lib.fasta_alignment.restype = ctypes.c_int

def fasta_alignment(query, target, k, match=1, mismatch=-1, gap=-2):
    aligned_query = ctypes.create_string_buffer(1000)
    aligned_target = ctypes.create_string_buffer(1000)
    start_q = ctypes.c_int()
    start_t = ctypes.c_int()

    score = fasta_lib.fasta_alignment(
        query.encode("utf-8"),
        target.encode("utf-8"),
        k,
        match,
        mismatch,
        gap,
        aligned_query,
        aligned_target,
        ctypes.byref(start_q),
        ctypes.byref(start_t)
    )

    return {
        "score": score,
        "aligned_query": aligned_query.value.decode("utf-8"),
        "aligned_target": aligned_target.value.decode("utf-8"),
        "start_q": start_q.value,
        "start_t": start_t.value,
    }

def driver(k, query, target):
    result = fasta_alignment(query, target, k)
    print("Score:", result["score"])
    print("Aligned Query:", result["aligned_query"])
    print("Aligned Target:", result["aligned_target"])
    print("Start in Query:", result["start_q"])
    print("Start in Target:", result["start_t"])

# Benchmarking functions for energy
@measure_energy_to_csv(n=__default__["fasta"]["test_n"], csv_filename="fasta_ctypes")
def run_energy_benchmark(k: int, query_sequence: str, target_sequence: str) -> None:
    driver(k, query_sequence, target_sequence)

# Benchmarking function for time
@measure_time_to_csv(n=__default__["fasta"]["test_n"], csv_filename="fasta_ctypes")
def run_time_benchmark(k: int, query_sequence: str, target_sequence: str) -> None:
    driver(k, query_sequence, target_sequence)


if __name__ == "__main__":
    k = __default__["fasta"]["k"]
    query_sequence = __default__["fasta"]["query_sequence"]
    target_sequence = __default__["fasta"]["target_sequence"]

    # Run the driver function
    run_energy_benchmark(k, query_sequence, target_sequence)
    run_time_benchmark(k, query_sequence, target_sequence)
