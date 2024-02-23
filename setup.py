from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('readme.MD').read(),
    install_requires=['numpy'],
    url='https://github.com/<username>/<package-name>',
    author='<your-name>',
    email='<your-email>'
)