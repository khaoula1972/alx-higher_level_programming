#include "lists.h"
/**
 * is_palindrome - a function that checks if
 * a singly linked list is a palindrome.
 * @head: pointer to the first node
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int flag = 1;
	listint_t *slow = *head, *fast = *head;
	listint_t *second_half = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (flag);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	if (fast != NULL)
		slow = slow->next;

	second_half = reverse_list(&slow);
	while (second_half != NULL)
	{
		if ((*head)->n != second_half->n)
			flag = 0;
		*head = (*head)->next;
		second_half = second_half->next;
	}
	reverse_list(&slow);
	return (flag);
}

/**
 * reverse_list - Reverses a linked list starting from the given node.
 * @head: Pointer to the head node of the list.
 * Return: Pointer to the new head of the reversed list.
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
	return (*head);
}
