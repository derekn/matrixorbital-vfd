from setuptools import find_packages, setup

meta = {}
with open('matrixorbital_vfd/__version__.py') as fp:
	exec(fp.read(), meta)

setup(
	name='matrixorbital-vfd',
	version=meta['__version__'],
	description='I2C display driver for Matrix Orbital VFDs',
	author='Derek Nicol',
	author_email='derekn85@gmail.com',
	url='https://github.com/derekn/matrixorbital-vfd',
	license='MIT',
	packages=find_packages(),
	python_requires='>=3.4.0',
	install_requires=[
		'smbus2',
	],
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9',
		'Topic :: Software Development :: Libraries',
		'Topic :: System :: Hardware',
		'Topic :: Utilities',
	],
	keywords='matrix orbital vfd vacuum fluorescent display i2c smbus',
)
