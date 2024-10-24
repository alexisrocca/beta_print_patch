from . import __version__ as app_version

app_name = "beta_print_patch"
app_title = "Beta Print Patch"
app_publisher = "IEA-IT"
app_description = "Patch frappe print application (version-14)."
app_email = "it@iea.com.ar"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/beta_print_patch/css/beta_print_patch.css"
# app_include_js = "/assets/beta_print_patch/js/beta_print_patch.js"

# include js, css files in header of web template
# web_include_css = "/assets/beta_print_patch/css/beta_print_patch.css"
# web_include_js = "/assets/beta_print_patch/js/beta_print_patch.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "beta_print_patch/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
page_js = {"print" : "public/js/beta_print_patch.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "beta_print_patch.utils.jinja_methods",
#	"filters": "beta_print_patch.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "beta_print_patch.install.before_install"
# after_install = "beta_print_patch.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "beta_print_patch.uninstall.before_uninstall"
# after_uninstall = "beta_print_patch.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "beta_print_patch.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"beta_print_patch.tasks.all"
#	],
#	"daily": [
#		"beta_print_patch.tasks.daily"
#	],
#	"hourly": [
#		"beta_print_patch.tasks.hourly"
#	],
#	"weekly": [
#		"beta_print_patch.tasks.weekly"
#	],
#	"monthly": [
#		"beta_print_patch.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "beta_print_patch.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "beta_print_patch.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "beta_print_patch.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"beta_print_patch.auth.validate"
# ]
