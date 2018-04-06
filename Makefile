clean:
	rm -rf build dist
	find . -name '*.pyc' -exec rm \{\} \;

test:
	openfisca-run-test openfisca_pau/tests --country-package openfisca_france --extensions openfisca_pau
