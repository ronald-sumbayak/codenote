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
        'langName' => 'text',
        'caret'    => 0
    ];

    public function enc () {
        return md5 ($this->uri) . $this->password;
    }
}
