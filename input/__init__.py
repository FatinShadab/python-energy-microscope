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
}