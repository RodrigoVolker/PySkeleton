try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': '__ ___',
    'author': 'Damon McCullough',
    'url': 'https://github.com/damonmcc/___',
    'download_url': 'https://github.com/damonmcc/___.git',
    'author_email': 'damonmcc1391@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME']
    'scripts': [],
    'name': '___'
}

setup(**config)
