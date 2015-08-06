TESTS="*_test.py"
REQUIREMENTS="src/requirements.txt"

install:
	pip install -r $(REQUIREMENTS) 

test: 
	@python -B -m unittest discover -s tests -p $(TESTS)

.PHONY: test install
