/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_tolower.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdameros <tdameros@student.42lyon.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/07 11:08:56 by tdameros          #+#    #+#             */
/*   Updated: 2022/10/07 11:10:14 by tdameros         ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	ft_tolower(int c);

int	main(int argc, char **argv)
{
	if (argc == 2)
		printf("%c", ft_tolower(argv[1][0]));
	return (0);
}
