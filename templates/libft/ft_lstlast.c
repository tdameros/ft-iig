/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstlast.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdameros <tdameros@student.42lyon.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/11 18:35:36 by tdameros          #+#    #+#             */
/*   Updated: 2022/10/11 20:04:06 by tdameros         ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <string.h>

typedef struct s_list
{
	void			*content;
	struct s_list	*next;
}	t_list;

t_list *ft_lstlast(t_list *lst);

void	print_node(t_list *node)
{
	if (node == NULL)
		printf("NULL");
	else
		printf("%s", (char *) node->content);
}

void	testnull()
{
	t_list	*node1 = NULL;
	print_node(ft_lstlast(node1));
}

void	test1()
{
	t_list	node1 = {"node1", NULL};
	print_node(ft_lstlast(&node1));
}

void	test2()
{
	t_list	node2 = {"node2", NULL};
	t_list	node1 = {"node1", &node2};
	print_node(ft_lstlast(&node1));
}

void	test3()
{
	t_list	node3 = {"node3", NULL};
	t_list	node2 = {"node2", &node3};
	t_list	node1 = {"node1", &node2};
	print_node(ft_lstlast(&node1));
}

int	main(int argc,	char **argv)
{
	if (argc == 2)
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
