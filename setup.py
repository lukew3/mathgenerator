from setuptools import setup, find_packages

setup(
    name='mathGenerator',
    version='1.0.0',
    description='An open source solution for generating math problems',
    url='https://github.com/todarith/mathGenerator',
    author='Luke Weiler',
    author_email='lukew25073@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[

    ],
    entry_points={
	   'console_scripts': [
            'mathGenerator=mathGenerator.mainGen:main'
	   ],
    },
)
