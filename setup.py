from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in beta_print_patch/__init__.py
from beta_print_patch import __version__ as version

setup(
	name="beta_print_patch",
	version=version,
	description="Patch frappe print application (version-14).",
	author="IEA-IT",
	author_email="it@iea.com.ar",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
