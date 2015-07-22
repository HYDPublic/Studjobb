BIN    = node_modules/.bin
RUNNER = $(BIN)/_mocha
TESTS  = $(shell find test -name "*.js")

install: node_modules

node_modules: package.json
	@npm install

test: 
	@$(RUNNER) $(TESTS) 

.PHONY: install test
