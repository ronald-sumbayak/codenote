<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Code extends Model
{
    public $incrementing = false;

    protected $primaryKey = 'uri';
    protected $guarded = [];
    protected $hidden = ['user', 'password'];
    protected $attributes = [
        'user'     => 'umum',
        'language' => 'text',
        'caret'    => 0,
        'compiled' => false
    ];
}
