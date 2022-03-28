<?php

require_once("../../globals.php");
require_once("$srcdir/api.inc");

use OpenEMR\Common\Csrf\CsrfUtils;
use OpenEMR\Core\Header;
// -------GENERATE--------
$form_name = 'My Test Form';
$form_folder = 'testForm';
// -----------------------

formHeader("Form: " . $form_name);
$returnurl = 'encounter_top.php';

//------------GENERATE----------------
$table_name = 'form_testForm';

/* load the saved record */
$record = formFetch($table_name, $_GET['id']);

/* remove the time-of-day from the date fields 
Will need written through and looped in text writing program
*/
//------------GENERATE----------------------
?>

<html>

<head>
        <!-- assets -->
    <?php Header::setupHeader('datetime-picker'); ?>
    <link rel="stylesheet" href="../../forms/<?php echo $form_folder; ?>/style.css?v=<?php echo $v_js_includes; ?>">
    <?php echo "<style>"; include_once("style.css"); echo "</style>";?>

</head>

<body class="body_top">

    <?php echo date("F d, Y", time()); ?>
<!-- ----------GENERATE---------------- -->
    <form method=post
        action="<?php echo $rootdir; ?>/forms/<?php echo $form_folder; ?>/save.php?mode=update&id=<?php echo attr_url($_GET["id"]); ?>"
        name="my_form">
		<?php
		$myText = attr($record['myText']);
		$myTime = attr($record['myTime']);
		$myInteger = attr($record['myInteger']);
		$myFloat = attr($record['myFloat']);
		$myCheckbox = attr($record['myCheckbox']);
		$myTextarea = attr($record['myTextarea']);
		$myRadio = $record['myRadio'];
		($myRadio == 'n') ? ($myRadio_n = 'CHECKED') : ($myRadio_n = '');
		($myRadio == 'y') ? ($myRadio_y = 'CHECKED') : ($myRadio_y = '');
		($myRadio == 'unsure') ? ($myRadio_unsure = 'CHECKED') : ($myRadio_unsure = '');
		$myDate = attr($record['myDate']);
		?>
        <!-- ----------GENERATE---------------- -->
        <input type="hidden" name="csrf_token_form" value="<?php echo attr(CsrfUtils::collectCsrfToken()); ?>" />

        <?php echo "<span class='title'>" . xlt($form_name) . "</span>";?>
        <!-- <span class="title"><?php// echo xlt($form_name); ?></span> -->

        <!-- container for the main body of the form -->

        <div id="form_container">

            <div class="general">
<!-- ----------GENERATE---------------- -->
			<div>
				<label for='myText'>This is my Text input.</label>
			</div>
			<div>
			<?php echo "
				<input id='myText' name='myText' type='text' value='$myText' required>
			"; ?>
			</div>
			<div>
				<label for='myTime'>This is my Time input.</label>
			</div>
			<div>
			<?php echo"
				<input id='myTime' name='myTime' type='time' value='$myTime' required>
			"; ?>
			</div>
			<div>
				<label for='myInteger'>This is my integer input (0 to 100).</label>
			</div>
			<div>
			<?php echo"
				<input id='myInteger' name='myInteger' type='number' value='$myInteger' min='0' max='100' required>
			"; ?>
			</div>
			<div>
				<label for='myFloat'>This is my float input (0.00 to 99.99).</label>
			</div>
			<div>
			<?php echo"
				<input id='myFloat' name='myFloat' type='number' value='$myFloat' min='0.00' max='99.99' step='0.01' required>
			"; ?>
			</div>
			<div>
<label for='myCheckbox'>This is my checkbox (not set to required but pre-checked).</label>				<input type='checkbox' name='myCheckbox' value='on' <?php echo ($myCheckbox == 'on') ? 'checked' : ''; ?> >
			</div>
			<div>
				<label for='myTextarea'>Here is a textarea:</label>
			</div>
			<div>
				<?php echo "
				<textarea id='myTextarea' name='myTextarea' >$myTextarea</textarea>
				"; ?>
			</div>
			<div>
				<label for='myRadio'>Do you think this form maker is useful?</label>
			</div>
			<div>
			<?php echo "
				<label for='myRadio_n'>Not Really.</label>
<input type='radio' id='myRadio_n' name='myRadio' value='n' $myRadio_n required>
				<label for='myRadio_y'>Yes</label>
<input type='radio' id='myRadio_y' name='myRadio' value='y' $myRadio_y required>
				<label for='myRadio_unsure'>Rather not say.</label>
<input type='radio' id='myRadio_unsure' name='myRadio' value='unsure' $myRadio_unsure required>
			"; ?>
			</div>
			<div>
				<label for='myDate'>My Date set to January 31st, 2022</label>
			</div>
			<div>
			<?php echo "
				<input id='myDate' name='myDate' type='date' value='$myDate' required>
			"; ?>
			</div>
<!-- ----------GENERATE---------------- -->
                  <!-- Save/Cancel/Print buttons -->
				<?php echo "<button class='save'>Save</button>" ?>
                <?php echo "<input type='button' class='dontsave' value ='" . xla("Cancel") . "'>"; ?>
            </div> <!-- end form_container -->

    </form>

</body>

<script>
// jQuery stuff to make the page a little easier to use

$(function() {
    $(".save").click(function() {
        top.restoreSession();
        document.my_form.submit();
    });
    $(".dontsave").click(function() {
        parent.closeTab(window.name, false);
    });
    $('.datepicker').datetimepicker({
        <?php $datetimepicker_timepicker = false; ?>
        <?php $datetimepicker_showseconds = false; ?>
        <?php $datetimepicker_formatInput = false; ?>
        <?php require($GLOBALS['srcdir'] . '/js/xl/jquery-datetimepicker-2-5-4.js.php'); ?>
        <?php // can add any additional javascript settings to datetimepicker here; need to prepend first setting with a comma 
            ?>
    });
});
</script>

</html>


