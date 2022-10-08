/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdameros <tdameros@student.42lyon.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/07 12:57:55 by tdameros          #+#    #+#             */
/*   Updated: 2022/10/07 13:12:18 by tdameros         ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int	ft_memcmp(const void *s1, const void *s2, size_t n);

void	memcmp_string_type(char *s1, char *s2, size_t n)
{
	int	result;

	result = ft_memcmp(s1, s2, n);
	if (result < 0)
		result = -1;
	else if (result > 0)
		result = 1;
	else
		result = 0;
	printf("%d", result);
}

void	memcmp_int_type(int s1, int s2, size_t n)
{
	int	result;

	result = ft_memcmp(&s1, &s2, n);
	if (result < 0)
		result = -1;
	else if (result > 0)
		result = 1;
	else
		result = 0;
	printf("%d", result);
}

void	memcmp_float_type(float s1, float s2, size_t n)
{
	int	result;

	result = ft_memcmp(&s1, &s2, n);
	if (result < 0)
		result = -1;
	else if (result > 0)
		result = 1;
	else
		result = 0;
	printf("%d", result);
}

int	main(int argc, char **argv)
{
	size_t	n;

	if (argc == 5)
	{
		n = atoi(argv[4]);
		if (!strcmp(argv[1], "string"))
			memcmp_string_type(argv[2], argv[3], n);
		else if (!strcmp(argv[1], "int"))
			memcmp_int_type(atoi(argv[2]), atoi(argv[3]), n);
		else if (!strcmp(argv[1], "float"))
			memcmp_float_type(atof(argv[2]), atof(argv[3]), n);
	}
	return (0);
}
