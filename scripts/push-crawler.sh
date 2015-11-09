#!/bin/bash
CURRENT_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd ) 
CRAWLER_RUN=$CURRENT_DIR"/../src/crawler/runner.py"
CRAWLER_DIR=$CURRENT_DIR"/../src/crawler/formulas"
rsync -r $CRAWLER_DIR michael@studjobb.no:/srv/studjobb.no/src/crawler/ --verbose
rsync    $CRAWLER_RUN michael@studjobb.no:/srv/studjobb.no/src/crawler/ --verbose
