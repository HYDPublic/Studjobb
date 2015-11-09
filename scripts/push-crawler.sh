#!/bin/bash
CURRENT_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd ) 
CRAWLER_DIR=$CURRENT_DIR"/../src/crawler/formulas"
rsync $CRAWLER_DIR michael@studjobb.no:/srv/studjobb.no/src/ --verbose
