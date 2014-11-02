<?php

use Illuminate\Database\Eloquent\Model  as Eloquent;

class Company extends Eloquent {

    protected $table = 'companies';

    public function jobs () {
		return $this->hasMany('Job');
	}

}
