from setuptools import setup, find_packages

pyver_requires = []

with open('requirements.txt') as file:
    for line in file.readlines():
        pyver_requires.append(line.strip())

with open('README.rst') as file:
    long_description = file.read()

setup(
    name='nodemeister',
    version='0.0.1',
    author='Jason Antman',
    author_email='jason@jasonantman.com',
    packages=find_packages(),
    url='http://github.com/jantman/nodemeister/',
    description='Django ENC for Puppet',
    long_description=long_description,
    install_requires=pyver_requires,
    keywords="puppet ENC django",
    include_package_data=True
)
