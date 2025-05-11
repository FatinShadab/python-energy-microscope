from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

extensions = [
    Extension(
        name="raw",
        sources=["raw.pyx"],
        include_dirs=[numpy.get_include()],
    )
]

setup(
    name="fannkuch_redux_cython",
    ext_modules=cythonize(extensions, compiler_directives={'language_level': "3"}),
    zip_safe=False,
)