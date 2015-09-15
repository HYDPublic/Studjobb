#!/bin/bash
CURRENT_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd ) 
CRAWLER_DIR=$CURRENT_DIR"/../src/crawler/"
(cd $CRAWLER_DIR && scrapy list | xargs -n 1 scrapy crawl)
