import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyONS", # Replace with your own username
    version_format="{tag}.{commitcount}",
    setup_requires=['setuptools-git-version'],
    author="Jack Minchin",
    author_email="jackminchin@gmail.com",
    description="Interact with the ONS API in Python ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jackminchin/PythonONSAPIWrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
