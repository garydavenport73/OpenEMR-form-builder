import json
import os
infile = open('input.json','r')
data = json.load(infile)
infile.close()
 
print(data)
print()
print(data["folderName"])
print(data["formName"])

def make_folder(data):
    os.makedirs(data["folderName"],exist_ok=True)

def make_newphp(data): 
    
    form_name = data["formName"]
    form_folder = data["folderName"]
    
    str="<?php\n\nrequire_once(\"../../globals.php\");\nrequire_once(\"$srcdir/api.inc\");\n\nuse OpenEMR\\Common\\Csrf\\CsrfUtils;\nuse OpenEMR\\Core\\Header;\n"

    str+="// -------GENERATE--------\n"
    str+="$form_name = '"+form_name+"';\n"
    str+="$form_folder = '"+form_folder+"';\n"
    str+="// -----------------------\n"
    
    str+="\nformHeader(\"Form: \" . $form_name);\n$returnurl = \'encounter_top.php\';\n\n?>\n\n<html>\n\n<head>\n    <!-- assets -->\n    <?php Header::setupHeader(\'datetime-picker\'); ?>\n    <link rel=\"stylesheet\" href=\"../../forms/<?php echo $form_folder; ?>/style.css?v=<?php echo $v_js_includes; ?>\">\n    <?php echo \"<style>\"; include_once(\"style.css\"); echo \"</style>\";?>\n\n</head>\n\n<body class=\"body_top\">\n\n    <?php echo date(\"F d, Y\", time()); ?>\n    <form method=post action=\"<?php echo $rootdir; ?>/forms/<?php echo $form_folder; ?>/save.php?mode=new\" name=\"my_form\">\n"

    str+="<!-- ----------GENERATE---------------- -->\n\n    <?php\n"

    #loop through variables 
    for i in range(len(data["inputs"])):
        inputType = data["inputs"][i]["type"]
        name = data["inputs"][i]["properties"]["name"]

        if inputType == "text":
            try:
                value = data["inputs"][i]["properties"]["value"]
            except:
                value = ""
            str+="\t\t$" + name + " = '"+value+"';\n"
        elif inputType == "date":
            try:
                value = data["inputs"][i]["properties"]["value"]
            except:
                value = ""
            str+="\t\t$" + name + " = '"+value+"';\n"
        elif inputType == "time":
            try:
                value = data["inputs"][i]["properties"]["value"]
            except:
                value = ""
            str+="\t\t$" + name + " = '"+value+"';\n"
        elif inputType == "integer":
            try:
                value = data["inputs"][i]["properties"]["value"]
            except:
                value = ""
            str+="\t\t$" + name + " = '"+value+"';\n"
        elif inputType == "float":
            try:
                value = data["inputs"][i]["properties"]["value"]
            except:
                value = ""
            str+="\t\t$" + name + " = '"+value+"';\n"
        elif inputType == "checkbox":
            try:
                value = data["inputs"][i]["properties"]["value"]
            except:
                value = "on"
            str+="\t\t$" + name + " = '"+value+"';\n"
        elif inputType == "textarea":
            try:
                value = data["inputs"][i]["properties"]["value"]
            except:
                value = ""
            str+="\t\t$" + name + " = '"+value+"';\n"
        elif inputType == "datetimepicker":
            try:
                value = "'"+data["inputs"][i]["properties"]["value"]+"'"
            except:
                value = "date('Y-m-d', time())"
            str+="\t\t$" + name + " = "+value+";\n"
        elif inputType == "radio":
            str+="\t\t$" + name + " = '';\n"
            buttons = data["inputs"][i]["properties"]["buttons"]
            for j in range(len(buttons)):
                value = buttons[j]['value']
                str+="\t\t($"+name+" == '"+value+"') ? ($"+name+"_"+value+" = 'CHECKED') : ($"+name+"_"+value+" = '');\n"

    str+="    ?> \n<!-- ----------GENERATE---------------- -->\n"
    str+="        <input type=\"hidden\" name=\"csrf_token_form\" value=\"<?php echo attr(CsrfUtils::collectCsrfToken()); ?>\" />\n\n        <?php echo \"<span class=\'title\'>\" . xlt($form_name) . \"</span>\";?>\n        <!-- <span class=\"title\"><?php// echo xlt($form_name); ?></span> -->\n\n        <!-- container for the main body of the form -->\n\n        <div id=\"form_container\">\n\n            <div class=\"general\">\n"
    str+="<!-- ----------GENERATE---------------- -->\n"
    for i in range(len(data["inputs"])):
        inputType = data["inputs"][i]["type"]
        name = data["inputs"][i]["properties"]["name"]
        label = data["inputs"][i]["properties"]["label"]
        try:
            isRequired = data["inputs"][i]["properties"]["required"]
        except:
            isRequired = ""
        if inputType!="checkbox":
            str+="\t\t\t<div>\n"
            str+="\t\t\t\t<label for='"+name+"'>"+label+"</label>\n"
            str+="\t\t\t</div>\n"
        if inputType == "text":
            str+="\t\t\t<div>\n"
            str+="\t\t\t<?php echo \"\n"
            str+="\t\t\t\t<input id='"+name+"' name='"+name+"' type='text' value='$"+name+"' " + isRequired +">\n"
            str+="\t\t\t\"; ?>\n"
            str+="\t\t\t</div>\n"
        elif inputType == "date":
            str+="\t\t\t<div>\n"
            str+="\t\t\t<?php echo \"\n"
            str+="\t\t\t\t<input id='"+name+"' name='"+name+"' type='date' value='$"+name+"' " + isRequired +">\n"
            str+="\t\t\t\"; ?>\n"
            str+="\t\t\t</div>\n"
        elif inputType == "time":
            str+="\t\t\t<div>\n"
            str+="\t\t\t<?php echo\"\n"
            str+="\t\t\t\t<input id='"+name+"' name='"+name+"' type='time' value='$"+name+"' " + isRequired +">\n"
            str+="\t\t\t\"; ?>\n"
            str+="\t\t\t</div>\n"
        elif inputType == "checkbox":
            try:
                checked = data["inputs"][i]["properties"]["checked"]
            except:
                checked = ""
            try:
                value = data["inputs"][i]["properties"]["value"]
            except:
                value = "on"
            str+="\t\t\t<div>\n"
            str+="<label for='"+name+"'>"+label+"</label>"
            str+="\t\t\t<?php echo\"\n"
            str+="\t\t\t\t<input id='"+name+"' name='"+name+"' type='checkbox' value='"+value+"' "+checked+" " +isRequired +">\n"
            str+="\t\t\t\"; ?>\n"
            str+="\t\t\t</div>\n"
        elif inputType == "integer":
            try:
                max = data["inputs"][i]["properties"]["max"]
            except:
                max = ""
            try:
                min = data["inputs"][i]["properties"]["min"]
            except:
                min = ""
            str+="\t\t\t<div>\n"
            str+="\t\t\t<?php echo\"\n"
            str+="\t\t\t\t<input id='"+name+"' name='"+name+"' type='number' value='$"+name+"' min='"+min+"' max='"+max+"' " + isRequired +">\n"
            str+="\t\t\t\"; ?>\n"
            str+="\t\t\t</div>\n"
        elif inputType == "float":
            try:
                max = data["inputs"][i]["properties"]["max"]
            except:
                max = ""
            try:
                min = data["inputs"][i]["properties"]["min"]
            except:
                min = ""
            try:
                step = data["inputs"][i]["properties"]["step"]
            except:
                step = ""
            str+="\t\t\t<div>\n"
            str+="\t\t\t<?php echo\"\n"
            str+="\t\t\t\t<input id='"+name+"' name='"+name+"' type='number' value='$"+name+"' min='"+min+"' max='"+max+"' step='"+step+"' " + isRequired +">\n"
            str+="\t\t\t\"; ?>\n"
            str+="\t\t\t</div>\n"
        elif inputType == "textarea":
            str+="\t\t\t<div>\n"
            str+="\t\t\t\t<?php echo \"\n"
            str+="\t\t\t\t<textarea id='"+name+"' name='"+name+"' "+isRequired+">$"+name+"</textarea>\n"
            str+="\t\t\t\t\"; ?>\n"
            str+="\t\t\t</div>\n"
        elif inputType == "datetimepicker":
            str+="\t\t\t<div>\n"
            str+="\t\t\t\t<?php\n"
            str+="\t\t\t\techo \"<input type='text' class='datepicker' id='"+name+"' name='"+name+"' value='\" . $"+name+" . \"' title='\" . xla('yyyy-mm-dd') . \"' "+isRequired+">\"\n"
            str+="\t\t\t\t?>\n"                    
            str+="\t\t\t</div>\n"
        elif inputType == "radio":
            str+="\t\t\t<div>\n"
            str+="\t\t\t<?php echo \"\n"
            buttons = data["inputs"][i]["properties"]["buttons"]
            for j in range(len(buttons)):
                value = buttons[j]['value']
                label = buttons[j]['label']
                str+="\t\t\t\t<label for='"+name+"_"+value+"'>"+label+"</label>\n<input type='radio' id='"+name+"_"+value+"' name='"+name+"' value='"+value+"' $"+name+"_"+value+" "+isRequired+">\n"
            str+="\t\t\t\"; ?>\n"        
            str+="\t\t\t</div>\n"
    str+="<!-- ----------GENERATE---------------- -->\n                <!-- Save/Cancel/Print buttons -->\n\t\t\t\t<?php echo \"<button class=\'save\'>Save</button>\" ?>\n                <?php echo \"<input type=\'button\' class=\'dontsave\' value =\'\" . xla(\"Cancel\") . \"\'>\"; ?>\n\n            </div>\n        </div> <!-- end form_container -->\n    </form>\n</body>\n\n<script>\n// jQuery stuff to make the page a little easier to use\n\n$(function() {\n    $(\".save\").click(function() {\n        top.restoreSession();\n        document.my_form.submit();\n    });\n    $(\".dontsave\").click(function() {\n        parent.closeTab(window.name, false);\n    });\n    $(\".printform\").click(function() {\n        PrintForm();\n    });\n\n    $(\'.datepicker\').datetimepicker({\n        <?php $datetimepicker_timepicker = false; ?>\n        <?php $datetimepicker_showseconds = false; ?>\n        <?php $datetimepicker_formatInput = false; ?>\n        <?php require($GLOBALS[\'srcdir\'] . \'/js/xl/jquery-datetimepicker-2-5-4.js.php\'); ?>\n        <?php // can add any additional javascript settings to datetimepicker here; need to prepend first setting with a comma \n            ?>\n    });\n});\n</script>\n\n</html>\n\n"
    outfile = open(form_folder+"/new.php","w")
    outfile.write(str)
    outfile.close()

