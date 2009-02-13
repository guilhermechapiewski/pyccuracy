import re
from element_is_visible_helper import *

class LinkIsVisibleAction(ElementIsVisibleHelper):
	def __init__(self, browser_driver, language):
		ElementIsVisibleHelper.__init__(self, browser_driver, language)

	def get_selector(self, element_name):
		return r"//a[(@name='%s' or @id='%s')]" % (element_name, element_name)
	
	def matches(self, line):
		reg = self.language["link_is_visible_regex"]
		self.last_match = reg.search(line)
		return self.last_match
	
	def values_for(self, line):
		return self.last_match and (self.last_match.groups()[1],) or tuple([])
		
	def execute(self, values):
		checkbox_name = values[0]
		error_message = self.language["link_is_visible_failure"]
		self.execute_is_visible(checkbox_name, error_message)

	def __call__(browser_driver):
		return CheckboxClickAction(browser_driver)