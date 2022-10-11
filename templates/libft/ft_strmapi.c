/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmapi.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdameros <tdameros@student.42lyon.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/11 12:42:19 by tdameros          #+#    #+#             */
/*   Updated: 2022/10/11 13:10:40 by tdameros         ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char	*ft_strmapi(char const *s, char (*f)(unsigned int, char));

char	ft_tolower(unsigned int i, char c)
{
	(void) i;
	if (c >= 'A' && c <= 'Z')
		return (c + 32);
	return (c);
}

char	ft_toupper(unsigned int i, char c)
{
	(void) i;
	if (c >= 'a' && c <= 'z')
		return (c - 32);
	return (c);
}

char	ft_upper_eveni(unsigned int i, char c)
{
	if (i % 2 == 0)
		return (ft_toupper(i, c));
	return (ft_tolower(i, c));
}

int	main(int argc, char **argv)
{
	char	*str_map;

	if (argc == 3)
	{
		if (!strcmp(argv[2], "ft_tolower"))
			str_map = ft_strmapi(argv[1], ft_tolower);
		else if (!strcmp(argv[2], "ft_toupper"))
			str_map = ft_strmapi(argv[1], ft_toupper);
		else if (!strcmp(argv[2], "ft_upper_eveni"))
			str_map = ft_strmapi(argv[1], ft_upper_eveni);
		if (str_map != NULL)
		{
			printf("%s", str_map);
			free(str_map);
		}
	}	
	return (0);
}
