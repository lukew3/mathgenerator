sphinx-apidoc mathgenerator -F -o docs
sphinx-build -b html docs/ docs/build/html
cd docs/build/html
python -m http.server 8000
