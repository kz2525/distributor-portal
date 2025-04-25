from setuptools import setup, find_packages

setup(
    name='distributor-portal',
    version='0.0.1',
    description='Distributor Portal App for ERPNext',
    author='Your Name',
    author_email='you@example.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['frappe'],
)
