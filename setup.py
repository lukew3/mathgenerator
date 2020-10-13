from setuptools import setup, find_packages

setup(
    name='mathgenerator',
    version='1.0.1',
    description='An open source solution for generating math problems',
    url='https://github.com/todarith/mathgenerator',
    author='Luke Weiler',
    author_email='lukew25073@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[

    ],
    entry_points={
	   'console_scripts': [
            'mathgenerator=mathgenerator.generator:main'
	   ],
    },
)
