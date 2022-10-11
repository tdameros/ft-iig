/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstdelone.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdameros <tdameros@student.42lyon.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/11 18:35:36 by tdameros          #+#    #+#             */
/*   Updated: 2022/10/11 21:56:41 by tdameros         ###   ########lyon.fr   */
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

void	ft_lstdelone(t_list *lst, void (*del)(void *));

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
	ft_lstdelone(node1, free);
	ft_print_lst(node1, 0);
}

void	test1()
{
	t_list	*node1 = ft_lstnew(strdup("node1"));
	ft_lstdelone(node1, free);
	ft_print_lst(node1, 0);
}

void	test2()
{
	t_list	*node2 = ft_lstnew(strdup("node2"));
	t_list	node1 = {"node1", node2};
	ft_lstdelone(node2, free);
	ft_print_lst(&node1, 1);
}

void	test3()
{
	t_list	node3 = {"node3", NULL};
	t_list	*node2 = ft_lstnew(strdup("node2"));
	node2->next = &node3;
	t_list	node1 = {"node1", node2};
	ft_lstdelone(node2, free);
	ft_print_lst(&node1, 1);
	printf("|");
	ft_print_lst(&node3, 1);
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
