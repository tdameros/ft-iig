/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isprint.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdameros <tdameros@student.42lyon.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/06 20:42:56 by tdameros          #+#    #+#             */
/*   Updated: 2022/10/06 20:43:34 by tdameros         ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

int	ft_isprint(int c);

int	main(int argc, char **argv)
{
	int	nbr;

	(void) argc;
	nbr = atoi(argv[1]);
	printf("%d", ft_isprint(nbr));
	return (0);
}
