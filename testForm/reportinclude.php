<?php
$uniqueReportId = $table_name . 'uniqueReport' . $id; 
//This is a unique identifier so that each time 
//yourFolderName_report($pid, $encounter, $cols, $id)
//is called, and the table is built, the table will have unique
//ids in their html elements.
$record = formFetch($table_name, $id); //fetch the current record

//use the fetched record to assign values
?>
<?php echo "<style>"; include_once("style.css"); echo "</style>";?>
<div id="<?php echo $uniqueReportId . '_report'; ?>" style="display:none;">
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
    <!-- container for the main body of the form -->

    <div class="general">
<!-- ----------GENERATE---------------- -->
			<div>
				<label for='myText'>This is my Text input.</label>
			</div>
			<div>
			<?php echo "
				<input type='text' value='$myText' disabled>
			"; ?>
			</div>
			<div>
				<label for='myTime'>This is my Time input.</label>
			</div>
			<div>
			<?php echo"
				<input type='time' value='$myTime' disabled>
			"; ?>
			</div>
			<div>
				<label for='myInteger'>This is my integer input (0 to 100).</label>
			</div>
			<div>
			<?php echo"
				<input type='number' value='$myInteger' disabled>
			"; ?>
			</div>
			<div>
				<label for='myFloat'>This is my float input (0.00 to 99.99).</label>
			</div>
			<div>
			<?php echo"
				<input type='number' value='$myFloat' disabled>
			"; ?>
			</div>
			<div>
<label for='myCheckbox'>This is my checkbox (not set to required but pre-checked).</label>				<input type='checkbox' <?php echo ($myCheckbox == 'on') ? 'checked' : ''; ?> disabled>
			</div>
			<div>
				<label for='myTextarea'>Here is a textarea:</label>
			</div>
			<div>
				<?php echo "
				<textarea disabled>$myTextarea</textarea>
				"; ?>
			</div>
			<div>
				<label for='myRadio'>Do you think this form maker is useful?</label>
			</div>
			<div>
			<?php echo "
				<label for='myRadio_n'>Not Really.</label>
<input type='radio' value='n' $myRadio_n disabled>
				<label for='myRadio_y'>Yes</label>
<input type='radio' value='y' $myRadio_y disabled>
				<label for='myRadio_unsure'>Rather not say.</label>
<input type='radio' value='unsure' $myRadio_unsure disabled>
			"; ?>
			</div>
			<div>
				<label for='myDate'>My Date set to January 31st, 2022</label>
			</div>
			<div>
			<?php echo "
				<input type='date' value='$myDate' disabled>
			"; ?>
			</div>
    </div>

    <script>
    //this will display or hide the report and change what the button says
    //it uses the button's id to determine which report to toggle
    function toggleReport(theId) {
        thisReport = document.getElementById(theId + "_report");
        thisButton = document.getElementById(theId);
        if (thisReport.style.display === "none") {
            thisReport.style.display = "unset";
            thisButton.innerHTML = "Hide Report";
        } else {
            thisReport.style.display = "none";
            thisButton.innerHTML = "Show Report";
        }
    }

    //this will display or hide the table and change what the button says
    //it uses the button's id to determine which report to toggle
    function toggleTable(theId) {
        populateTable(theId);
        let thisTable = document.getElementById(theId + "_table");
        let thisButton = document.getElementById(theId);
        if (thisTable.style.display === "none") {
            thisTable.style.display = "unset";
            thisButton.innerHTML = "Hide Table";
        } else {
            thisTable.style.display = "none";
            thisButton.innerHTML = "Show Table";
        }
    }

    //when called populates the contents of the div containing the table
    //it checks the id of the button pressed to determine which table on the 
    //page to populate
    function populateTable(theId) {
        let thisTableInnerDiv = document.getElementById(theId + "_table_inner_div");
        if (thisTableInnerDiv.innerText.trim() === "") {
            let fields = Object.keys(tableContents[0]);
            //    Here you could opt to show field names instead of manually setting below
            str = "<table>";
            str += "<tr>";
            for (let i = 0; i < fields.length; i++) {
                str += "<th>" + fields[i] + "</th>";
            }
            str += "</tr>";
            for (let i = 0; i < tableContents.length; i++) {
                str += "<tr>";
                for (let j = 0; j < fields.length; j++) {
                    str += "<td>" + tableContents[i][fields[j]] + "</td>";
                }
                str += "</tr>";
            }
            str += "</table>";
            //str = JSON.stringify(tableContents);
            thisTableInnerDiv.innerHTML = str;
        }
    }

    //it uses then id of the start date or end date filter to determine which table to change
    function changeTable() {
        let reportTableBaseName = "";
        if (this.id.includes("_start_filter_value")) {
            reportTableBaseName = this.id.split("_start_filter_value")[0];
        } else if (this.id.includes("_end_filter_value")) {
            reportTableBaseName = this.id.split("_end_filter_value")[0];
        }
        let thisStartFilterValue = document.getElementById(reportTableBaseName + "_start_filter_value").value.trim();
        let thisEndFilterValue = document.getElementById(reportTableBaseName + "_end_filter_value").value.trim();
        //four cases,   start "",           end ""              make no comparisons, show all  OO
        //              start something,    end ""              check only start               XO
        //              start "",           end something       check only end                 OX
        //              start something,    end something       check start and end            XX
        let thisTableInnerDiv = document.getElementById(reportTableBaseName + "_table_button_table_inner_div");

        let tableString = "";

        let fields = Object.keys(tableContents[0]);
        //    Here you could opt to show field names instead of manually setting below
        tableString = "<table>";
        tableString += "<tr>";
        for (let i = 0; i < fields.length; i++) {
            tableString += "<th>" + fields[i] + "</th>";
        }
        tableString += "</tr>";
        for (let i = 0; i < tableContents.length; i++) {
            if ((thisStartFilterValue === "") && (thisEndFilterValue === "")) { //OO
                tableString += "<tr>";
                for (let j = 0; j < fields.length; j++) {
                    tableString += "<td>" + tableContents[i][fields[j]] + "</td>";
                }
                tableString += "</tr>";
            } else if ((thisStartFilterValue != "") && (thisEndFilterValue === "")) { //XO
                if (tableContents[i][orderByVariable] >= thisStartFilterValue) {
                    tableString += "<tr>";
                    for (let j = 0; j < fields.length; j++) {
                        tableString += "<td>" + tableContents[i][fields[j]] + "</td>";
                    }
                    tableString += "</tr>";
                }
            } else if ((thisStartFilterValue === "") && (thisEndFilterValue != "")) { //OX
                if (tableContents[i][orderByVariable] <= thisEndFilterValue) {
                    tableString += "<tr>";
                    for (let j = 0; j < fields.length; j++) {
                        tableString += "<td>" + tableContents[i][fields[j]] + "</td>";
                    }
                    tableString += "</tr>";
                }
            } else if ((thisStartFilterValue != "") && (thisEndFilterValue != "")) { //XX
                if ((tableContents[i][orderByVariable] >= thisStartFilterValue) && (tableContents[i][orderByVariable] <=
                        thisEndFilterValue)) {
                    tableString += "<tr>";
                    for (let j = 0; j < fields.length; j++) {
                        tableString += "<td>" + tableContents[i][fields[j]] + "</td>";
                    }
                    tableString += "</tr>";
                }
            }
        }
        tableString+="</table>";
        thisTableInnerDiv.innerHTML = tableString;
    }
    </script>