def make_viewphp(data):
    form_name = data["formName"]
    form_folder = data["folderName"]
    table_name = "form_" + form_folder
    
    str="<?php\n\nrequire_once(\"../../globals.php\");\nrequire_once(\"$srcdir/api.inc\");\n\nuse OpenEMR\\Common\\Csrf\\CsrfUtils;\nuse OpenEMR\\Core\\Header;\n"

    str+="// -------GENERATE--------\n"
    str+="$form_name = '"+form_name+"';\n"
    str+="$form_folder = '"+form_folder+"';\n"
    str+="// -----------------------\n"

    str+="\nformHeader(\"Form: \" . $form_name);\n$returnurl = \'encounter_top.php\';\n\n//------------GENERATE----------------\n"

    str+="$table_name = '"+table_name+"';\n"

    str+="\n/* load the saved record */\n"
    str+="$record = formFetch($table_name, $_GET['id']);\n"
    str+="\n/* remove the time-of-day from the date fields \n"
    str+="Will need written through and looped in text writing program\n"
    str+="*/\n"

    #check all records to see if they are datetimepicker if so change
    for i in range(len(data["inputs"])):
        inputType = data["inputs"][i]["type"]
        name = data["inputs"][i]["properties"]["name"]
        if inputType == "datetimepicker":
            str+="if ($record['"+name+"'] != '') {\n"
            str+="\t$dateparts = explode(' ', $record['"+name+"']);\n"
            str+="\t$record['"+name+"'] = $dateparts[0];\n}\n\n"

    str+="//------------GENERATE----------------------\n?>\n\n<html>\n\n<head>\n        <!-- assets -->\n    <?php Header::setupHeader(\'datetime-picker\'); ?>\n    <link rel=\"stylesheet\" href=\"../../forms/<?php echo $form_folder; ?>/style.css?v=<?php echo $v_js_includes; ?>\">\n    <?php echo \"<style>\"; include_once(\"style.css\"); echo \"</style>\";?>\n\n</head>\n\n<body class=\"body_top\">\n\n    <?php echo date(\"F d, Y\", time()); ?>\n<!-- ----------GENERATE---------------- -->\n    <form method=post\n        action=\"<?php echo $rootdir; ?>/forms/<?php echo $form_folder; ?>/save.php?mode=update&id=<?php echo attr_url($_GET[\"id\"]); ?>\"\n        name=\"my_form\">\n\t\t<?php\n"

    #loop through variables 
    for i in range(len(data["inputs"])):
        inputType = data["inputs"][i]["type"]
        name = data["inputs"][i]["properties"]["name"]

        if inputType == "text":
            str+="\t\t$" + name + " = attr($record['"+name+"']);\n"
        elif inputType == "date":
            str+="\t\t$" + name + " = attr($record['"+name+"']);\n"
        elif inputType == "time":
            str+="\t\t$" + name + " = attr($record['"+name+"']);\n" ###########################
        elif inputType == "checkbox":
            str+="\t\t$" + name + " = attr($record['"+name+"']);\n"
        elif inputType == "integer":
            str+="\t\t$" + name + " = attr($record['"+name+"']);\n"
        elif inputType == "float":
            str+="\t\t$" + name + " = attr($record['"+name+"']);\n"
        elif inputType == "textarea":
            str+="\t\t$" + name + " = attr($record['"+name+"']);\n"
        elif inputType == "datetimepicker":
            str+="\t\t$" + name + " = attr($record['"+name+"']);\n"
        elif inputType == "radio":
            str+="\t\t$" + name + " = $record['"+name+"'];\n"
            buttons = data["inputs"][i]["properties"]["buttons"]
            for j in range(len(buttons)):
                value = buttons[j]['value']
                str+="\t\t($"+name+" == '"+value+"') ? ($"+name+"_"+value+" = 'CHECKED') : ($"+name+"_"+value+" = '');\n"

    str+="\t\t?>\n        <!-- ----------GENERATE---------------- -->\n        <input type=\"hidden\" name=\"csrf_token_form\" value=\"<?php echo attr(CsrfUtils::collectCsrfToken()); ?>\" />\n\n        <?php echo \"<span class=\'title\'>\" . xlt($form_name) . \"</span>\";?>\n        <!-- <span class=\"title\"><?php// echo xlt($form_name); ?></span> -->\n\n        <!-- container for the main body of the form -->\n\n        <div id=\"form_container\">\n\n            <div class=\"general\">\n"

    str+="<!-- ----------GENERATE---------------- -->\n"
    for i in range(len(data["inputs"])):
        inputType = data["inputs"][i]["type"]
        name = data["inputs"][i]["properties"]["name"]
        label = data["inputs"][i]["properties"]["label"]
        try:
            isRequired = data["inputs"][i]["properties"]["required"]
        except:
            isRequired = "" 
        if inputType!="checkbox":
            str+="\t\t\t<div>\n"
            str+="\t\t\t\t<label for='"+name+"'>"+label+"</label>\n"
            str+="\t\t\t</div>\n"
        if inputType == "text":
            str+="\t\t\t<div>\n"
            str+="\t\t\t<?php echo \"\n"
            str+="\t\t\t\t<input id='"+name+"' name='"+name+"' type='text' value='$"+name+"' " + isRequired +">\n"
            str+="\t\t\t\"; ?>\n"
            str+="\t\t\t</div>\n"
        if inputType == "date":
            str+="\t\t\t<div>\n"
            str+="\t\t\t<?php echo \"\n"
            str+="\t\t\t\t<input id='"+name+"' name='"+name+"' type='date' value='$"+name+"' " + isRequired +">\n"
            str+="\t\t\t\"; ?>\n"
            str+="\t\t\t</div>\n"
        elif inputType == "time":
            str+="\t\t\t<div>\n"
            str+="\t\t\t<?php echo\"\n"
            str+="\t\t\t\t<input id='"+name+"' name='"+name+"' type='time' value='$"+name+"' " + isRequired +">\n"
            str+="\t\t\t\"; ?>\n"
            str+="\t\t\t</div>\n"
        elif inputType == "checkbox":
            try:
                value = data["inputs"][i]["properties"]["value"]
            except:
                value = "on"

            str+="\t\t\t<div>\n"
            #str+="\t\t\t<?php echo\"\n"
            str+="<label for='"+name+"'>"+label+"</label>"
            
            str+="\t\t\t\t<input type='checkbox' name='"+name+"' value='"+ value +"' <?php echo ($" + name + " == '"+value+"') ? 'checked' : ''; ?> "+isRequired+">\n"
            #str+="\t\t\t\"; ?>\n"
            str+="\t\t\t</div>\n"
        elif inputType == "integer":
            try:
                max = data["inputs"][i]["properties"]["max"]
            except:
                max = ""
            try:
                min = data["inputs"][i]["properties"]["min"]
            except:
                min = ""
            str+="\t\t\t<div>\n"
            str+="\t\t\t<?php echo\"\n"
            str+="\t\t\t\t<input id='"+name+"' name='"+name+"' type='number' value='$"+name+"' min='"+min+"' max='"+max+"' " + isRequired +">\n"
            str+="\t\t\t\"; ?>\n"
            str+="\t\t\t</div>\n"
        elif inputType == "float":
            try:
                max = data["inputs"][i]["properties"]["max"]
            except:
                max = ""
            try:
                min = data["inputs"][i]["properties"]["min"]
            except:
                min = ""
            try:
                step = data["inputs"][i]["properties"]["step"]
            except:
                step = ""
            str+="\t\t\t<div>\n"
            str+="\t\t\t<?php echo\"\n"
            str+="\t\t\t\t<input id='"+name+"' name='"+name+"' type='number' value='$"+name+"' min='"+min+"' max='"+max+"' step='"+step+"' " + isRequired +">\n"
            str+="\t\t\t\"; ?>\n"
            str+="\t\t\t</div>\n"
        elif inputType == "textarea":
            str+="\t\t\t<div>\n"
            str+="\t\t\t\t<?php echo \"\n"
            str+="\t\t\t\t<textarea id='"+name+"' name='"+name+"' "+isRequired+">$"+name+"</textarea>\n"
            str+="\t\t\t\t\"; ?>\n"
            str+="\t\t\t</div>\n"
        elif inputType == "datetimepicker":
            str+="\t\t\t<div>\n"
            str+="\t\t\t\t<?php\n"
            str+="\t\t\t\techo \"<input type='text' class='datepicker' id='"+name+"' name='"+name+"' value='\" . $"+name+" . \"' title='\" . xla('yyyy-mm-dd') . \"' "+isRequired+">\"\n"
            str+="\t\t\t\t?>\n"                    
            str+="\t\t\t</div>\n"
        elif inputType == "radio":
            str+="\t\t\t<div>\n"
            str+="\t\t\t<?php echo \"\n"
            buttons = data["inputs"][i]["properties"]["buttons"]
            for j in range(len(buttons)):
                value = buttons[j]['value']
                label = buttons[j]['label']
                str+="\t\t\t\t<label for='"+name+"_"+value+"'>"+label+"</label>\n<input type='radio' id='"+name+"_"+value+"' name='"+name+"' value='"+value+"' $"+name+"_"+value+" "+isRequired+">\n"
            str+="\t\t\t\"; ?>\n"        
            str+="\t\t\t</div>\n"
    str+="<!-- ----------GENERATE---------------- -->\n                  <!-- Save/Cancel/Print buttons -->\n\t\t\t\t<?php echo \"<button class=\'save\'>Save</button>\" ?>\n                <?php echo \"<input type=\'button\' class=\'dontsave\' value =\'\" . xla(\"Cancel\") . \"\'>\"; ?>\n            </div> <!-- end form_container -->\n\n    </form>\n\n</body>\n\n<script>\n// jQuery stuff to make the page a little easier to use\n\n$(function() {\n    $(\".save\").click(function() {\n        top.restoreSession();\n        document.my_form.submit();\n    });\n    $(\".dontsave\").click(function() {\n        parent.closeTab(window.name, false);\n    });\n    $(\'.datepicker\').datetimepicker({\n        <?php $datetimepicker_timepicker = false; ?>\n        <?php $datetimepicker_showseconds = false; ?>\n        <?php $datetimepicker_formatInput = false; ?>\n        <?php require($GLOBALS[\'srcdir\'] . \'/js/xl/jquery-datetimepicker-2-5-4.js.php\'); ?>\n        <?php // can add any additional javascript settings to datetimepicker here; need to prepend first setting with a comma \n            ?>\n    });\n});\n</script>\n\n</html>\n\n\n"

    outfile = open(form_folder+"/view.php","w")
    outfile.write(str)
    outfile.close()

