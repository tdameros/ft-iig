/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstmap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdameros <tdameros@student.42lyon.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/11 22:22:06 by tdameros          #+#    #+#             */
/*   Updated: 2022/10/11 23:28:08 by tdameros         ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

typedef struct s_list
{
	void			*content;
	struct s_list	*next;
}	t_list;

t_list	*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *));

void	ft_lstdelone(t_list *lst, void (*del)(void *))
{
	if (lst != NULL)
	{
		del(lst->content);
		free(lst);
	}
}

void ft_lstclear(t_list **lst, void (*del)(void *))
{
	t_list	*current_node;
	t_list	*next_node;

	current_node = *lst;	
	while (current_node != NULL)
	{
		next_node = current_node->next;
		ft_lstdelone(current_node, del);
		current_node = next_node;
	}
	*lst = NULL;
}

void	ft_print_lst(t_list	*lst)
{
	if (lst == NULL)
		printf("NULL");
	while (lst != NULL)
	{
		printf("%s", (char *) lst->content);
		if (lst->next != NULL)
			printf("->");
		lst = lst->next;
	}
}

void	*ft_strupper(void *s)
{
	char	*s_str;
	int		index;
   
	s_str = strdup((char *) s);
	index = 0;
	while (s_str[index] != '\0')
	{
		s_str[index] = toupper(s_str[index]);	
		index++;
	}
	return ((void *) s_str);
}

void	*ft_strlower(void *s)
{
	char	*s_str;
	int		index;
   
	s_str = strdup((char *) s);
	index = 0;
	while (s_str[index] != '\0')
	{
		s_str[index] = tolower(s_str[index]);	
		index++;
	}
	return ((void *) s_str);
}

void	lstiter(void *(*f)(void *))
{
	t_list	node3 = {"node3", NULL};
	t_list	node2 = {"node2", &node3};
	t_list	node1 = {"node1", &node2};
	t_list	*new_lst = ft_lstmap(&node1, f, free);
	ft_print_lst(new_lst);
	ft_lstclear(&new_lst, free);
}

void	lstiter_null(void *(*f)(void *))
{
	t_list	*node1 = NULL;
	t_list	*new_lst = ft_lstmap(node1, f, free);
	ft_print_lst(new_lst);
	ft_lstclear(&new_lst, free);
}

int	main(int argc, char **argv)
{
	if (argc == 3)
	{
		if (!strcmp(argv[1], "node1->node2->node3") && !strcmp(argv[2], "strupper"))
			lstiter(ft_strupper);
		else if (!strcmp(argv[1], "node1->node2->node3") && !strcmp(argv[2], "strlower"))
			lstiter(ft_strlower);
		else if (!strcmp(argv[1], "NULL") && !strcmp(argv[2], "strupper"))
			lstiter_null(ft_strupper);
		else if (!strcmp(argv[1], "NULL") && !strcmp(argv[2], "strlower"))
			lstiter_null(ft_strlower);
	}	
	return (0);
}
