#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <string.h>

/**
 * print_python_bytes - print python things
 * @p: pointer to PyObject p
*/

void print_python_bytes(PyObject *p)
{
    size_t byte_count, i;
    char *data;

    setbuf(stdout, NULL);
    printf("[.] bytes object info\n");

    if (PyBytes_Check(p) == 0)
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    data = ((PyBytesObject *)(p))->ob_sval;
    byte_count = PyBytes_Size(p);
    printf("  size: %ld\n  trying string: %s\n", byte_count, data);
    
    if (byte_count >= 10)
		byte_count = 10;
	else
		byte_count++;

    printf("  first %ld bytes: ", byte_count);
    
    for (i = 0; i < byte_count - 1; i++)
        printf("%02hhx ", data[i]);
        
    printf("%02hhx\n", data[i]);
}

/**
 * print_python_float - print python things
 * @p: pointer to PyObject p
*/

void print_python_float(PyObject *p)
{
    char *str_repr;
    double float_val;

    setbuf(stdout, NULL);
    printf("[.] float object info\n");

    if (PyFloat_Check(p) == 0)
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    float_val = ((PyFloatObject *)(p))->ob_fval;
    str_repr = PyOS_double_to_string(float_val, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
    printf("  value: %s\n", str_repr);
}

/**
 * print_python_list - print python things
 * @p: pointer to PyObject p
*/

void print_python_list(PyObject *p)
{
    size_t list_size, i;
    const char *type_name;
    PyListObject *list_obj;

    setbuf(stdout, NULL);
    printf("[*] Python list info\n");

    if (PyList_Check(p) == 0)
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    list_obj = (PyListObject *)p;
    list_size = PyList_GET_SIZE(p);
    size_t allocated_size = list_obj->allocated;

    printf("[*] Size of the Python List = %ld\n[*] Allocated = %li\n", list_size, allocated_size);
    for (i = 0; i < list_size; i++)
    {
        type_name = (list_obj->ob_item[i])->ob_type->tp_name;
        printf("Element %li: %s\n", i, type_name);
        
        if (!strcmp(type_name, "bytes"))
            print_python_bytes(list_obj->ob_item[i]);
        else if (!strcmp(type_name, "float"))
            print_python_float(list_obj->ob_item[i]);
    }
}
