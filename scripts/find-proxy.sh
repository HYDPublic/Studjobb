#!/bin/bash
CURRENT_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd ) 
CRAWLER_DIR=$CURRENT_DIR"/../src/crawler/"
python $CRAWLER_DIR"/elite-proxy-finder/elite-proxy-finder.py"
