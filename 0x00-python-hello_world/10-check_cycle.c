#include "lists.h"

/**
* check_cycle - finds a linked list with a cycle
* @list: list to check
*
* Return: 1 if list has a cycle, else 0
*/
int check_cycle(listint_t *list)
{
	listint_t *itr;

	if (list == NULL)
		return (0);

	itr = list;

	while (itr != NULL)
	{
		if (itr->visited)
			return (1);
		itr->visited = 1;
		itr = itr->next;
	}

	return (0);
}
