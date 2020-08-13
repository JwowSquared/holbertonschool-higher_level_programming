#include "lists.h"

/**
* check_cycle - finds a linked list with a cycle
* @list: list to check
*
* Return: 1 if list has a cycle, else 0
*/
int check_cycle(listint_t *list)
{
	listint_t *itr, *fast;

	if (list == NULL || list->next == NULL)
		return (0);

	itr = list;
	fast = list->next->next;

	while (itr != NULL && fast != NULL)
	{
		if (itr == fast)
			return (1);
		itr = itr->next;
		if (itr == NULL)
			return (0);
		fast = fast->next->next;
	}

	return (0);
}
