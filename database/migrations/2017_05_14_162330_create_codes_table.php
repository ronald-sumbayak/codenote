<?php

use Illuminate\Support\Facades\Schema;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class CreateCodesTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('codes', function (Blueprint $table) {
            $table->string ('uri');
            $table->string ('user', 32)->default ('umum');
            $table->string ('password', 128)->nullable ();
            $table->integer ('caret')->default (0);

            $table->integer ('langId')->default (0);
            $table->string ('langName', 64)->default ('text');
            $table->string ('langVersion', 64)->nullable ();

            $table->string ('result', 32)->nullable ();
            $table->float ('time', 3, 2)->nullable ();
            $table->bigInteger ('memory')->nullable ();

            $table->longText ('code')->nullable ();
            $table->longText ('input')->nullable ();
            $table->longText ('output')->nullable ();

            $table->timestamps();

            $table->primary ('uri');
            $table->unique ('uri');
            $table->index ('uri');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('codes');
    }
}
