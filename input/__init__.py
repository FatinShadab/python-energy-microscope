import random

__default__ = {
    'hanoi': {
        'test_n': 15,
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
    
}