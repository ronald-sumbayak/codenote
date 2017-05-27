<?php

namespace App\Http\Controllers;

use App\Code;
use Illuminate\Http\Request;

class ViewController extends Controller {

    public function raw (Request $request, $uri) {
        $code = Code::find ($uri);
        if ($code) return $code->source;
        return view ('404');
    }

    public function code (Request $request, $uri) {
        $code = Code::find ($uri);
        if ($code) return view ('code', ['code' => $code]);
        return view ('404');
    }

    public function download (Request $request, $uri) {
        $code = Code::find ($uri);
        if ($code) return response ()->attachment ($code->source, $uri, 'txt');
        return view ('404');
    }
}
