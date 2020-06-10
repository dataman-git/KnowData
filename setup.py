import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="KnowData", # Replace with your own username
    version="0.0.1",
    author="Dataman",
    author_email="datasciencecheers@gmail.com",
    description="The python module to help to know your data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dataman-git/KnowData",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)