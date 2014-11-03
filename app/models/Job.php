<?php

use Illuminate\Database\Eloquent\Model as Eloquent;

class Job extends Eloquent {

    protected $table = 'jobs';

    public function company () {
        return $this->belongsTo('Company');
    }

    public function due () {
        return date('Y-m-d', strtotime($this->due));
    }

}
