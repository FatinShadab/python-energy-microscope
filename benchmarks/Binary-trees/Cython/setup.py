from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("raw.pyx")
)

# use the command below to build the Cython code:
# python setup.py build_ext --inplace
