import setuptools
from flask_lt import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flask-localtunnel",
    version=__version__,
    author="Jak Bin",
    description="A simple way to demo Flask apps from your machine.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/redevil1/flask-localtunnel",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    keywords='flask,flask-ngrok,ngrok,localtunnel,demo',
    py_modules=['flask_lt'],
    install_requires=['Flask>=0.14.0'],
)
