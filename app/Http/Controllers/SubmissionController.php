<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Submission;

class SubmissionController extends Controller
{
    public function submit (Request $request) {
        $submission = new Submission;
        $submission->id = $request->id;
        $submission->save ();
        return response ()->json (['status' => 'success']);
    }

    public function convert (Request $request) {
        return str_replace ('\n', "<br>", $request->text);
    }
}
