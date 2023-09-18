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
    Py_ssize_t length = ((PyASCIIObject *)(p))->length;

    if (!p || !PyUnicode_Check(p))
    {
        fprintf(stderr, "[ERROR] Invalid String Object\n");
        return;
    }

    printf("[.] string object info\n");

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf(" type: compact ascii\n");
	else
		printf(" type: compact unicode object\n");

    printf("  length: %zd\n", length);
    printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}
