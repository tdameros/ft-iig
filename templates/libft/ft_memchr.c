/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdameros <tdameros@student.42lyon.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/07 11:49:21 by tdameros          #+#    #+#             */
/*   Updated: 2022/10/07 13:11:13 by tdameros         ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void	*ft_memchr(const void *s, int c, size_t n);

void	memchr_string_type(char *s, int c, size_t n)
{
	void	*return_ptr;
	void	*expected_ptr;

	return_ptr = ft_memchr(s, c, n);
	expected_ptr = memchr(s, c, n);
	if (return_ptr == expected_ptr)
		printf("valid return ptr");
	else
		printf("invalid return ptr");
}

void	memchr_int_type(int s, int c, size_t n)
{
	void	*return_ptr;
	void	*expected_ptr;

	return_ptr = ft_memchr(&s, c, n);
	expected_ptr = memchr(&s, c, n);
	if (return_ptr == expected_ptr)
		printf("valid return ptr");
	else
		printf("invalid return ptr");
}

void	memchr_float_type(float s, int c, size_t n)
{
	void	*return_ptr;
	void	*expected_ptr;

	return_ptr = ft_memchr(&s, c, n);
	expected_ptr = memchr(&s, c, n);
	if (return_ptr == expected_ptr)
		printf("valid return ptr");
	else
		printf("invalid return ptr");
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
			memchr_string_type(argv[2], c, n);
		else if (!strcmp(argv[1], "int"))
			memchr_int_type(atoi(argv[2]), c, n);
		else if (!strcmp(argv[1], "float"))
			memchr_float_type(atof(argv[2]), c, n);
	}
	return (0);
}
