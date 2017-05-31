# Release Checklist

A list of things that need to work for each and every release.

## Initial conditions

- [ ] Get an account on [testpypi](https://wiki.python.org/moin/TestPyPI)
- [ ] include credentials for both `pipy` and `testpypi` in your `~/.pypirc`

    [distutils]
    index-servers =
        pypi
        testpypi

    [pypi]
    username:yours
    password:yours

    [testpypi]
    repository=https://testpypi.python.org/pypi
    username:yours
    password:yours

- [ ] `pip install pypandoc` - required for README.md conversion, since
  PyPI only supports ReStructured Text as rich text descriptions on the site.

## Release: 
- [ ] bump the version in setup.py
        `.devN` (`.dev4` -> `.dev5`) for dev release
- [ ] `python setupegg.py sdist bdist_wheel`
- [ ] inspect the artifacts before upload

    $ ls dist
    rlipython-0.1.2.dev0-py2.py3-none-any.whl rlipython-0.1.2.dev0.tar.gz

- [ ] `python setupegg.py sdist bdist_wheel upload -r testpypi`
- [ ] Check pypi test site for results, possibly :

    pip install --pre --upgrade --extra-index https://testpypi.python.org/pypi rlipython

- [ ] `python setupegg.py sdist bdist_wheel upload -r pypi`


## Stable release:

Same as Dev release, just bump the 
