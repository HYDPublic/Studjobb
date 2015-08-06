TESTS="*_test.py"

install:
	pip install -r ./requirements.txt

test: 
	@python -B -m unittest discover -s tests -p $(TESTS)

.PHONY: test install
