CREATE TABLE IF NOT EXISTS `form_testForm` (
    /* these fields are common to all forms and should remain intact */
    id bigint(20) NOT NULL auto_increment,
    date datetime default NULL,
    pid bigint(20) default NULL,
    user varchar(255) default NULL,
    groupname varchar(255) default NULL,
    authorized tinyint(4) default NULL,
    activity tinyint(4) default NULL,

    /* these fields are customized to this form */
	myText varchar(255),
	myTime varchar(255),
	myInteger int,
	myFloat float,
	myCheckbox varchar(255),
	myTextarea longtext,
	myRadio varchar(255),
	myDate date,
    /* end of custom form fields */

    PRIMARY KEY (id)
) ENGINE=InnoDB;
