<?php

require_once("../../globals.php");
require_once($GLOBALS["srcdir"] . "/api.inc");

function testForm_report($pid, $encounter, $cols, $id)
{
    $table_name = "form_testForm";
  $form_folder = "testForm";
  include("reportinclude.php");
}
