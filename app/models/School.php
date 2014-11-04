<?php

use Illuminate\Database\Eloquent\Model  as Eloquent;

class School extends Eloquent {

    protected $table = 'schools';

    public function slug () {
		//return $this->hasMany('Job');
	}

}
