import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="convigure",
    version="0.2.0",
    author="Randy Cahya Wihandika",
    author_email="rendicahya@gmail.com",
    description="Easy configuration for Python with dot notation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rendicahya/convigure",
    packages=setuptools.find_packages(),
    install_requires=["toml"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
