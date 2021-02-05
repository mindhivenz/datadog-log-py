import pathlib
import setuptools

README_PATH = pathlib.Path(__file__).parent / "README.md"

setuptools.setup(
    name="datadog-log",
    version="1.2.0",
    description="JSON formatted logging for Datadog",
    long_description=README_PATH.read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/mindhivenz/datadog-log-py",
    author="Mindhive",
    author_email="devops@mindhive.co.nz",
    license="MIT",
    packages=["datadoglog"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["python-json-logger"],
)
