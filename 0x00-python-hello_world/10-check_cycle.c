#include "lists.h"

/**
* check_cycle - finds a linked list with a cycle
* @list: list to check
*
* Return: 1 if list has a cycle, else 0
*/
int check_cycle(listint_t *list)
{
	listint_t *itr, *stopper;
	int i, j = 1;

	if (list == NULL)
		return (0);

	stopper = list->next;

	while (stopper != NULL)
	{
		i = 0;
		itr = list;
		while (i < j)
		{
			if (itr == stopper)
				return (1);
			i++;
			itr = itr->next;
		}
		j++;
		stopper = stopper->next;
	}

	return (0);
}
