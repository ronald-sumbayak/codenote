<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get  ('/', 'CodeController@index');

Route::get  ('/api/token/',         'CodeController@token');
Route::post ('/api/checkpassword/', 'CodeController@checkPassword');
Route::get  ('/api/setpassword/',   'CodeController@setPassword');
Route::post ('/api/setpassword/',   'CodeController@setPassword');
Route::post ('/api/clearpassword/', 'CodeController@clearPassword');
Route::post ('/api/changeuri/',     'CodeController@changeUri');

Route::post ('/api/submission/', 'SubmissionController@submit');
Route::post ('/api/convert/',    'SubmissionController@convert');

Route::post ('/api/postresult/', 'CodeController@postResult');
Route::post ('/api/postdata/',   'CodeController@postData');
Route::get  ('/api/getdata/',    'CodeController@getData');

Route::get  ('/share/{uri}', 'CodeController@share');
Route::get  ('/{uri}',       'CodeController@open');
Route::post ('/{uri}',       'CodeController@open');
