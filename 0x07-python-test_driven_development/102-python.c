#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Print a Python string.
 * @p: PyObject representing a Python string.
 *
 * This function checks if @p is a valid Python string and prints its contents.
 * If @p is not a valid string, it sets a Python exception.
*/

void print_python_string(PyObject *p) {
    if (!PyUnicode_Check(p)) {
        PyErr_SetString(PyExc_TypeError, "p must be a valid string");
        return;
    }

    const char *str = PyUnicode_AsUTF8(p);
    if (str) {
        printf("String: %s\n", str);
    } else {
        PyErr_Print();
    }
}
