/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstiter.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdameros <tdameros@student.42lyon.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/11 22:22:06 by tdameros          #+#    #+#             */
/*   Updated: 2022/10/11 22:58:14 by tdameros         ###   ########lyon.fr   */
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

void	ft_lstiter(t_list *lst, void (*f)(void *));

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

void	ft_strupper(void *s)
{
	char	*s_str = (char *) s;

	while (*s_str != '\0')
	{
		*s_str = toupper(*s_str);
		s_str++;
	}
}

void	ft_strlower(void *s)
{
	char	*s_str = (char *) s;

	while (*s_str != '\0')
	{
		*s_str = tolower(*s_str);	
		s_str++;
	}
}

void	lstiter(void (*f)(void *))
{
	char	*s3 = strdup("node3");
	char	*s2 = strdup("node2");
	char	*s1 = strdup("node1");
	t_list	node3 = {s3, NULL};
	t_list	node2 = {s2, &node3};
	t_list	node1 = {s1, &node2};
	ft_lstiter(&node1, f);
	ft_print_lst(&node1);
	free(s1);
	free(s2);
	free(s3);
}

void	lstiter_null(void (*f)(void *))
{
	t_list	*node1 = NULL;
	ft_lstiter(node1, f);
	ft_print_lst(node1);
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
