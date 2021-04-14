from setuptools import setup,find_packages


setup(
    name="RBAPG",
    version="0.0.1",
    packages=find_packages(),
    url="https://github.com/AzizKpln/RBAPG",
    license="GPL-3.0",
    author="Aziz Kaplan",
    author_email="AzizKpln@protonmail.com",
    description="READ THE README.MD FILE PLEASE",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
)
