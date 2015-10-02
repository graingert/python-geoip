(
    cd geolite2
    ./download.sh
    python setup.py sdist bdist_wheel
    twine upload dist/* -u graingert-autopypi -p "${PYPI_PASSWORD}"
)
