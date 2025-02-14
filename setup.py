###############################################################################
# pKa-ANI								      #
###############################################################################

from setuptools import find_packages
from distutils.core import setup

setup(name='pkaani',
      version="0.1.2",
      description="A Python package to calculate pKa values for proteins",
      long_description=open('README.md').read(),
      long_description_content_type="text/markdown",
      author="Hatice GOKCAN, Olexandr ISAYEV",
      author_email="olexandr@olexandrisayev.com",
      url="https://github.com/isayevlab/pKa-ANI",
      download_url="https://github.com/isayevlab/pKa-ANI",
      python_requires='>=3.6',
      install_requires=["numpy", "scipy", "torch", "torchani==2.2.0", "scikit-learn==1.0.2", "ase", "joblib", "setuptools==58.2.0"],
      packages=find_packages(),
      include_package_data=True,
      entry_points={'console_scripts': ['pkaani = pkaani.run:main', ]},
      )


