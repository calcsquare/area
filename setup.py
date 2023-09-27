from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="calcsquare",
    version="0.0.1",
    author="RA",
    author_email="romandreev.it@gmail.com",
    description="A package to calculate area of a figure",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/calcsquare/area",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.9.6",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
