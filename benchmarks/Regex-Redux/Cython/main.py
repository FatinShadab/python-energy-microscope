import re
from typing import List, Tuple
from raw import regex_redux
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv
from input import __default__



if __name__ == "__main__":
    regex_redux("input_fasta.txt")