def make_reportincludewithtablephp(data):
    form_name = data["formName"]
    form_folder = data["folderName"]
    table_name = "form_" + form_folder

    orderByField = ""
    orderByStatement = ""
    orderByType = ""

    try:
        orderByField = data["orderByField"]
        orderByStatement= "ORDER BY " + orderByField
    except:
        orderByField = ""
        orderByStatement = ""

    order=""
    if orderByField!="":
        try:
            order = data["order"]
        except:
            order = ""
    if orderByField!="":
        for i in range(len(data["inputs"])):
            if data["inputs"][i]["properties"]["name"]==orderByField:
                orderByType=data["inputs"][i]["type"]

        ##########################
        
    str="<?php\n$uniqueReportId = $table_name . \'uniqueReport\' . $id; \n//This is a unique identifier so that each time \n//yourFolderName_report($pid, $encounter, $cols, $id)\n//is called, and the table is built, the table will have unique\n//ids in their html elements.\n$record = formFetch($table_name, $id); //fetch the current record\n\n//use the fetched record to assign values\n?>\n<?php echo \"<style>\"; include_once(\"style.css\"); echo \"</style>\";?>\n<div id=\"<?php echo $uniqueReportId . \'_report\'; ?>\" style=\"display:none;\">\n    <?php\n"

      #loop through variables 
    for i in range(len(data["inputs"])):
        inputType = data["inputs"][i]["type"]
        name = data["inputs"][i]["properties"]["name"]

        if inputType == "text":
            str+="\t\t$" + name + " = attr($record['"+name+"']);\n"
        elif inputType == "date":
            str+="\t\t$" + name + " = attr($record['"+name+"']);\n"
        elif inputType == "time":
            str+="\t\t$" + name + " = attr($record['"+name+"']);\n" ###########################
        elif inputType == "checkbox":
            str+="\t\t$" + name + " = attr($record['"+name+"']);\n"
        elif inputType == "integer":
            str+="\t\t$" + name + " = attr($record['"+name+"']);\n"
        elif inputType == "float":
            str+="\t\t$" + name + " = attr($record['"+name+"']);\n"
        elif inputType == "textarea":
            str+="\t\t$" + name + " = attr($record['"+name+"']);\n"
        elif inputType == "radio":
            str+="\t\t$" + name + " = $record['"+name+"'];\n"
            buttons = data["inputs"][i]["properties"]["buttons"]
            for j in range(len(buttons)):
                value = buttons[j]['value']
                str+="\t\t($"+name+" == '"+value+"') ? ($"+name+"_"+value+" = 'CHECKED') : ($"+name+"_"+value+" = '');\n"
    str+="?>\n    <!-- container for the main body of the form -->\n\n    <div class=\"general\">\n"
    str+="<!-- ----------GENERATE---------------- -->\n"
    for i in range(len(data["inputs"])):
        inputType = data["inputs"][i]["type"]
        name = data["inputs"][i]["properties"]["name"]
        label = data["inputs"][i]["properties"]["label"]
        if inputType!="checkbox":
            str+="\t\t\t<div>\n"
            str+="\t\t\t\t<label for='"+name+"'>"+label+"</label>\n"
            str+="\t\t\t</div>\n"
        if inputType == "text":
            str+="\t\t\t<div>\n"
            str+="\t\t\t<?php echo \"\n"
            str+="\t\t\t\t<input type='text' value='$"+name+"' disabled>\n"
            str+="\t\t\t\"; ?>\n"
            str+="\t\t\t</div>\n"
        elif inputType == "date":
            str+="\t\t\t<div>\n"
            str+="\t\t\t<?php echo \"\n"
            str+="\t\t\t\t<input type='date' value='$"+name+"' disabled>\n"
            str+="\t\t\t\"; ?>\n"
            str+="\t\t\t</div>\n"
        elif inputType == "time":
            str+="\t\t\t<div>\n"
            str+="\t\t\t<?php echo\"\n"
            str+="\t\t\t\t<input type='time' value='$"+name+"' disabled>\n"
            str+="\t\t\t\"; ?>\n"
            str+="\t\t\t</div>\n"
        elif inputType == "checkbox":
            try:
                value = data["inputs"][i]["properties"]["value"]
            except:
                value = "on"
            str+="\t\t\t<div>\n"
            #str+="\t\t\t<?php echo\"\n"
            str+="<label for='"+name+"'>"+label+"</label>"
            str+="\t\t\t\t<input type='checkbox' <?php echo ($"+name+" == '"+value+"') ? 'checked' : ''; ?> disabled>\n"
            #str+="\t\t\t\"; ?>\n"
            str+="\t\t\t</div>\n"
        elif inputType == "integer":
            str+="\t\t\t<div>\n"
            str+="\t\t\t<?php echo\"\n"
            str+="\t\t\t\t<input type='number' value='$"+name+"' disabled>\n"
            str+="\t\t\t\"; ?>\n"
            str+="\t\t\t</div>\n"
        elif inputType == "float":
            str+="\t\t\t<div>\n"
            str+="\t\t\t<?php echo\"\n"
            str+="\t\t\t\t<input type='number' value='$"+name+"' disabled>\n"
            str+="\t\t\t\"; ?>\n"
            str+="\t\t\t</div>\n"
        elif inputType == "textarea":
            str+="\t\t\t<div>\n"
            str+="\t\t\t\t<?php echo \"\n"
            str+="\t\t\t\t<textarea disabled>$"+name+"</textarea>\n"
            str+="\t\t\t\t\"; ?>\n"
            str+="\t\t\t</div>\n"
        elif inputType == "radio":
            str+="\t\t\t<div>\n"
            str+="\t\t\t<?php echo \"\n"
            buttons = data["inputs"][i]["properties"]["buttons"]
            for j in range(len(buttons)):
                value = buttons[j]['value']
                label = buttons[j]['label']
                str+="\t\t\t\t<label for='"+name+"_"+value+"'>"+label+"</label>\n<input type='radio' value='"+value+"' $"+name+"_"+value+" disabled>\n"
            str+="\t\t\t\"; ?>\n"        
            str+="\t\t\t</div>\n"
    str+="    </div>\n\n    <script>\n    //this will display or hide the report and change what the button says\n    //it uses the button\'s id to determine which report to toggle\n    function toggleReport(theId) {\n        thisReport = document.getElementById(theId + \"_report\");\n        thisButton = document.getElementById(theId);\n        if (thisReport.style.display === \"none\") {\n            thisReport.style.display = \"unset\";\n            thisButton.innerHTML = \"Hide Report\";\n        } else {\n            thisReport.style.display = \"none\";\n            thisButton.innerHTML = \"Show Report\";\n        }\n    }\n\n    //this will display or hide the table and change what the button says\n    //it uses the button\'s id to determine which report to toggle\n    function toggleTable(theId) {\n        populateTable(theId);\n        let thisTable = document.getElementById(theId + \"_table\");\n        let thisButton = document.getElementById(theId);\n        if (thisTable.style.display === \"none\") {\n            thisTable.style.display = \"unset\";\n            thisButton.innerHTML = \"Hide Table\";\n        } else {\n            thisTable.style.display = \"none\";\n            thisButton.innerHTML = \"Show Table\";\n        }\n    }\n\n    //when called populates the contents of the div containing the table\n    //it checks the id of the button pressed to determine which table on the \n    //page to populate\n    function populateTable(theId) {\n        let thisTableInnerDiv = document.getElementById(theId + \"_table_inner_div\");\n        if (thisTableInnerDiv.innerText.trim() === \"\") {\n            let fields = Object.keys(tableContents[0]);\n            //    Here you could opt to show field names instead of manually setting below\n            str = \"<table>\";\n            str += \"<tr>\";\n            for (let i = 0; i < fields.length; i++) {\n                str += \"<th>\" + fields[i] + \"</th>\";\n            }\n            str += \"</tr>\";\n            for (let i = 0; i < tableContents.length; i++) {\n                str += \"<tr>\";\n                for (let j = 0; j < fields.length; j++) {\n                    str += \"<td>\" + tableContents[i][fields[j]] + \"</td>\";\n                }\n                str += \"</tr>\";\n            }\n            str += \"</table>\";\n            //str = JSON.stringify(tableContents);\n            thisTableInnerDiv.innerHTML = str;\n        }\n    }\n\n    //it uses then id of the start date or end date filter to determine which table to change\n    function changeTable() {\n        let reportTableBaseName = \"\";\n        if (this.id.includes(\"_start_filter_value\")) {\n            reportTableBaseName = this.id.split(\"_start_filter_value\")[0];\n        } else if (this.id.includes(\"_end_filter_value\")) {\n            reportTableBaseName = this.id.split(\"_end_filter_value\")[0];\n        }\n        let thisStartFilterValue = document.getElementById(reportTableBaseName + \"_start_filter_value\").value.trim();\n        let thisEndFilterValue = document.getElementById(reportTableBaseName + \"_end_filter_value\").value.trim();\n        //four cases,   start \"\",           end \"\"              make no comparisons, show all  OO\n        //              start something,    end \"\"              check only start               XO\n        //              start \"\",           end something       check only end                 OX\n        //              start something,    end something       check start and end            XX\n        let thisTableInnerDiv = document.getElementById(reportTableBaseName + \"_table_button_table_inner_div\");\n\n        let tableString = \"\";\n\n        let fields = Object.keys(tableContents[0]);\n        //    Here you could opt to show field names instead of manually setting below\n        tableString = \"<table>\";\n        tableString += \"<tr>\";\n        for (let i = 0; i < fields.length; i++) {\n            tableString += \"<th>\" + fields[i] + \"</th>\";\n        }\n        tableString += \"</tr>\";\n        for (let i = 0; i < tableContents.length; i++) {\n            if ((thisStartFilterValue === \"\") && (thisEndFilterValue === \"\")) { //OO\n                tableString += \"<tr>\";\n                for (let j = 0; j < fields.length; j++) {\n                    tableString += \"<td>\" + tableContents[i][fields[j]] + \"</td>\";\n                }\n                tableString += \"</tr>\";\n            } else if ((thisStartFilterValue != \"\") && (thisEndFilterValue === \"\")) { //XO\n                if (tableContents[i][orderByVariable] >= thisStartFilterValue) {\n                    tableString += \"<tr>\";\n                    for (let j = 0; j < fields.length; j++) {\n                        tableString += \"<td>\" + tableContents[i][fields[j]] + \"</td>\";\n                    }\n                    tableString += \"</tr>\";\n                }\n            } else if ((thisStartFilterValue === \"\") && (thisEndFilterValue != \"\")) { //OX\n                if (tableContents[i][orderByVariable] <= thisEndFilterValue) {\n                    tableString += \"<tr>\";\n                    for (let j = 0; j < fields.length; j++) {\n                        tableString += \"<td>\" + tableContents[i][fields[j]] + \"</td>\";\n                    }\n                    tableString += \"</tr>\";\n                }\n            } else if ((thisStartFilterValue != \"\") && (thisEndFilterValue != \"\")) { //XX\n                if ((tableContents[i][orderByVariable] >= thisStartFilterValue) && (tableContents[i][orderByVariable] <=\n                        thisEndFilterValue)) {\n                    tableString += \"<tr>\";\n                    for (let j = 0; j < fields.length; j++) {\n                        tableString += \"<td>\" + tableContents[i][fields[j]] + \"</td>\";\n                    }\n                    tableString += \"</tr>\";\n                }\n            }\n        }\n        tableString+=\"</table>\";\n        thisTableInnerDiv.innerHTML = tableString;\n    }\n    </script>\n</div>\n\n<?php\n\n//This SQL query gets all results for this patient, not just the current encouter.\n\n////////////////////////////////////////////GENERATE/////////////////////////////////////\n"
    str+="$result = sqlStatement(\"SELECT * FROM $table_name WHERE pid=$pid "+orderByStatement+" "+order+";\");\n"
    str+="$orderByVariable = \'"+orderByField+"\';\n"
    str+="$orderByType = '"+orderByType+"';\n"
    str+="$fieldNamesArray = array("

    showInTable = ""
    for i in range(len(data["inputs"])):
        try:
            showInTable = data["inputs"][i]["properties"]["showInTable"]
        except:
            showInTable = "false"
        if showInTable.lower() == "true" or data["inputs"][i]["properties"]["name"] == orderByField:
            str+="'"+data["inputs"][i]["properties"]["name"]+"',"
    str = str.rstrip(",")
    str+= ");\n"
    str+="\n\n//////////////////////////////////////////////////////////////////////////////////////////\n$numberOfFields = count($fieldNamesArray);\n\n$showTableButtonAndCSVButton = \"\";\nif ($numberOfFields<=0){\n    $showTableButtonAndCSVButton =\" style=\'display:none;\' \";;\n}\n\necho \"<script>orderByVariable=\'$orderByVariable\';</script>\";  //using non-strict mode declaration of object\n//$result_set = array(); //all results from sql query, just in case this is needed in the future\n$table_data = array(); //just the field results we need for building the table\n\n$row_count = 0;\n\necho \"<script>\n\ttableContents=[];\n\t</script>\";\n\n$fieldCount = count($fieldNamesArray);\n\nwhile ($row = sqlFetchArray($result)) { //using api function given in the program\n\t//$result_set[] = $row;\n\n    for ($i = 0; $i < $fieldCount; $i++) {\n        $table_data[$row_count][$fieldNamesArray[$i]] = $row[$fieldNamesArray[$i]];;\n    }\n    \n    $row_count = $row_count + 1;\n}\n\n//make a json string from the table data and echo this into javascript to\n//be used dynamically on the page\n$jsonTableDataString = json_encode($table_data);\necho \"<script>tableContents=$jsonTableDataString;</script>\";  //using non-strict mode declaration of object\n?>\n\n<script>\n//This function takes the current table turns it into csv\n//(convention is double quote all data, no trailing spaces, one \\n newline per data line)\n\n//Uses the id of the button clicked to determine which table to convert to csv \nfunction convertTableToCSV(theId) {\n    let str = \"\";\n    let fields = [];\n    //figuring out which button clicked\n    let reportTableBaseName = theId.split(\"_csv_button\")[0];\n    let thisStartFilterValue = document.getElementById(reportTableBaseName + \"_start_filter_value\").value.trim();\n    let thisEndFilterValue = document.getElementById(reportTableBaseName + \"_end_filter_value\").value.trim();\n\n    //four cases,   start \"\",           end \"\"              make no comparisons, show all  OO\n    //              start something,    end \"\"              check only start               XO\n    //              start \"\",           end something       check only end                 OX\n    //              start something,    end something       check start and end            XX\n\n    if (tableContents.length > 0) { //only if there is at least one line to put in table\n        let fields = Object.keys(tableContents[0]);\n        //    Here you could opt to show field names instead of manually setting below\n        for (let i = 0; i < fields.length; i++) {\n            str += \"\\\"\";\n            str += fields[i];\n            str += \"\\\",\";\n        }\n        str = str.substr(0, str.length - 1);\n        str += \"\\n\";\n\n        //build the table\n\n        for (let i = 0; i < tableContents.length; i++) {\n            if ((thisStartFilterValue === \"\") && (thisEndFilterValue === \"\")) { //OO\n                for (let field in tableContents[i]) {\n                    str += \"\\\"\";\n                    str += tableContents[i][field];\n                    str += \"\\\",\";\n                }\n                str = str.substr(0, str.length - 1);\n                str += \"\\n\";\n            } else if ((thisStartFilterValue != \"\") && (thisEndFilterValue === \"\")) { //XO\n                if (tableContents[i][orderByVariable] >= thisStartFilterValue) {\n                    for (let field in tableContents[i]) {\n                        str += \"\\\"\";\n                        str += tableContents[i][field];\n                        str += \"\\\",\";\n                    }\n                    str = str.substr(0, str.length - 1);\n                    str += \"\\n\";\n                }\n            } else if ((thisStartFilterValue === \"\") && (thisEndFilterValue != \"\")) { //OX\n                if (tableContents[i][orderByVariable] <= thisEndFilterValue) {\n                    for (let field in tableContents[i]) {\n                        str += \"\\\"\";\n                        str += tableContents[i][field];\n                        str += \"\\\",\";\n                    }\n                    str = str.substr(0, str.length - 1);\n                    str += \"\\n\";\n                }\n            } else if ((thisStartFilterValue != \"\") && (thisEndFilterValue != \"\")) { //XX\n                if ((tableContents[i][orderByVariable] >= thisStartFilterValue) && (tableContents[i][orderByVariable] <=\n                        thisEndFilterValue)) {\n                    for (let field in tableContents[i]) {\n                        str += \"\\\"\";\n                        str += tableContents[i][field];\n                        str += \"\\\",\";\n                    }\n                    str = str.substr(0, str.length - 1);\n                    str += \"\\n\";\n                }\n            }\n        }\n    }\n    console.log(\"Here are the csv contents you requested:\");\n    console.log(\"---------------------------------------\");\n    console.log(str);\n    console.log();\n    if (str.trim() != \"\") { //don\'t offer to save an empty string\n        saveStringToTextFile(str);\n    }\n}\n\n//general function to saves a string to a file, only using first argument in this program currently\nfunction saveStringToTextFile(str1, fileName = \"myCSVFile\", fileType = \".csv\", addDate = false) {\n    let saveFileName = fileName;\n    let dateString = \'\';\n\n    if (addDate === true) {\n        //make a string representing the date to add on to the filename\n        dateString = (new Date()).toLocaleString();\n        dateString = \"_\" + dateString.replaceAll(\"/\", \"_\").replaceAll(\",\", \"_\").replaceAll(\" \", \"_\").replaceAll(\":\",\n            \"_\");\n    }\n\n    saveFileName = fileName + dateString + fileType;\n\n    //place data in blob and use to make a file for download\n    let blobVersionOfText = new Blob([str1], {\n        type: \"text/plain\"\n    });\n    let urlToBlob = window.URL.createObjectURL(blobVersionOfText);\n    let downloadLink = document.createElement(\"a\");\n    downloadLink.style.display = \"none\";\n    downloadLink.download = saveFileName;\n    downloadLink.href = urlToBlob;\n    document.body.appendChild(downloadLink);\n    downloadLink.click();\n    downloadLink.parentElement.removeChild(downloadLink);\n}\n</script>\n\n\n<!-- Here is the div for the table data contents -->\n<div id=\"<?php echo $uniqueReportId . \'_table_button_table\'; ?>\" style=\"display:none;\">\n    <div class=\'general report-table\' id=\"<?php echo $uniqueReportId . \'_table_button_table_inner_div\'; ?>\"></div>\n\n    <?php\n$showOrderInputs = \"\";\nif ($orderByVariable===\"\"){\n    $showOrderInputs=\" style=\'display:none;\' \";\n} \n?>\n\n    <div class=\'general\' <?php echo $showOrderInputs;?>>\n        <label for=\"<?php echo $uniqueReportId . \'_start_filter_value\'; ?>\">Start:</label>\n        <input type=\'<?php echo $orderByType;?>\' id=\"<?php echo $uniqueReportId . \'_start_filter_value\'; ?>\">\n        <label for=\"<?php echo $uniqueReportId . \'_end_filter_value\'; ?>\">End:</label>\n        <input type=\'<?php echo $orderByType;?>\' id=\"<?php echo $uniqueReportId . \'_end_filter_value\'; ?>\">\n    </div>\n\n\n</div>\n\n<!-- Buttons for toggling report, toggling table and csv -->\n<div>\n    <button id=\'<?php echo $uniqueReportId ?>\' onclick=\"toggleReport(this.id)\">Show Report</button>\n    <button id=\'<?php echo $uniqueReportId . \"_table_button\" ;?>\' <?php echo $showTableButtonAndCSVButton;?>\n        onclick=\"toggleTable(this.id);populateTable(this.id);\">Show Table</button>\n    <button id=\'<?php echo $uniqueReportId . \"_csv_button\";?>\' <?php echo $showTableButtonAndCSVButton;?>\n        onclick=\"{convertTableToCSV(this.id);}\">Download\n        CSV</button>\n</div>\n\n<!-- Add event listeners to the tables start date and end date to call the changeTable function and repopulate the table -->\n<script>\ndocument.getElementById(\"<?php echo $uniqueReportId . \'_start_filter_value\'; ?>\").addEventListener(\'change\',\n    changeTable);\ndocument.getElementById(\"<?php echo $uniqueReportId . \'_end_filter_value\'; ?>\").addEventListener(\'change\', changeTable);\n</script>\n"

    outfile = open(form_folder+"/reportinclude.php","w")
    outfile.write(str)
    outfile.close()

