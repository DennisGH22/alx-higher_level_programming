#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Print a Python string.
 * @p: PyObject representing a Python string.
 *
 * This function checks if @p is a valid Python string and prints its contents.
 * If @p is not a valid string, it sets a Python exception.
*/

void print_python_string(PyObject *p)
{
	Py_ssize_t length;
	const wchar_t *wide_str;

	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	printf("[.] string object info\n");

	length = ((PyASCIIObject *)(p))->length;
	wide_str = PyUnicode_AsWideCharString(p, &length);

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	printf("  length: %ld\n", length);
	printf("  value: %ls\n", wide_str);
}