</div>

<?php

//This SQL query gets all results for this patient, not just the current encouter.

////////////////////////////////////////////GENERATE/////////////////////////////////////
$result = sqlStatement("SELECT * FROM $table_name WHERE pid=$pid ORDER BY myDate ASC;");
$orderByVariable = 'myDate';
$orderByType = 'date';
$fieldNamesArray = array('myText','myTime','myInteger','myFloat','myCheckbox','myTextarea','myRadio','myDate');


//////////////////////////////////////////////////////////////////////////////////////////
$numberOfFields = count($fieldNamesArray);

$showTableButtonAndCSVButton = "";
if ($numberOfFields<=0){
    $showTableButtonAndCSVButton =" style='display:none;' ";;
}

echo "<script>orderByVariable='$orderByVariable';</script>";  //using non-strict mode declaration of object
//$result_set = array(); //all results from sql query, just in case this is needed in the future
$table_data = array(); //just the field results we need for building the table

$row_count = 0;

echo "<script>
	tableContents=[];
	</script>";

$fieldCount = count($fieldNamesArray);

while ($row = sqlFetchArray($result)) { //using api function given in the program
	//$result_set[] = $row;

    for ($i = 0; $i < $fieldCount; $i++) {
        $table_data[$row_count][$fieldNamesArray[$i]] = $row[$fieldNamesArray[$i]];;
    }
    
    $row_count = $row_count + 1;
}

//make a json string from the table data and echo this into javascript to
//be used dynamically on the page
$jsonTableDataString = json_encode($table_data);
echo "<script>tableContents=$jsonTableDataString;</script>";  //using non-strict mode declaration of object
?>

<script>
//This function takes the current table turns it into csv
//(convention is double quote all data, no trailing spaces, one \n newline per data line)