def make_reportincludephp(data):
    form_name = data["formName"]
    form_folder = data["folderName"]
    table_name = "form_" + form_folder

    str="<?php\n$printableId = $table_name . \'printable\' . $id;\n$record = formFetch($table_name, $id);\n?>\n<?php echo \"<style>\"; include_once(\"style.css\"); echo \"</style>\";?>\n<div id=\"<?php echo $printableId . \'_report\'; ?>\" style=\"display:none;\">\n<?php\n"

    #check all records to see if they are datetimepicker if so change
    for i in range(len(data["inputs"])):
        inputType = data["inputs"][i]["type"]
        name = data["inputs"][i]["properties"]["name"]
        if inputType == "datetimepicker":
            str+="if ($record['"+name+"'] != '') {\n"
            str+="\t$dateparts = explode(' ', $record['"+name+"']);\n"
            str+="\t$record['"+name+"'] = $dateparts[0];\n}\n\n"

      #loop through variables 
    for i in range(len(data["inputs"])):
        inputType = data["inputs"][i]["type"]
        name = data["inputs"][i]["properties"]["name"]

        if inputType == "text":
            str+="\t\t$" + name + " = attr($record['"+name+"']);\n"
        elif inputType == "date":
            str+="\t\t$" + name + " = attr($record['"+name+"']);\n"
        elif inputType == "time":
            str+="\t\t$" + name + " = attr($record['"+name+"']);\n" ###########################
        elif inputType == "checkbox":
            str+="\t\t$" + name + " = attr($record['"+name+"']);\n"
        elif inputType == "integer":
            str+="\t\t$" + name + " = attr($record['"+name+"']);\n"
        elif inputType == "float":
            str+="\t\t$" + name + " = attr($record['"+name+"']);\n"
        elif inputType == "textarea":
            str+="\t\t$" + name + " = attr($record['"+name+"']);\n"
        elif inputType == "datetimepicker":
            str+="\t\t$" + name + " = attr($record['"+name+"']);\n"
        elif inputType == "radio":
            str+="\t\t$" + name + " = $record['"+name+"'];\n"
            buttons = data["inputs"][i]["properties"]["buttons"]
            for j in range(len(buttons)):
                value = buttons[j]['value']
                str+="\t\t($"+name+" == '"+value+"') ? ($"+name+"_"+value+" = 'CHECKED') : ($"+name+"_"+value+" = '');\n"
    str+="?>\n    <!-- container for the main body of the form -->\n\n    <div class=\"general\">\n"
    str+="<!-- ----------GENERATE---------------- -->\n"
    for i in range(len(data["inputs"])):
        inputType = data["inputs"][i]["type"]
        name = data["inputs"][i]["properties"]["name"]
        label = data["inputs"][i]["properties"]["label"]
        if inputType!="checkbox":
            str+="\t\t\t<div>\n"
            str+="\t\t\t\t<label for='"+name+"'>"+label+"</label>\n"
            str+="\t\t\t</div>\n"
        if inputType == "text":
            str+="\t\t\t<div>\n"
            str+="\t\t\t<?php echo \"\n"
            str+="\t\t\t\t<input type='text' value='$"+name+"' disabled>\n"
            str+="\t\t\t\"; ?>\n"
            str+="\t\t\t</div>\n"
        elif inputType == "date":
            str+="\t\t\t<div>\n"
            str+="\t\t\t<?php echo \"\n"
            str+="\t\t\t\t<input type='date' value='$"+name+"' disabled>\n"
            str+="\t\t\t\"; ?>\n"
            str+="\t\t\t</div>\n"
        elif inputType == "time":
            str+="\t\t\t<div>\n"
            str+="\t\t\t<?php echo\"\n"
            str+="\t\t\t\t<input type='time' value='$"+name+"' disabled>\n"
            str+="\t\t\t\"; ?>\n"
            str+="\t\t\t</div>\n"
        elif inputType == "checkbox":
            try:
                value = data["inputs"][i]["properties"]["value"]
            except:
                value = "on"
            str+="\t\t\t<div>\n"
            #str+="\t\t\t<?php echo\"\n"
            str+="<label for='"+name+"'>"+label+"</label>"
            str+="\t\t\t\t<input type='checkbox' <?php echo ($"+name+" == '"+value+"') ? 'checked' : ''; ?> disabled>\n"
            #str+="\t\t\t\"; ?>\n"
            str+="\t\t\t</div>\n"
        elif inputType == "integer":
            str+="\t\t\t<div>\n"
            str+="\t\t\t<?php echo\"\n"
            str+="\t\t\t\t<input type='number' value='$"+name+"' disabled>\n"
            str+="\t\t\t\"; ?>\n"
            str+="\t\t\t</div>\n"
        elif inputType == "float":
            str+="\t\t\t<div>\n"
            str+="\t\t\t<?php echo\"\n"
            str+="\t\t\t\t<input type='number' value='$"+name+"' disabled>\n"
            str+="\t\t\t\"; ?>\n"
            str+="\t\t\t</div>\n"
        elif inputType == "textarea":
            str+="\t\t\t<div>\n"
            str+="\t\t\t\t<?php echo \"\n"
            str+="\t\t\t\t<textarea disabled>$"+name+"</textarea>\n"
            str+="\t\t\t\t\"; ?>\n"
            str+="\t\t\t</div>\n"
        elif inputType == "datetimepicker":
            str+="\t\t\t<div>\n"
            str+="\t\t\t\t<?php\n"
            str+="\t\t\t\techo \"<input type='text' class='datepicker' value='\" . $"+name+" . \"' title='\" . xla('yyyy-mm-dd') . \"' disabled>\"\n"
            str+="\t\t\t\t?>\n"                    
            str+="\t\t\t</div>\n"
        elif inputType == "radio":
            str+="\t\t\t<div>\n"
            str+="\t\t\t<?php echo \"\n"
            buttons = data["inputs"][i]["properties"]["buttons"]
            for j in range(len(buttons)):
                value = buttons[j]['value']
                label = buttons[j]['label']
                str+="\t\t\t\t<label for='"+name+"_"+value+"'>"+label+"</label>\n<input type='radio' value='"+value+"' $"+name+"_"+value+" disabled>\n"
            str+="\t\t\t\"; ?>\n"        
            str+="\t\t\t</div>\n"
    str+="    </div>\n\n    <script>\n    function toggleReport(theId) {\n        thisReport = document.getElementById(theId + \"_report\");\n        thisButton = document.getElementById(theId);\n        if (thisReport.style.display === \"none\") {\n            thisReport.style.display = \"unset\";\n            thisButton.innerHTML = \"Hide Report\";\n        } else {\n            thisReport.style.display = \"none\";\n            thisButton.innerHTML = \"Show Report\";\n        }\n    }\n\n    function openReport(theId) {\n        thisReport = document.getElementById(theId + \"_report\");\n        thisButton = document.getElementById(theId);\n        thisButton.innerHTML = \"Hide Report\";\n        thisReport.style.display = \"unset\";\n    }\n\n    function printReport(theId) {\n        var divContents = document.getElementById(theId + \"_report\").innerHTML;\n        var a = window.open(\'\', \'_blank\');\n        a.document.write(\'<html><head><title></title><style>*{font-size:0.8rem;}</style></head><body>\');\n        a.document.write(divContents);\n        a.document.write(\'</body></html>\');\n        a.document.close();\n        a.print();\n        a.close();\n    }\n    </script>\n</div>\n<div>\n    <button id=\'<?php echo $printableId ?>\' onclick=\"toggleReport(this.id)\">Show Report</button>\n    <button onclick=\"{openReport(\'<?php echo $printableId ?>\');printReport(\'<?php echo $printableId ?>\');}\">Print\n        Report</button>\n</div>\n"

    outfile = open(form_folder+"/reportinclude.php","w")
    outfile.write(str)
    outfile.close()

            
