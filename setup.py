from setuptools import setup, find_packages

setup(
    name="estadistica",
    version="0.2",
    packages=find_packages(),
    install_requires = [
        'redondeo @ https://github.com/lobogral/redondeo/releases/latest/download/redondeo.tar.gz',
        'matplotlib',
        'sympy'
    ]
)
