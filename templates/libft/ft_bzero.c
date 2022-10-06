/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_bzero.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdameros <tdameros@student.42lyon.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/06 20:45:37 by tdameros          #+#    #+#             */
/*   Updated: 2022/10/06 22:21:27 by tdameros         ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void	ft_bzero(void *s, size_t n);

void	print_bytes(void *s, size_t n)
{
	unsigned char	*ptr;
	size_t	index;

	ptr = (unsigned char *) s;
	index = 0;
	while (index < n)
	{
		printf("%d|", *ptr);
		ptr++;
		index++;
	}
}

void	bzero_str_type(char *str, size_t len, size_t n)
{
	ft_bzero(str, n);
	print_bytes(str, len);
}

void	bzero_int_type(int nbr, size_t n)
{
	ft_bzero(&nbr, n);
	print_bytes(&nbr, sizeof(nbr));
}

void	bzero_float_type(float nbr, size_t n)
{
	ft_bzero(&nbr, n);
	print_bytes(&nbr, sizeof(nbr));
}

int	main(int argc, char **argv)
{
	size_t	n;

	if (argc == 4)
	{
		n = atoi(argv[3]);
		if (!strcmp(argv[1], "string"))
			bzero_str_type(argv[2], strlen(argv[2]), n);
		else if (!strcmp(argv[1], "int"))
			bzero_int_type(atoi(argv[2]), n);
		else if (!strcmp(argv[1], "float"))
			bzero_float_type(atof(argv[2]), n);
	}
	return (0);
}