def make_printphp(data):
    form_name = data["formName"]
    form_folder = data["folderName"]
    table_name = "form_" + form_folder

    str="<?php\n\nrequire_once(\"../../globals.php\");\nrequire_once(\"$srcdir/api.inc\");\n\nuse OpenEMR\\Common\\Csrf\\CsrfUtils;\nuse OpenEMR\\Core\\Header;\n\nfunction display_array($your_array)\n{\n    foreach ($your_array as $key => $value) {\n        if (is_array($value)) {\n            display_array($value);\n        } else {\n            echo \"Key:$key ------- Value:$value<br>\\n\";\n        }\n    }\n}\n\n// -------GENERATE-------\n"
    
    str+="$table_name = '"+table_name+"';\n"
    str+="$form_name = '"+form_name+"';\n"
    str+="$form_folder = '"+form_folder+"';\n"
    
    str+="// -------GENERATE-------\n\nformHeader(\"Form: \" . $form_name);\n$returnurl = \'encounter_top.php\';\n\n/* load the saved record */\n$record = formFetch($table_name, $_GET[\"id\"]);\n\n?>\n\n<html>\n\n<head>\n    <?php Header::setupHeader(); ?>\n    <link rel=\"stylesheet\" href=\"../../forms/<?php echo $form_folder; ?>/style.css\">\n</head>\n\n<body class=\"body_top\">\n    <div>\n        Printed on <?php echo date(\"F d, Y\", time()); ?>\n    </div>\n    <div>\n        <?php\n        include_once(\'localFunctions.php\');\n        display_array($record);\n        ?>\n    </div>\n</body>\n\n<script>\n    window.print();\n    //window.close();\n</script>\n\n</html>\n"
    
    outfile = open(form_folder+"/print.php","w")
    outfile.write(str)
    outfile.close()

