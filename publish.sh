rm -rf build/
rm -rf dist/
pipenv run python setup.py sdist bdist_wheel
pipenv run twine check dist/*
pipenv run twine upload dist/*
