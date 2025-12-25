from setuptools import setup, find_packages

setup(
    name="shared",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=[
        "sqlalchemy>=2.0"
    ],
)
