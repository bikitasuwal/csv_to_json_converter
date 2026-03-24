from setuptools import setup, find_packages

setup(
    name="csv_to_json_converter_bikitasuwal",
    version="0.1.0",
    author="Bikita Suwal",
    author_email="bikitasuwal12@example.com",
    description="Python package to automatically organize files by type",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/bikitasuwal/csv-to-json-converter",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.13.5',
)