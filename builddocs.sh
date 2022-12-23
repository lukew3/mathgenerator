sphinx-apidoc mathgenerator -F -o docs
cd docs
sphinx build -b html
cd _build/html
python -m http.server 8000