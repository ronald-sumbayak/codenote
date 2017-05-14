<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Code;
use \DateTime;

class CodeController extends Controller
{
    private function generateUri () {
        $chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
        $uri   = "";

        for ($i = 0; $i < 6; $i++)
            $uri .= $chars[mt_rand (1, strlen ($chars)) - 1];

        return $uri;
    }

    private function simpleJson ($message) {
        return response ()->json (['status' => $message]);
    }

    public function index () {
        $uri = $this->generateUri ();
        while (Code::find ($uri)) $uri = $this->generateUri ();
        return redirect ($uri);
    }

    public function open (Request $request, $uri) {
        $code = Code::firstOrNew (['uri' => $uri]);

        if ($code->password && $request->session ()->get (md5 ($code->uri)) != $code->enc ())
            return view ('protected', ['code' => $code]);
        return view ('editor', ['code' => $code]);
    }

    public function checkPassword (Request $request) {
        if (!$request->uri)
            return $this->simpleJson ('you must provide uri');

        $code = Code::find ($request->uri);

        if (!$code)
            return $this->simpleJson ('code does not exists');

        if (!$code->password)
            return $this->simpleJson ('this code is not password-protected');

        if (!$request->password)
            return $this->simpleJson ('you must provide password');

        if (md5 ($request->password) != $code->password)
            return $this->simpleJson ('password didn\'t match');

        $request->session ()->put (md5 ($code->uri), $code->enc ());
        return $this->simpleJson ('success');
    }

    public function setPassword (Request $request) {
        if (!$request->uri)
            return $this->simpleJson ('you must provide uri');

        $code = Code::firstOrNew (['uri' =>$request->uri]);

        if ($code->password) {
            if (!$request->oldpassword)
                return $this->simpleJson ('you must provide old-password');

            if (md5 ($request->oldpassword) != $code->password)
                return $this->simpleJson ('old password didn\'t match');
        }

        if (!$request->newpassword)
            return $this->simpleJson ('you must provide new-password');

        $code->password = md5 ($request->newpassword);
        $code->save ();
        $request->session ()->put (md5 ($code->uri), $code->enc ());
        return $this->simpleJson ('success');
    }

    public function clearPassword (Request $request) {
        if (!$request->uri)
            return $this->simpleJson ('you must provide uri');

        $code = Code::firstOrNew (['uri' => $request->uri]);

        $code->password = null;
        $code->save ();
        return $this->simpleJson ('success');
    }


    public function changeUri (Request $request) {
        if (!$request->uri)
            return $this->simpleJson ('you must provide uri');

        $code = Code::firstOrNew (['uri' => $request->uri]);

        if (!$request->newuri)
            return $this->simpleJson ('you must provide new-uri');

        if (!ctype_alnum ($request->newuri))
            return $this->simpleJson ('URL not valid');

        if (Code::find ($request->newuri))
            return $this->simpleJson ('URL already tekan');

        $request->session ()->forget (md5 ($code->uri));
        $code->uri = $request->newuri;
        $code->save ();
        $request->session ()->put (md5 ($code->uri), $code->enc ());
        return $this->simpleJson ('success');
    }

    public function getData (Request $request) {
        if (!$request->uri)
            return $this->simpleJson ('you must provide uri');

        $code = Code::find ($request->uri);

        if (!$code)
            return $this->simpleJson ('code does not exist');

        if (!$request->lastupdate)
            return $this->simpleJson ('you must provide lastupdate');

        if (new DateTime ($code->updated_at) <= new DateTime ($request->lastupdate))
            return $this->simpleJson ('no update');

        return response ()->json (['status' => 'update', 'code' => $code]);
    }

    public function putData (Request $request) {
        if (!$request->uri)
            return $this->simpleJson ('you must provide uri');

        $code = Code::firstOrNew (['uri' => $request->uri]);

        if (!$code)
            return $this->simpleJson ('code does not exists');

        $code->caret = $request->caret;
        $code->langId = $request->langId;
        $code->langName = $request->langName;
        $code->langVersion = $request->langVersion;
        $code->time = $request->time;
        $code->result = $request->result;
        $code->memory = $request->memory;
        $code->source = $request->source;
        $code->input = $request->input;
        $code->output = $request->output;
        $code->save ();
        return $this->simpleJson ('success');
    }

    public function token () {
        return '5b5ba4a2227f47f54e2959e227ed5bb5';
    }
}