def make_reportphpold(data):
    form_folder = data["folderName"]
    str="<?php\n\nrequire_once(\"../../globals.php\");\nrequire_once($GLOBALS[\"srcdir\"] . \"/api.inc\");\n// -------GENERATE-------\n"
    str+="\tfunction "+form_folder+"_report($pid, $encounter, $cols, $id){\n"
    str+="$table_name = 'form_"+form_folder+"';\n"
    str+="// -------GENERATE-------\n\n    $count = 0;\n    $data = formFetch($table_name, $id);\n\n    if ($data) {\n        print \"<table><tr>\";\n\n        foreach ($data as $key => $value) {\n            if (\n                $key == \"id\" || $key == \"pid\" || $key == \"user\" ||\n                $key == \"groupname\" || $key == \"authorized\" ||\n                $key == \"activity\" || $key == \"date\" ||\n                $value == \"\" || $value == \"0000-00-00 00:00:00\" ||\n                $value == \"n\"\n            ) {\n                // skip certain fields and blank data\n                continue;\n            }\n\n            $key = ucwords(str_replace(\"_\", \" \", $key));\n            print(\"<tr>\\n\");\n            print(\"<tr>\\n\");\n            print \"<td><span class=bold>\" . text($key) . \": </span><span class=text>\" . text($value) . \"</span></td>\";\n            $count++;\n            if ($count == $cols) {\n                $count = 0;\n                print \"</tr><tr>\\n\";\n            }\n        }\n    }\n\n    print \"</tr></table>\";\n}\n\n"
    outfile = open(form_folder+"/report.php","w")
    outfile.write(str)
    outfile.close()

