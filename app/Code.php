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
        'user'     => 0,
        'langName' => 'text'
    ];

    public function enc () {
        return md5 ($this->uri) . $this->password;
    }
}
