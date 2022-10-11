/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_striteri.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdameros <tdameros@student.42lyon.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/11 12:42:19 by tdameros          #+#    #+#             */
/*   Updated: 2022/10/11 13:22:08 by tdameros         ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void	ft_striteri(char *s, void (*f)(unsigned int, char*));

void	ft_tolower(unsigned int i, char	*c)
{
	(void) i;
	if (*c >= 'A' && *c <= 'Z')
		*c = *c + 32;
}

void	ft_toupper(unsigned int i, char *c)
{
	(void) i;
	if (*c >= 'a' && *c <= 'z')
		*c = *c - 32;
}

void	ft_upper_eveni(unsigned int i, char *c)
{
	if (i % 2 == 0)
		ft_toupper(i, c);
	else
		ft_tolower(i, c);
}

int	main(int argc, char **argv)
{
	if (argc == 3)
	{
		if (!strcmp(argv[2], "ft_tolower"))
			ft_striteri(argv[1], ft_tolower);
		else if (!strcmp(argv[2], "ft_toupper"))
			ft_striteri(argv[1], ft_toupper);
		else if (!strcmp(argv[2], "ft_upper_eveni"))
			ft_striteri(argv[1], ft_upper_eveni);
		printf("%s", argv[1]);
	}	
	return (0);
}
