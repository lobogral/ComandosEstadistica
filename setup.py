from setuptools import setup, find_packages


def url_release(package: str) -> str:
    """Retorna el URL faltante de un paquete.

    Retorna el URL faltante de un paquete para
    descargar el release de la última versión.
    """
    retorno = '/releases/latest/download/'
    retorno += package + '.tar.gz'
    return retorno


setup(
    name="estadistica",
    version="0.3",
    packages=find_packages(),
    install_requires=[
        'redondeo @ https://github.com/lobogral/redondeo'
            + url_release("redondeo"),
        'matplotlib',
        'sympy'
    ]
)
