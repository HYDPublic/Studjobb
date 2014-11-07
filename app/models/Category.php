<?php

use Illuminate\Database\Eloquent\Model  as Eloquent;

class Category extends Eloquent {

    protected $table = 'categories';

    public function jobs () {
		return $this
            ->hasMany('Job')
            ->where('published', true)
            ->where('due', '>', date('Y-m-d G:i:s'))
            ->whereRaw('created_at >= now() - interval 30 day')
            ->orderBy('jobs.created_at', 'desc');
	}

}
