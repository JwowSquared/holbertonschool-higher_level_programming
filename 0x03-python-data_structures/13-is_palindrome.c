#include "lists.h"

/**
* is_palindrome - checks if a linked list is a palindrome
* @head: head of linked list
*
* Return: 1 if list is palindrome, else 0
*/
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);

	if (helper(*head, *head) != NULL)
		return (1);
	return (0);
}

/**
* helper - recursively compares the forwards list with the backwards list
* @itr: list that will be backwards as the recursion unfolds
* @head: starts going forward once recursion unfolds
*
* Return: NULL if not palindrome, else random valid pointer is returned
*/
listint_t *helper(listint_t *itr, listint_t *head)
{
	listint_t *out = NULL;

	if (itr == NULL)
		return (head);

	out = helper(itr->next, head);
	if (out == NULL)
		return (NULL);

	if (itr->n == out->n)
	{
		if (itr != head)
			return (out->next);
		return (out);
	}
	return (NULL);
}
