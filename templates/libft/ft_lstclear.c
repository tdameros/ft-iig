/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstclear.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdameros <tdameros@student.42lyon.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/11 18:35:36 by tdameros          #+#    #+#             */
/*   Updated: 2022/10/11 22:09:07 by tdameros         ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct s_list
{
	void			*content;
	struct s_list	*next;
}	t_list;

void ft_lstclear(t_list **lst, void (*del)(void *));

void	ft_print_lst(t_list	*lst, int len)
{
	if (len == 0)
		printf("NULL");
	while (len)
	{
		printf("%s", (char *) lst->content);
		lst = lst->next;
		len--;
		if (len)
			printf("->");
	}
}

t_list	*ft_lstnew(void *content)
{
	t_list	*new_node;

	new_node = malloc(sizeof(t_list));
	if (new_node == NULL)
		return (NULL);
	new_node->content = content;
	new_node->next = NULL;
	return (new_node);
}

void	testnull()
{
	t_list	*node1 = NULL;
	ft_lstclear(&node1, free);
	ft_print_lst(node1, 0);
}

void	test1()
{
	t_list	*node1 = ft_lstnew(strdup("node1"));
	ft_lstclear(&node1, free);
	if (node1 == NULL)
		ft_print_lst(node1, 0);
	else
		printf("Initial ptr must be set to NULL");
}

void	test2()
{
	t_list	*node2 = ft_lstnew(strdup("node2"));
	t_list	*node1 = ft_lstnew(strdup("node1"));
	node1->next = node2;
	ft_lstclear(&node1, free);
	if (node1 == NULL)
		ft_print_lst(node1, 0);
	else
		printf("Initial ptr must be set to NULL");
}

void	test3()
{
	t_list	*node3 = ft_lstnew(strdup("node3"));
	t_list	*node2 = ft_lstnew(strdup("node2"));
	t_list	*node1 = ft_lstnew(strdup("node1"));
	node1->next = node2;
	node2->next = node3;
	ft_lstclear(&node1, free);
	if (node1 == NULL)
		ft_print_lst(node1, 0);
	else
		printf("Initial ptr must be set to NULL");
}

int	main(int argc,	char **argv)
{
	if (argc == 3)
	{
		if (!strcmp(argv[1], "NULL"))
			testnull();
		else if (!strcmp(argv[1], "node1"))
			test1();
		else if (!strcmp(argv[1], "node1->node2"))
			test2();
		else if (!strcmp(argv[1], "node1->node2->node3"))
			test3();
	}
	return (0);
}
