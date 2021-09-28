from setuptools import setup, find_namespace_packages

setup(
    name="estadistica",
    version="0.1",
    package_dir={'estadistica': 'src/estadistica'},
    packages=find_namespace_packages('src'),
    install_requires = [
        'redondeo @ https://github.com/lobogral/redondeo/releases/latest/download/redondeo.tar.gz',
        'matplotlib',
        'sympy'
    ]
)
