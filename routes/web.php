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


use Illuminate\Support\Facades\Route;

Route::get  ('/', 'CodeController@index')->name ('index');

Route::post ('/login',            'UserController@authenticate')->name ('login');
Route::get  ('/account/register', 'UserController@showRegister')->name ('showregister');
Route::post ('/register',         'UserController@register')->name ('register');
Route::post ('/account/logout',   'UserController@logout')->name ('logout');

Route::get    ('/user/mycodes',  'UserController@mycodes')->name ('mycodes');
Route::post   ('/delete',        'UserController@delete')->name ('delete');
Route::delete ('/bulkdelete',    'UserController@bulkdelete')->name ('bulkdelete');

Route::post ('/api/token/',         'CodeController@token');
Route::post ('/api/checkpassword/', 'CodeController@checkPassword');
Route::post ('/api/setpassword/',   'CodeController@setPassword');
Route::post ('/api/clearpassword/', 'CodeController@clearPassword')->name ('clearpassword');
Route::post ('/api/changeuri/',     'CodeController@changeUri');

Route::post ('/api/submission/', 'SubmissionController@submit');
Route::post ('/api/convert/',    'SubmissionController@convert');

Route::post ('/api/postresult/', 'CodeController@postResult');
Route::post ('/api/postdata/',   'CodeController@postData');
Route::get  ('/api/getdata/',    'CodeController@getData');

Route::get ('/raw/{uri}',      'ViewController@raw');
Route::get ('/code/{uri}',     'ViewController@code');
Route::get ('/download/{uri}', 'ViewController@download');
Route::get ('/{uri}',          'CodeController@open');

//Auth::routes();

//Route::get('/home', 'HomeController@index')->name('home');
