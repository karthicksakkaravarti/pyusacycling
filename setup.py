from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pyusacycling",
    version="0.1.4",
    author="PyUSACycling Team",
    author_email="author@example.com",
    description="A package for parsing USA Cycling event results",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/karthicksakkaravarti/pyusacycling",
    project_urls={
        "Bug Tracker": "https://github.com/karthicksakkaravarti/pyusacycling/issues",
        "Documentation": "https://github.com/karthicksakkaravarti/pyusacycling#readme",
        "Source Code": "https://github.com/karthicksakkaravarti/pyusacycling",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
    ],
    python_requires=">=3.9",
    install_requires=[
        "requests>=2.25.0",
        "beautifulsoup4>=4.9.0",
        "pydantic>=1.9.0",
        "lxml>=4.6.0",  # For better HTML parsing performance
        "python-dateutil>=2.8.2",  # For date parsing
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "pytest-cov>=2.12.0",
            "black>=22.0.0",
            "isort>=5.10.0",
            "flake8>=4.0.0",
            "mypy>=0.910",
            "types-requests>=2.25.0",
            "types-beautifulsoup4>=4.9.0",
            "types-python-dateutil>=2.8.2",
            "build>=0.8.0",
            "twine>=4.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "pyusacycling=pyusacycling.cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
