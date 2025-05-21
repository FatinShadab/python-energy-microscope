import random

__default__ = {
    'hanoi': {
        'test_n': 100,
        'n': 18,
    },
    
    'strassen': {
        'test_n': 100,
        'A': [[random.randint(0, 10) for _ in range(128)] for _ in range(128)],
        'B': [[random.randint(0, 10) for _ in range(128)] for _ in range(128)],
    },
    
    'spectral-norm': {
        'test_n': 100,
        'iterations': 1000,
        'matrix': [[random.randint(0, 10) for _ in range(128)] for _ in range(128)],
    },
    
    'sieve': {
        'test_n': 100,
        'n': 10000000,
    },
    
    'n-queens': {
        'test_n': 100,
        'n': 18,
    },
    
    'reverse_complement': {
        'test_n': 100,
        'dna_sequence': "ATGC" * 10000000,  # Example DNA sequence
    },
    
    'binary-trees': {
        'test_n': 100,
        'depth': 18,
    },
    
    'knn': {
        'test_n': 100,
        'num_samples': 10000,  # Number of samples
        'num_features': 100,   # Number of features
        'k': 5,               # Number of neighbors
    },
    
    'pi_digits': {
        'test_n': 100,
        'iterations': 1000,  # Adjust for precision
    },
    
    'K_Nucleotide': {
        'test_n': 100,
        'k': 6,  # Length of the
        'nucleotide_sequence_file': '/home/eaegon/Documents/GITHUB/python-energy-microscope/benchmarks/K-Nucleotide/dna.txt',  # Path to the input file 
    },
    
    "fannkuch_redux": {
        "test_n": 100,
        "n": 10,  # You can change this value to test with different values of n
        "perm": list(range(1, 11)),  # Initialize the first permutation must be in range [1, n]
    },
    
    "fasta": {
        "test_n": 100,
        "k": 8,
        "query_sequence": "ACGTAGCTAGCTAGTACGATCGATCGTACGATCGATCGTAGCTAGCTGACGATCGATCGTACGATCGTAGCTAGCATCG",
        "target_sequence": "GATCGATCGTAGCTAGCATCGATCGTACGATCGATCGTAGCTAGCTGACGATCGATCGTACGATCGTAGCTAGCATCG"
    },
    
    "mandelbrot": {
        "test_n": 100,
        "width": 100,
        "height": 100,
        "max_iter": 100,
        "x_min": -2.0,
        "x_max": 1.0,
        "y_min": -1.5,
        "y_max": 1.5
    },

    "nbody": {
        "test_n": 100,
        "num_bodies": 100,
        "time_steps": 1000,
        "G": 6.67430e-11,  # Gravitational constant
        "dt": 1000,  # Time step
        "bodies": [
            {
                "mass": random.uniform(1e24, 1e30),
                "position": [random.uniform(-1e11, 1e11) for _ in range(3)],
                "velocity": [random.uniform(-1e4, 1e4) for _ in range(3)]
            } for _ in range(100)
        ]
    }
}