from setuptools import setup, find_packages

setup(name='mathgenerator',
      version='1.5.1',
      description='A math task generator based off of https://github.com/lukew3/mathgenerator',
      url='https://github.com/synapse-alpha/mathgenerator',
      author='SN1 Development Team',
      author_email='brady@opentensor.dev',
      license='MIT',
      packages=find_packages(),
      install_requires=['sympy', 'scipy'],
      entry_points={})
