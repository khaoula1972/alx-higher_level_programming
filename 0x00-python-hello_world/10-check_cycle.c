#include "lists.h"
/**
 * check_cycle - a function in C that checks if a singly linked list
 * has a cycle in it.
 * @list: pointer to the head of the linked list
 * Return: 1 if there is a cycle, 0 if there is no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *walker, *runner;

	if (list == NULL || list->next == NULL)
		return (0);

	walker = list;
	runner = list->next;

	while (runner != NULL && runner->next != NULL)
	{
		if (runner == walker)
			return (1);

		walker = walker->next;
		runner = runner->next->next;
	}
	return (0);
}
