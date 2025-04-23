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
    }
}