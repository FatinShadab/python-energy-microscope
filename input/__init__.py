import random

__default__ = {
    'hanoi': {
        'test_n': 50,
        'n': 18,
    },

    'strassen': {
        'test_n': 50,
        'A': [[random.randint(0, 10) for _ in range(128)] for _ in range(128)],
        'B': [[random.randint(0, 10) for _ in range(128)] for _ in range(128)],
    },

    'spectral-norm': {
        'test_n': 50,
        'iterations': 1000,
        'matrix': [[random.randint(0, 10) for _ in range(128)] for _ in range(128)],
    },

    'sieve': {
        'test_n': 50,
        'n': 10_000_000,
    },

    'n-queens': {
        'test_n': 50,
        'n': 18,
    },

    'reverse_complement': {
        'test_n': 50,
        'dna_sequence': "ATGC" * 10_000_000,
    },

    'binary-trees': {
        'test_n': 50,
        'depth': 18,
    },

    'knn': {
        'test_n': 50,
        'num_samples': 10_000,
        'num_features': 100,
        'k': 5,
    },

    'pi_digits': {
        'test_n': 50,
        'iterations': 1000,
    },

    'K_Nucleotide': {
        'test_n': 50,
        'k': 6,
        'nucleotide_sequence_file': '/home/eaegon/Documents/GITHUB/python-energy-microscope/benchmarks/K-Nucleotide/dna.txt',
    },

    "fannkuch_redux": {
        "test_n": 50,
        "n": 10,
        "perm": list(range(1, 11)),
    },

    "fasta": {
        "test_n": 50,
        "k": 8,
        "query_sequence": "ACGTAGCTAGCTAGTACGATCGATCGTACGATCGATCGTAGCTAGCTGACGATCGATCGTACGATCGTAGCTAGCATCG",
        "target_sequence": "GATCGATCGTAGCTAGCATCGATCGTACGATCGATCGTAGCTAGCTGACGATCGATCGTACGATCGTAGCTAGCATCG"
    },

    "mandelbrot": {
        "test_n": 50,
        "width": 100,
        "height": 100,
        "max_iter": 100,
        "x_min": -2.0,
        "x_max": 1.0,
        "y_min": -1.5,
        "y_max": 1.5
    },

    "nbody": {
        "test_n": 50,
        "num_bodies": 100,
        "time_steps": 1000,
        "G": 6.67430e-11,
        "dt": 1000,
        "bodies": [
            {
                "mass": random.uniform(1e24, 1e30),
                "position": [random.uniform(-1e11, 1e11) for _ in range(3)],
                "velocity": [random.uniform(-1e4, 1e4) for _ in range(3)]
            } for _ in range(100)
        ]
    },

    "regex_redux": {
        "file_path": "input_fasta.txt",
        "test_n": 50
    }
}
