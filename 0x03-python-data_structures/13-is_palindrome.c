#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the head of the linked list.
 *
 * Return: 1 if the list is a palindrome, or 0 otherwise.
*/

int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head;
    listint_t *prev = NULL, *temp, *second_half;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        temp = slow;
        slow = slow->next;
    }

    second_half = slow;
    while (second_half != NULL)
    {
        temp = second_half->next;
        second_half->next = prev;
        prev = second_half;
        second_half = temp;
    }

    while (prev != NULL)
    {
        if ((*head)->n != prev->n)
            return (0);
        (*head) = (*head)->next;
        prev = prev->next;
    }

    return (1);
}
