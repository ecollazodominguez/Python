from setuptools import setup

descripcion_longa = open("readme.txt").read()

setup(
    name = "Exemplo de empaquetado",
    version = "0.12",
    author = "Eduardo",
    author_email = "ecollazodominguez@danielcastelao.org",
    url = "https://www.danielcastelao.org",
    license = "GLP",
    platforms = "Unix",
    classifiers = ["Development Status :: 3 - Alpha",
                   "Environment :: Console",
                   "Topic :: Software Development :: Libraries",
                   "License :: OSI Aproved :: GNU General Public License",
                   "Programing Language :: Python",
                   "Operating System :: Linux Ubuntu"],
    description = "Descripción breve do empaquetado",
    long_description = descripcion_longa,
    keywords = "empaquetado instalador paquetes",
    packages =['paquete', 'paquete/subPaquete'], #packages = find_packages(exclude = ('*test', '*.test.*')
    package_data = {
        'paquete': 'notas.txt',
        'paquete/subPaquete': 'texto.txt'
    },
    entry_points = {'console_scripts': ['imprimeAlgo = paquete.moduloPaquete: main',],}
)