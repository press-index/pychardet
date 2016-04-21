# coding=utf-8
import glob
import os
import re

from Cython.Distutils import build_ext
from setuptools import setup, find_packages, Extension


def get_version():
    init = os.path.join(os.path.dirname(__file__), 'pychardet/__init__.py')
    with open(init, 'r') as f:
        matches = re.findall(r'__version__\s*=\s*[\"\']([\d\w\.]+)[\"\']',
                             f.read())
        if matches:
            return matches[0]

        raise ValueError("Could not find version string")


def get_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()


lang_models = glob.glob('pychardet/src/LangModels/*.cpp')
uchardet_sources = glob.glob('pychardet/src/*.cpp') + lang_models

pychardet_sources = ["pychardet/universal_detector.pyx",
                     "pychardet/detector.cpp"]

extensions = [
    Extension("pychardet.universal_detector",
              sources=pychardet_sources + uchardet_sources,
              language="c++")
]

setup(
    name='pychardet',
    version=get_version(),
    author='Pressindex',
    packages=find_packages(),
    install_requires=get_requirements(),
    classifiers=(
        'Programming Language :: Cython',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ),
    include_package_data=True,
    ext_modules=extensions,
    cmdclass={'build_ext': build_ext}
)
