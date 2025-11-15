from setuptools import setup, find_packages

setup(
name="Sorting_Package",
version="0.1.0",
# Find packages in the root (e.g., 'src' and 'src.algorithms')
packages=find_packages(where='src'),
package_dir={'': 'src'},    
description="A demonstration package for various sorting algorithms.",
author="Bidisha",
install_requires=[],
extras_require={
"dev": ["pytest"],
}
)