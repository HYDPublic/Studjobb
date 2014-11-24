<?php

use Illuminate\Database\Eloquent\Model as Eloquent;

class CrawledJob extends Eloquent {

    protected $table = 'crawled';

    public function createdAt () {
        return date('m-d-y h:m', strtotime($this->created_at));
    }

    public function source () {
        $parsed = parse_url($this->url);
        return $parsed['host'];
    }

    public function emails () {
        return $this->hasMany('email');
    }

    public function getEmail () {

        /* See if stored */
        if (isset($this->email))
            return $this->email;

        /* Try to guess */
        $pattern="/[A-Za-z0-9_-]+@[A-Za-z0-9_-]+\.([A-Za-z0-9_-][A-Za-z0-9_]+)/";
        preg_match_all($pattern, $this->content, $matches);

        if ($matches) {
            return implode (', ', $matches[0]);
        }
    }

}
