<?php

use Illuminate\Database\Eloquent\Model as Eloquent;

class CrawledJob extends Eloquent {

    protected $table = 'crawled';

    public function createdAt () {
        return date('m-d', strtotime($this->created_at));
    }

    public function source () {
        $parsed = parse_url($this->url);
        return $parsed['host'];
    }

}
