from distutils.core import setup


extras_requires = {
    ':sys_platform == "win32"': ['pyreadline>=2'],
    ':sys_platform == "darwin" and platform_python_implementation == "CPython"': ['gnureadline'],
}

setup(
    name='rlipython',
    version='0.1.1',
    packages=['rlipython',],
    install_requires=["ipython>5.3"],
    extras_requires=extras_requires,
    license='BSD',
    author='The IPython Development Team',
    author_email='ipython-dev@python.org',
    url='https://github.com/ipython/rlipython',
    description="readline integration for IPython 5.4+ and 6.0+",
    long_description=open('readme.md').read(),
)
