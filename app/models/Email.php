<?php

use Illuminate\Database\Eloquent\Model  as Eloquent;

class Email extends Eloquent {

    protected $table = 'emails';

    public function crawledjob () {
        return $this->hasOne('CrawledJob');
    }

}
