<?php

use Illuminate\Database\Eloquent\Model  as Eloquent;

class Category extends Eloquent {

    protected $table = 'categories';

    public function jobs () {
		return $this->hasMany('Job')->orderBy('jobs.created_at', 'desc');
	}

}
