"""
Setup script for the CWR import module.
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cwr_import",
    version="0.1.0",
    author="Sebastian Spring",
    author_email="sebastian.spring@example.com",
    description="Parser for Common Works Registration (CWR) files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sebastianspring/cwr_import",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[],
    entry_points={
        "console_scripts": [
            "cwr_import=cwr_import.src.main:main",
        ],
    },
) 