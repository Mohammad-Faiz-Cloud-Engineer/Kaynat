"""
Setup script for Kaynat Programming Language.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="kaynat",
    version="1.0.0",
    author="Mohammad Faiz",
    author_email="",
    description="A programming language that reads like English",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mohammad-Faiz-Cloud-Engineer/Kaynat",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: Software Development :: Interpreters",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "kaynat=kaynat.main:main",
            "kaynat-repl=kaynat.repl:start_repl",
        ],
    },
    keywords="programming-language english-syntax educational interpreter",
    project_urls={
        "Documentation": "https://github.com/Mohammad-Faiz-Cloud-Engineer/Kaynat/tree/main/docs",
        "Source": "https://github.com/Mohammad-Faiz-Cloud-Engineer/Kaynat",
    },
)
