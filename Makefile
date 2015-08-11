TESTS="*_test.py"
REQUIREMENTS="requirements.txt"

install:
	pip install -r $(REQUIREMENTS) 

test: 
	@python -B -m unittest discover -s tests -p $(TESTS)

serve:
	@python src/webserver/main.py

run:
	@python src/webserver/webserver.py

.PHONY: test install serve
