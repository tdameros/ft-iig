/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isascii.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdameros <tdameros@student.42lyon.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/06 20:40:29 by tdameros          #+#    #+#             */
/*   Updated: 2022/10/06 20:41:20 by tdameros         ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

int	ft_isascii(int c);

int	main(int argc, char **argv)
{
	int		nbr;

	(void) argc;
	nbr = atoi(argv[1]);
	printf("%d", ft_isascii(nbr));
	return (0);
}
