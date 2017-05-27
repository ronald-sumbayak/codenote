<?php

namespace App\Http\Controllers;

use App\Code;
use App\User;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Hash;

class UserController extends Controller {

    private function simpleJson ($message) {
        return response ()->json (['status' => $message]);
    }

    public function authenticate (Request $request) {
        if (!$request->email)
            return $this->simpleJson ("you must provide an email");

        if (!$request->password)
            return $this->simpleJson ("you must provide a password");

        if (!User::where ('email', $request->email))
            return $this->simpleJson ($request->email . " does not exist in our database");

        if (Auth::attempt (['email' => $request->email, 'password' => $request->password], true))
            return $this->simpleJson ('success');
        else
            return $this->simpleJson ("Password didn't match");
    }

    public function showRegister (Request $request) {
        return view ('register');
    }

    public function register (Request $request) {
        if (!$request->name)
            return $this->simpleJson ("you must provide a name");

        if (!$request->email)
            return $this->simpleJson ("you must provide an email");

        if (User::where ('email', $request->email)->count () > 0)
            return $this->simpleJson ("this email has already been used");

        if (!$request->password || !$request->password_confirmation)
            return $this->simpleJson ("you must provide a password");

        if ($request->password != $request->password_confirmation)
            return $this->simpleJson ("password didn't match");

        $user = new User;
        $user->name = $request->name;
        $user->email = $request->email;
        $user->password = Hash::make ($request->password);
        $user->save ();

        Auth::login ($user, true);
        
        if ($request->uri) return redirect ($request->uri);
        return $this->simpleJson ("success");
    }

    public function logout (Request $request) {
        Auth::logout ();
        if ($request->uri) return back ();
        return redirect (route ('index'));
    }

    public function mycodes (Request $request) {
        $codes = Code::where ('user', Auth::id ())->paginate (10);
        return view ('mycodes', ['codes' => $codes]);
    }

    public function delete (Request $request) {
        $code = Code::find ($request->uri);
        if ($code) $code->delete ();
        return redirect ()->route ('mycodes');
    }
}
