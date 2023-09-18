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
    long int length = ((PyASCIIObject *)(p))->length;
    char *wide_str = PyUnicode_AsWideCharString(p, &length);

    if (!p || !PyUnicode_Check(p))
    {
        fprintf(stderr, "[ERROR] Invalid String Object\n");
        return;
    }

    printf("[.] string object info\n");

    printf("  type: %s\n", PyUnicode_IS_COMPACT_ASCII(p) ? "compact ascii" : "compact unicode object");
    printf("  length: %ld\n", length);
    printf("  value: %ls\n", wide_str);

    PyMem_Free((void *)wide_str);
}
