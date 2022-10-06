/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdameros <tdameros@student.42lyon.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/06 20:43:46 by tdameros          #+#    #+#             */
/*   Updated: 2022/10/06 21:39:40 by tdameros         ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void	*ft_memcpy(void *dest, const void *src, size_t n);

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

void	memcpy_string_type(char *dest, char *src, size_t n)
{
	size_t	len;
	void	*return_ptr;

	len = strlen(dest);
	return_ptr = ft_memcpy(dest, src, n);
	print_bytes(return_ptr, len);
}

void	memcpy_int_type(int dest, int src, size_t n)
{
	void	*return_ptr;

	return_ptr = ft_memcpy(&dest, &src, n);
	print_bytes(return_ptr, sizeof(dest));
}

void	memcpy_float_type(float dest, float src, size_t n)
{
	void	*return_ptr;

	return_ptr = ft_memcpy(&dest, &src, n);
	print_bytes(return_ptr, sizeof(dest));
}

int	main(int argc, char **argv)
{
	size_t	n;

	if (argc == 5)
	{
		n = atoi(argv[4]);
		if (!strcmp(argv[1], "string"))
			memcpy_string_type(argv[2], argv[3], n);
		else if (!strcmp(argv[1], "int"))
			memcpy_int_type(atoi(argv[2]), atoi(argv[3]), n);
		else if (!strcmp(argv[1], "float"))
			memcpy_float_type(atof(argv[2]), atof(argv[3]), n);
	}
}
