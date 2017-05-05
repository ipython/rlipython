from distutils.core import setup

setup(
    name='rlipython',
    version='0.1dev',
    packages=['rlipython',],
    install_requires=["ipython>5.3"],
    license='BSD',
    author='The IPython Development Team',
    author_email='ipython-dev@python.org',
    url='https://github.com/ipython/rlipython',
    description="readline integration for IPython 5.4+ and 6.0+",
    long_description=open('readme.md').read(),
)
