from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(
    name="Alberto_library",
    version="0.0.1",
    author="Alberto Pad",
    author_email="author@example.com",
    description="Functions pln",

    url="https://github.com/AlbertoPad/Albert_Library",
    py_modules=['pln'],
)