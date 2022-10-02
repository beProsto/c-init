from setuptools import setup
from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
	long_description = f.read()

ver = '0.1.1'

setup(
	name='c-init',
	version=ver,
	url='https://github.com/beProsto/c-init',
	license='MIT',
	author='beProsto',
	author_email='be1prosto@gmail.com',
	description='A simple tool for setting up c/c++ projects.',
	long_description=long_description,
	long_description_content_type='text/markdown',
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent'
	],
	packages=['c-init'],
	entry_points={
		'console_scripts': 'updog = updog.__main__:main'
	},
	include_package_data=True,
	install_requires=[],
)