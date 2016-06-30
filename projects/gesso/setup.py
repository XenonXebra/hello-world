try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'A sample project',
	'author': 'Gaurav',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'gggidwani@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['gesso'],
	'scripts': [],
	'name': 'gesso'
}

setup(**config)