import codecs
import os
import re

from setuptools import Command, find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

version = "0.0.0"
changes = os.path.join(here, "CHANGES.rst")
match = r"^#*\s*(?P<version>[0-9]+\.[0-9]+(\.[0-9]+)?)$"
with codecs.open(changes, encoding="utf-8") as changes:
    for line in changes:
        res = re.match(match, line)
        if res:
            version = res.group("version")
            break

# Get the long description
with codecs.open(os.path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

# Get version
with codecs.open(os.path.join(here, "CHANGES.rst"), encoding="utf-8") as f:
    changelog = f.read()


install_requirements = ["simple-rest-client>=1.0.0"]
tests_requirements = ["pytest", "pytest-cov", "coveralls"]


class VersionCommand(Command):
    description = "print library version"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print(version)


setup(
    name="vindi",
    version=version,
    description="Integração com API da Vindi (Python 3.6+)",
    long_description=long_description,
    url="https://github.com/allisson/python-vindi",
    author="Allisson Azevedo",
    author_email="allisson@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries",
    ],
    keywords="rest client http vindi",
    packages=find_packages(exclude=["docs", "tests*"]),
    setup_requires=["pytest-runner"],
    install_requires=install_requirements,
    tests_require=tests_requirements,
    cmdclass={"version": VersionCommand},
)