def make_reportphp(data):
    form_folder = data["folderName"]
    str="<?php\n\nrequire_once(\"../../globals.php\");\nrequire_once($GLOBALS[\"srcdir\"] . \"/api.inc\");\n\nfunction "+form_folder+"_report($pid, $encounter, $cols, $id)\n{\n    $table_name = \"form_"+form_folder+"\";\n  $form_folder = \""+form_folder+"\";\n  include(\"reportinclude.php\");\n}\n"
    outfile = open(form_folder+"/report.php","w")
    outfile.write(str)
    outfile.close()


    
def make_sql(data):
    table_name = "form_" + data["folderName"]
    
    str="CREATE TABLE IF NOT EXISTS `"+table_name+"` (\n"
    str+="    /* these fields are common to all forms and should remain intact */\n    id bigint(20) NOT NULL auto_increment,\n    date datetime default NULL,\n    pid bigint(20) default NULL,\n    user varchar(255) default NULL,\n    groupname varchar(255) default NULL,\n    authorized tinyint(4) default NULL,\n    activity tinyint(4) default NULL,\n\n    /* these fields are customized to this form */\n"
    
    for i in range(len(data["inputs"])):
        inputType = data["inputs"][i]["type"]
        name = data["inputs"][i]["properties"]["name"]
        if inputType == "text":
            str+= "\t" + name + " varchar(255),\n"
        elif inputType == "date":
            str+= "\t" + name + " date,\n"
        elif inputType == "time":
            str+= "\t" + name + " varchar(255),\n"
        elif inputType == "checkbox":
            str+= "\t" + name + " varchar(255),\n"
        elif inputType == "integer":
            str+= "\t" + name + " int,\n"
        elif inputType == "float":
            str+= "\t" + name + " float,\n"
        elif inputType == "textarea":
            str+= "\t" + name + " longtext,\n"
        elif inputType == "datetimepicker":
            str+= "\t" + name + " datetime default NULL,\n"
        elif inputType == "radio":
            str+= "\t" + name + " varchar(255),\n"
        
    str+="    /* end of custom form fields */\n\n    PRIMARY KEY (id)\n) ENGINE=InnoDB;\n"
    
    outfile = open(data["folderName"]+"/table.sql","w")
    outfile.write(str)
    outfile.close()

