class Config():

	config_object = {
		"cli_arguments": {
				"adddependencies": "-p \"[PROJECT_FOLDER]\" -all",
				"deploy": "-np -p \"[PROJECT_FOLDER]\"",
				"importbundle": "",
				"importfiles": "-p \"[PROJECT_FOLDER]\"",
				"importobjects": "-p \"[PROJECT_FOLDER]\"",
				"listbundles": "",
				"listfiles": "-folder \"/SuiteScripts\"",
				"listmissingdependencies": "-p \"[PROJECT_FOLDER]\"",
				"listobjects": "-p \"[PROJECT_FOLDER]\"",
				"preview": "-p \"[PROJECT_FOLDER]\"",
				"update": "-p \"[PROJECT_FOLDER]\"",
				"updatecustomrecordwithinstances": "-p \"[PROJECT_FOLDER]\"",
				"validate": "-p \"[PROJECT_FOLDER]\" -server"
		},
		"custom_objects": [
			[
				"Bundle Installation Script",
				"bundleinstallationscript",
				"/Objects/BundleInstallation",
				"customscript"
			],
			[
				"Centers",
				"center",
				"/Objects/CentersAndTabs/Centers",
				"custcenter"
			],
			[
				"Center Categories",
				"centercategory",
				"/Objects/CentersAndTabs/Categories",
				"custcentercategory"
			],
			[
				"Center Tabs",
				"centertab",
				"/Objects/CentersAndTabs/Tab",
				"custcentertab"
			],
			[
				"Client Scripts",
				"clientscript",
				"/Objects/Scripts/Client",
				"customscript"
			],
			[
				"CRM Custom Fields",
				"crmcustomfield",
				"/Objects/Fields/CRM",
				"custevent"
			],
			[
				"Custom Plugins",
				"customglplugin",
				"/Objects/Plugins/Custom",
				"customscript"
			],
			[
				"Custom Lists",
				"customlist",
				"/Objects/Lists",
				"customlist"
			],
			[
				"Custom Records",
				"customrecordtype",
				"/Objects/Records",
				"customrecord"
			],
			[
				"Email Capture Plugins",
				"emailcaptureplugin",
				"/Objects/Plugins/Email",
				"customscript"
			],
			[
				"Entity Custom Fields",
				"entitycustomfield",
				"/Objects/Fields/Entity",
				"custentity"
			],
			[
				"Entity Forms",
				"entryForm",
				"/Objects/Forms/EntryForm",
				"custform"
			],
			[
				"Transaction Forms",
				"transactionForm",
				"/Objects/Forms/TransactionForm",
				"custform"
			],
			[
				"Item Custom Fields",
				"itemcustomfield",
				"/Objects/Fields/Item",
				"custitem"
			],
			[
				"Item Number Custom Fields",
				"itemnumbercustomfield",
				"/Objects/Fields/ItemNumber",
				"custitem"
			],
			[
				"Item Option Custom Fields",
				"itemoptioncustomfield",
				"/Objects/Fields/ItemOption",
				"custitemoption"
			],
			[
				"Map Reduce Script",
				"mapreducescript",
				"/Objects/Scripts/MapReduce",
				"customscript"
			],
			[
				"Mass Update Script",
				"massupdatescript",
				"/Objects/Scripts/MassUpdate",
				"customscript"
			],
			[
				"Other Custom Field",
				"othercustomfield",
				"/Objects/Fields/Other",
				"custrecord"
			],
			[
				"Portlets",
				"portlet",
				"/Objects/Scripts/Portlet",
				"customscript"
			],
			[
				"Promotions Plugins",
				"promotionsplugin",
				"/Objects/Plugins/Promotions",
				"customscript"
			],
			[
				"Restlets",
				"restlet",
				"/Objects/Scripts/Restlet",
				"customscript"
			],
			[
				"Roles",
				"role",
				"/Objects/Roles",
				"customrole"
			],
			[
				"Saved Searches",
				"savedsearch",
				"/Objects/SavedSearches",
				"customsearch"
			],
			[
				"Scheduled Scripts",
				"scheduledscript",
				"/Objects/Scripts/Scheduled",
				"customscript"
			],
			[
				"Sub Tabs",
				"subtab",
				"/Objects/CentersAndTabs/SubTab",
				"custtab"
			],
			[
				"Suitelet",
				"suitelet",
				"/Objects/Scripts/Suitelet",
				"customscript"
			],
			[
				"Transaction Body Custom Field",
				"transactionbodycustomfield",
				"/Objects/Fields/TransactionBody",
				"transactionbodycustomfield"
			],
			[
				"Transaction Column Custom Field",
				"transactioncolumncustomfield",
				"/Objects/Fields/TransactionColumn",
				"custcol"
			],
			[
				"User Event Script",
				"usereventscript",
				"/Objects/Scripts/UserEvent",
				"customscript"
			],
			[
				"Workflows",
				"workflow",
				"/Objects/Workflows",
				"customworkflow"
			],
			[
				"Workflow Action Scripts",
				"workflowactionscript",
				"/Objects/Scripts/WorkflowAction",
				"customscript"
			]
		],
		"cli_commands": [
			[
				"Add Dependencies to Manifest",
				"Adds missing dependencies to the manifest file.",
				"adddependencies"
			],
			[
				"Deploy to Account",
				"Deploys the folder or zip file that contains the SuiteCloud project.",
				"deploy"
			],
			[
				"Import Bundle",
				"Imports a customization bundle from your NetSuite account and\nconverts it to an account customization project.",
				"importbundle"
			],
			[
				"Import Files",
				"Imports files from your NetSuite account to the account customization project.",
				"importfiles"
			],
			[
				"Import Objects",
				"Imports custom objects from your NetSuite account to the SuiteCloud project.",
				"importobjects"
			],
			[
				"List Bundles",
				"Lists the customization bundles that were created in your NetSuite account.",
				"listbundles"
			],
			[
				"List Files",
				"Lists the files in the File Cabinet of your NetSuite account.",
				"listfiles"
			],
			[
				"List Missing Dependencies",
				"Lists the missing dependencies in the SuiteCloud project.",
				"listmissingdependencies"
			],
			[
				"List Objects",
				"Lists the custom objects in your NetSuite account.",
				"listobjects"
			],
			[
				"Preview",
				"Previews the deployment steps of a folder or zip file that contains the SuiteCloud project.",
				"preview"
			],
			[
				"Update",
				"Updates existing custom objects in the SuiteCloud project folder with the custom objects in your NetSuite account.",
				"update"
			],
			[
				"Update Custom Record With Instances",
				"Updates the custom record object and its instances in the SuiteCloud project.",
				"updatecustomrecordwithinstances"
			],
			[
				"Validate Project",
				"Validates the folder or zip file that contains the SuiteCloud project.",
				"validate"
			],
			[
				"Clear Password",
				"Clears the password from this session",
				""
			]
		]
	}


	def get( index_key ):
		return Config.config_object[ index_key ]