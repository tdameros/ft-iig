/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdameros <tdameros@student.42lyon.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/06 20:43:46 by tdameros          #+#    #+#             */
/*   Updated: 2022/10/06 22:18:54 by tdameros         ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void	*ft_memmove(void *dest, const void *src, size_t n);

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

void	memmove_string_type(char *dest, char *src, size_t n, int overlap)
{
	size_t			len;
	void			*return_ptr;
	unsigned char	*dest_ptr;

	len = strlen(src);
	if (overlap)
	{
		dest_ptr = (unsigned char *) src;
		dest_ptr++;
		return_ptr = ft_memmove(dest_ptr, src, n);
	}
	else
	{
		return_ptr = ft_memmove(dest, src, n);
	}
	print_bytes(return_ptr, len);
}

void	memmove_int_type(int dest, int src, size_t n, int overlap)
{
	void			*return_ptr;
	unsigned char	*dest_ptr;

	if (overlap)
	{
		dest_ptr = (unsigned char *) &src;
		dest_ptr++;
		return_ptr = ft_memmove(dest_ptr, &src, n);
	}
	else
	{
		return_ptr = ft_memmove(&dest, &src, n);
	}
	print_bytes(return_ptr, 4);
}

void	memmove_float_type(float dest, float src, size_t n, int overlap)
{
	void			*return_ptr;
	unsigned char	*dest_ptr;

	if (overlap)
	{
		dest_ptr = (unsigned char *) &src;
		dest_ptr++;
		return_ptr = ft_memmove(dest_ptr, &src, n);
	}
	else
	{
		return_ptr = ft_memmove(&dest, &src, n);
	}
	print_bytes(return_ptr, 4);
}

int	main(int argc, char **argv)
{
	size_t	n;
	int		overlap;

	if (argc == 5)
	{
		n = atoi(argv[4]);
		if (!strcmp(argv[2], "src++"))
			overlap = 1;
		if (!strcmp(argv[1], "string"))
			memmove_string_type(argv[2], argv[3], n, overlap);
		else if (!strcmp(argv[1], "int"))
			memmove_int_type(atoi(argv[2]), atoi(argv[3]), n, overlap);
		else if (!strcmp(argv[1], "float"))
			memmove_float_type(atof(argv[2]), atof(argv[3]), n, overlap);
	}
}

