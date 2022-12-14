/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memset.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdameros <tdameros@student.42lyon.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/06 19:15:27 by tdameros          #+#    #+#             */
/*   Updated: 2022/10/06 19:15:30 by tdameros         ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void	*ft_memset(void *s, int c, size_t n);

void	print_bytes(void *s, size_t n)
{
	unsigned char	*ptr;
	size_t			index;

	ptr = (unsigned char *) s;
	index = 0;
	while (index < n)
	{
		printf("%d|", *ptr);
		ptr++;
		index++;
	}
}

void	memset_string_type(char *s, int c, size_t n)
{
	size_t	len;
	void	*return_ptr;

	len = strlen(s);
	return_ptr = ft_memset(s, c, n);
	print_bytes(return_ptr, len);
}

void	memset_int_type(int s, int c, size_t n)
{
	void	*return_ptr;

	return_ptr = ft_memset(&s, c, n);
	print_bytes(return_ptr, sizeof(s));
}

void	memset_float_type(float s, int c, size_t n)
{
	void	*return_ptr;

	return_ptr = ft_memset(&s, c, n);
	print_bytes(return_ptr, sizeof(s));
}

int	main(int argc, char **argv)
{
	int		c;
	size_t	n;

	if (argc == 5)
	{
		c = atoi(argv[3]);
		n = atoi(argv[4]);
		if (!strcmp(argv[1], "string"))
			memset_string_type(argv[2], c, n);
		else if (!strcmp(argv[1], "int"))
			memset_int_type(atoi(argv[2]), c, n);
		else if (!strcmp(argv[1], "float"))
			memset_float_type(atof(argv[2]), c, n);
	}
	return (0);
}
