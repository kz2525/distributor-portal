from setuptools import setup, find_packages

setup(
    name='distributor-portal',
    version='0.0.1',
    description='Distributor Portal App for ERPNext',
    author='kinza',
    author_email='kkz55kinza@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['frappe'],
    app_license = "MIT",
)
