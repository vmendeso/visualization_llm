#!/usr/bin/env python
from setuptools import setup, find_packages

# Read the README file for long description
try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "3Blue1Brown video creation repository"

setup(
    name="visualization-llm",
    version="1.0.0",
    author="3Blue1Brown",
    description="3Blue1Brown video creation repository with manim animations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/3b1b/videos",
    packages=find_packages(include=["custom", "custom.*"]),
    python_requires=">=3.7",
    install_requires=[
        # ManimGL - Core animation library
        "manimgl>=1.6.1",

        # Core dependencies (installed with manimgl)
        "numpy>=1.9",
        "scipy",
        "sympy",
        "pillow",
        "moderngl",
        "moderngl-window",
        "skia-python",
        "noise",
        "pydub",
        "pygments",
        "pyyaml",

        # Additional utilities
        "ipython>=8.18.0",
        "colour",
        "addict",
        "appdirs",
        "diskcache",
        "isosurfaces",
        "fontTools",
        "manimpango>=0.6.0",
    ],
    extras_require={
        "dev": [
            "pytest",
            "pylint",
            "black",
        ],
    },
    entry_points={
        "console_scripts": [
            # You can add custom scripts here if needed
            # "script_name=module:function",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Video",
        "Topic :: Multimedia :: Graphics",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    include_package_data=True,
    package_data={
        "custom": ["**/*.png", "**/*.svg", "**/*.jpg"],
    },
)
