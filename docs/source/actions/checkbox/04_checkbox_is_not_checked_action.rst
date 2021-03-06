========================================
I see the "some" checkbox is not checked
========================================

Syntax
------
::

	I see the "<checkbox name>" checkbox is not checked

where:
	``<checkbox name>`` - name or id for the desired input type="checkbox"
	
Description
-----------
Asserts that the specified checkbox is not checked.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match, the element is deemed not available.

Raises
------
Raises ActionFailedError if the checkbox is checked.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I see the "chkSomething" checkbox is not checked
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.1
   Checkbox Is Not Checked action.