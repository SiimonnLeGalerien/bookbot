from setuptools import setup, find_packages

setup(
    name="bookbot",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "bookbot=bookbot.main:main",
        ],
    },
    author="SiimonnLeGalerien",
    description="CLI tool to analyze text files",
    python_requires=">=3.8",
)
