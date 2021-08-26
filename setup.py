# coding=utf-8
import glob
import os
import re
from setuptools import setup, find_packages, Extension

try:
    from Cython.Distutils import build_ext
except ImportError:
    os.system("pip install Cython>=0.24")
    from Cython.Distutils import build_ext


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


def get_extensions():
    lang_models = glob.glob('pychardet/src/LangModels/*.cpp')
    uchardet_sources = glob.glob('pychardet/src/*.cpp') + lang_models

    pychardet_sources = ["pychardet/universal_detector.pyx",
                         "pychardet/detector.cpp"]

    return [
        Extension("pychardet.universal_detector",
                  sources=pychardet_sources + uchardet_sources,
                  language="c++")
    ]


setup(
    name='pychardet',
    version=get_version(),
    author='PressIndex',
    packages=find_packages(),
    install_requires=get_requirements(),
    classifiers=(
        'Programming Language :: Cython',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ),
    include_package_data=True,
    ext_modules=get_extensions(),
    cmdclass={'build_ext': build_ext}
)