//Uses the id of the button clicked to determine which table to convert to csv 
function convertTableToCSV(theId) {
    let str = "";
    let fields = [];
    //figuring out which button clicked
    let reportTableBaseName = theId.split("_csv_button")[0];
    let thisStartFilterValue = document.getElementById(reportTableBaseName + "_start_filter_value").value.trim();
    let thisEndFilterValue = document.getElementById(reportTableBaseName + "_end_filter_value").value.trim();

    //four cases,   start "",           end ""              make no comparisons, show all  OO
    //              start something,    end ""              check only start               XO
    //              start "",           end something       check only end                 OX
    //              start something,    end something       check start and end            XX

    if (tableContents.length > 0) { //only if there is at least one line to put in table
        let fields = Object.keys(tableContents[0]);
        //    Here you could opt to show field names instead of manually setting below
        for (let i = 0; i < fields.length; i++) {
            str += "\"";
            str += fields[i];
            str += "\",";
        }
        str = str.substr(0, str.length - 1);
        str += "\n";

        //build the table

        for (let i = 0; i < tableContents.length; i++) {
            if ((thisStartFilterValue === "") && (thisEndFilterValue === "")) { //OO
                for (let field in tableContents[i]) {
                    str += "\"";
                    str += tableContents[i][field];
                    str += "\",";
                }
                str = str.substr(0, str.length - 1);
                str += "\n";
            } else if ((thisStartFilterValue != "") && (thisEndFilterValue === "")) { //XO
                if (tableContents[i][orderByVariable] >= thisStartFilterValue) {
                    for (let field in tableContents[i]) {
                        str += "\"";
                        str += tableContents[i][field];
                        str += "\",";
                    }
                    str = str.substr(0, str.length - 1);
                    str += "\n";
                }
            } else if ((thisStartFilterValue === "") && (thisEndFilterValue != "")) { //OX
                if (tableContents[i][orderByVariable] <= thisEndFilterValue) {
                    for (let field in tableContents[i]) {
                        str += "\"";
                        str += tableContents[i][field];
                        str += "\",";
                    }
                    str = str.substr(0, str.length - 1);
                    str += "\n";
                }
            } else if ((thisStartFilterValue != "") && (thisEndFilterValue != "")) { //XX
                if ((tableContents[i][orderByVariable] >= thisStartFilterValue) && (tableContents[i][orderByVariable] <=
                        thisEndFilterValue)) {
                    for (let field in tableContents[i]) {
                        str += "\"";
                        str += tableContents[i][field];
                        str += "\",";
                    }
                    str = str.substr(0, str.length - 1);
                    str += "\n";
                }
            }
        }
    }
    console.log("Here are the csv contents you requested:");
    console.log("---------------------------------------");
    console.log(str);
    console.log();
    if (str.trim() != "") { //don't offer to save an empty string
        saveStringToTextFile(str);
    }
}

//general function to saves a string to a file, only using first argument in this program currently
function saveStringToTextFile(str1, fileName = "myCSVFile", fileType = ".csv", addDate = false) {
    let saveFileName = fileName;
    let dateString = '';

    if (addDate === true) {
        //make a string representing the date to add on to the filename
        dateString = (new Date()).toLocaleString();
        dateString = "_" + dateString.replaceAll("/", "_").replaceAll(",", "_").replaceAll(" ", "_").replaceAll(":",
            "_");
    }

    saveFileName = fileName + dateString + fileType;

    //place data in blob and use to make a file for download
    let blobVersionOfText = new Blob([str1], {
        type: "text/plain"
    });
    let urlToBlob = window.URL.createObjectURL(blobVersionOfText);
    let downloadLink = document.createElement("a");
    downloadLink.style.display = "none";
    downloadLink.download = saveFileName;
    downloadLink.href = urlToBlob;
    document.body.appendChild(downloadLink);
    downloadLink.click();
    downloadLink.parentElement.removeChild(downloadLink);
}
</script>


<!-- Here is the div for the table data contents -->
<div id="<?php echo $uniqueReportId . '_table_button_table'; ?>" style="display:none;">
    <div class='general report-table' id="<?php echo $uniqueReportId . '_table_button_table_inner_div'; ?>"></div>

    <?php
$showOrderInputs = "";
if ($orderByVariable===""){
    $showOrderInputs=" style='display:none;' ";
} 
?>

    <div class='general' <?php echo $showOrderInputs;?>>
        <label for="<?php echo $uniqueReportId . '_start_filter_value'; ?>">Start:</label>
        <input type='<?php echo $orderByType;?>' id="<?php echo $uniqueReportId . '_start_filter_value'; ?>">
        <label for="<?php echo $uniqueReportId . '_end_filter_value'; ?>">End:</label>
        <input type='<?php echo $orderByType;?>' id="<?php echo $uniqueReportId . '_end_filter_value'; ?>">
    </div>


</div>

<!-- Buttons for toggling report, toggling table and csv -->
<div>
    <button id='<?php echo $uniqueReportId ?>' onclick="toggleReport(this.id)">Show Report</button>
    <button id='<?php echo $uniqueReportId . "_table_button" ;?>' <?php echo $showTableButtonAndCSVButton;?>
        onclick="toggleTable(this.id);populateTable(this.id);">Show Table</button>
    <button id='<?php echo $uniqueReportId . "_csv_button";?>' <?php echo $showTableButtonAndCSVButton;?>
        onclick="{convertTableToCSV(this.id);}">Download
        CSV</button>
</div>

<!-- Add event listeners to the tables start date and end date to call the changeTable function and repopulate the table -->
<script>
document.getElementById("<?php echo $uniqueReportId . '_start_filter_value'; ?>").addEventListener('change',
    changeTable);
document.getElementById("<?php echo $uniqueReportId . '_end_filter_value'; ?>").addEventListener('change', changeTable);
</script>
