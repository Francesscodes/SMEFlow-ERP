from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

from smeflow_erp import __version__ as version

setup(
    name="smeflow_erp",
    version=version,
    description="HR and Operations ERP for SMEs",
    author="Francess Ekezie",
    author_email="zynefrancess6444@gmail.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)
