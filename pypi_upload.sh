# ~/.pypirc
#[distutils]
#index-servers =
#   pypi
#[pypi]
#   username=username
#   password=password


# Build the project tar file and save it under ./dist/
python3 setup.py build sdist

# Upload the built tar file to the pypi (using ~/.pypirc credentials)
twine upload -r pypi dist/PACKAGE-VERSION.tar.gz
