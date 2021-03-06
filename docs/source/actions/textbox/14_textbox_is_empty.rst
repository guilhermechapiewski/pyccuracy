=============================
I see "some" textbox is empty
=============================

Syntax
------
::

	I see "<textbox name>" textbox is empty

where:
	``<textbox name>`` - name or id for the desired textbox element
	
Description
-----------
Asserts that the specified textbox current text is empty.

.. note::

   The specified name will be checked against both "name" and "id" values. Only if neither of those match,
   the element is deemed not available.
   
Raises
------
Raises ActionFailedError if the textbox's text is not empty.
This Exception is captured by Pyccuracy to assert that the test failed.
	
Examples
--------
::

	...
	Then
		I see "txtSomething" textbox is empty
	
*Rest of the test ommitted for clarity*

Changelog
---------
.. versionadded:: 0.3
   Textbox Is Empty action.
