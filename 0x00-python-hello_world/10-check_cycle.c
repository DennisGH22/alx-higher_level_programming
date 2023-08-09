#include "lists.h"

/**
 * check_cycle - Check if a linked list has a cycle
 * @list: Pointer to the head of the linked list
 *
 * Return: 0 if there is no cycle, or 1 if there is a cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *slowPointer;
	listint_t *fastPointer;

	if (list == NULL || list->next == NULL)
		return (0);

	slowPointer = list;
	fastPointer = list;

	for (; slowPointer && fastPointer && fastPointer->next;)
	{
		slowPointer = slowPointer->next;
		fastPointer = fastPointer->next->next;

		if (slowPointer == fastPointer)
			return (1);
	}

	return (0);
}
