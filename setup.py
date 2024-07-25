from setuptools import find_packages, setup

setup(
    name="sort",
    version="0.1",
    url='https://github.com/ICGog/sort',
    install_requires=[
        "scipy",
        "filterpy==1.4.1",
        "scikit-learn==0.19.2",
        "numba==0.58.1"
    ],
    packages=find_packages(exclude=["scripts*", "notebooks*"])
)
