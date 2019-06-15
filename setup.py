import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="clusterbagging",
    version="0.5",
    author="Ismaël Lachheb",
    author_email="ismael.lachheb@protonmail.com",
    description="A Package to do cluster bagging",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/lachhebo/pyclustertend", 
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)