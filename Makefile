BIN    = node_modules
RUNNER = $(BIN)/mocha/bin/mocha
TESTS  = $(shell find test -name "*.js")

install: node_modules

node_modules: package.json
	@npm install

test: 
	@node $(RUNNER) $(TESTS) --harmony 

.PHONY: install test
