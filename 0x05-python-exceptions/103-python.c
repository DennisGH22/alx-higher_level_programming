#include <Python.h>

void print_python_list(PyObject *p);

/**
 * print_python_list - Prints the elements of a Python list object.
 * @p: A pointer to a PyObject representing a Python list.
*/

void print_python_list(PyObject *p)
{
    /* Check if p is a valid PyListObject */
    if (!PyList_Check(p))
    {
        PyErr_SetString(PyExc_TypeError, "Invalid input: p is not a PyListObject");
        return;
    }

    /* Get the length of the list */
    Py_ssize_t size = PyList_Size(p);

    /* Print the list elements */
    printf("[");
    for (Py_ssize_t i = 0; i < size; ++i)
    {
        PyObject *item = PyList_GetItem(p, i);
        PyObject *str_item = PyObject_Str(item);
        const char *str = PyUnicode_AsUTF8(str_item);
        printf("%s", str);
        Py_XDECREF(str_item);
        if (i < size - 1)
            printf(", ");
    }
    printf("]\n");
}
