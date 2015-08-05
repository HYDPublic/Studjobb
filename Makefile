TESTS="*_test.py"

test: 
	@python -B -m unittest discover -s tests -p $(TESTS)

.PHONY: test