def make_savephp(data):
    form_name = data["formName"]
    form_folder = data["folderName"]
    table_name = "form_" + form_folder
    str="<?php\n\n/*\n * This saves the submitted form\n */\n/**\n * example2 save.php\n *\n * @package   OpenEMR\n * @link      http://www.open-emr.org\n * @author    Brady Miller <brady.g.miller@gmail.com>\n * @copyright Copyright (c) 2018 Brady Miller <brady.g.miller@gmail.com>\n * @license   https://github.com/openemr/openemr/blob/master/LICENSE GNU General Public License 3\n */\n\nrequire_once(\"../../globals.php\");\nrequire_once(\"$srcdir/api.inc\");\nrequire_once(\"$srcdir/forms.inc\");\n\nuse OpenEMR\\Common\\Csrf\\CsrfUtils;\n\nif (!CsrfUtils::verifyCsrfToken($_POST[\"csrf_token_form\"])) {\n    CsrfUtils::csrfNotVerified();\n}\n\n// -------GENERATE-------\n"
    str+="$table_name = '"+table_name+"';\n"
    str+="$form_name = '"+form_name+"';\n"
    str+="$form_folder = '"+form_folder+"';\n"

    for i in range(len(data["inputs"])):
         inputType = data["inputs"][i]["type"]
         name = data["inputs"][i]["properties"]["name"]
         if inputType == "checkbox":
             str+="if(!isset($_POST['"+name+"'])){$_POST['"+name+"']='';}\n"


    str+="// -------GENERATE-------\n\nif ($encounter == \"\") {\n    $encounter = date(\"Ymd\");\n}\n\nif ($_GET[\"mode\"] == \"new\") {\n    /* NOTE - for customization you can replace $_POST with your own array\n     * of key=>value pairs where \'key\' is the table field name and\n     * \'value\' is whatever it should be set to\n     * ex)   $newrecord[\'parent_sig\'] = $_POST[\'sig\'];\n     *       $newid = formSubmit($table_name, $newrecord, $_GET[\"id\"], $userauthorized);\n     */\n\n    /* save the data into the form\'s own table */\n    $newid = formSubmit($table_name, $_POST, $_GET[\"id\"], $userauthorized);\n\n    /* link the form to the encounter in the \'forms\' table */\n    addForm($encounter, $form_name, $newid, $form_folder, $pid, $userauthorized);\n} elseif ($_GET[\"mode\"] == \"update\") {\n    /* update existing record */\n    $success = formUpdate($table_name, $_POST, $_GET[\"id\"], $userauthorized);\n"
    
    #build checkbox updates here

    # for i in range(len(data["inputs"])):
    #     inputType = data["inputs"][i]["type"]
    #     name = data["inputs"][i]["properties"]["name"]
    #     if inputType == "checkbox":
    #         str+="\tsqlStatement(\"UPDATE $table_name set pid = ?, "+name+"=? WHERE id=?\",\n"
    #         str+="\t\t[$_SESSION[\'pid\'],($_POST[\'"+name+"\'] ?? null),$_GET[\'id\']]);\n"

     #   sqlStatement(\"UPDATE $table_name set pid = ?, fever=? WHERE id=?\",
     #   $_SESSION[\'pid\'],($_POST[\'fever\'] ?? null),$_GET[\'id\']]);\n


    str+="}\n\nformHeader(\"Redirecting....\");\nformJump();\nformFooter();\n\n"
    outfile = open(form_folder+"/save.php","w")
    outfile.write(str)
    outfile.close()

def make_info(data):
    form_name = data["formName"]
    form_folder = data["folderName"]
    str=form_name + "\n"
    outfile = open(form_folder+"/info.txt","w")
    outfile.write(str)
    outfile.close()

def make_css(data):
    form_folder = data["folderName"]
    try:
        width = data["width"]
    except:
        width = "400px"
    str="* {\n    box-sizing: border-box;\n    font-size: 1em;\n}\n\ninput[type=time],\ninput[type=number],\ninput[type=text],\ntextarea {\n    width: 375px;\n    background-color: white;\n    border: 1px solid grey;\n}\n\n.report-table table,\n.report-table tr,\n.report-table th,\n.report-table td {\n    border: 1px solid black;\n    padding: 5px;\n    background-color: rgb(250, 250, 223);\n}\n\ndiv.center-div {\n    display: block;\n    text-align: center;\n}\n\n.general {\n "+"width: " + width + ";   \n    padding: 10px;\n    margin: 10px;\n    border: 1px solid grey;\n    background-color: #ffc;\n}\n\n.center-me {\n    text-align: center;\n}\n\ninput[type=radio] {\n    margin-right: 1em;\n}\n\nlabel {\n    margin-top: 0.5rem;\n    margin-bottom: 1rem;\n}\n\nhr {\n    border: 1px solid black;\n}\n\ninput[type=button],\nbutton {\n    padding: .25rem .5rem;\n    font-size: .765625rem;\n    line-height: 1.5;\n    border-radius: .2rem;\n    color: #fff;\n    background-color: #007bff;\n    border-color: #007bff;\n}\n\n"
    outfile = open(form_folder+"/style.css","w")
    outfile.write(str)
    outfile.close()

def make_inputBackup(data):
    form_folder = data["folderName"]
    infile = open('input.json','r')
    fileContents = infile.read() 
    infile.close()
    outfile = open(form_folder+"/input.json","w")
    outfile.write(fileContents)
    outfile.close()

make_folder(data)
make_newphp(data)
make_viewphp(data)
make_reportphp(data)
make_reportincludewithtablephp(data)
#make_reportincludephp(data)
#make_printphp(data)
make_savephp(data)
make_info(data)
make_sql(data)
make_css(data)
make_inputBackup(data)
