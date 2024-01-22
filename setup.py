# setup.py
import os

from setuptools import setup, find_packages

data_files = []
for root, dirs, files in os.walk("PYTHON-LEARN"):
    data_files.append(
        (os.path.relpath(root, "PYTHON-LEARN"), [os.path.join(root, f) for f in files])
    )

setup(
    name='python-learn',
    version='0.1',
    packages=find_packages(),
    data_files=data_files,
    install_requires=[
        'boto3==1.34.24',
        'pandas==2.2.0',
        'pytest==7.4.4',
        'flake8==7.0.0',
    ],
)
