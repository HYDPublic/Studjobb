TESTS="*_test.py"
REQUIREMENTS="requirements.txt"

install:
	pip install -r $(REQUIREMENTS) 

test: unit-test clean

unit-test: export TEST=true
unit-test:
	@python -B -m unittest discover -s tests -p $(TESTS)

serve:
	@python src/webserver/main.py

run:
	@python src/webserver/webserver.py

clean:
	@find . -name '*.pyc' -delete

.PHONY: test install serve
