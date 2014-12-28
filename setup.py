import os
from setuptools import setup, find_packages


def read(filename):
    """Read a file and return its contents.
    """
    with open(os.path.join(os.path.dirname(__file__), filename)) as infile:
        content = infile.read()

    return content


setup(
    name="Coh-Metrix-Dementia",
    version="0.0.1",
    author="Andre Cunha",
    author_email="andre.lv.cunha@gmail.com",
    description=("Coh-Metrix-Dementia is a tool for analyzing and classifying "
                 "texts from dementia patients."),
    license="GPLv3",
    keywords="text classification dementia",
    # url="http://packages.python.org/????",
    packages=find_packages(),
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Natural Language :: Portuguese (Brazilian)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
    ],
    install_requires = ['sqlalchemy >= 0.9.8',
                        'nltk >= 3.0.0',
                        'psycopg2 >= 2.5.4',
                        'prettytable >= 0.7.2']
)
