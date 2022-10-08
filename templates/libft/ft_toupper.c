/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_toupper.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdameros <tdameros@student.42lyon.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/07 10:58:55 by tdameros          #+#    #+#             */
/*   Updated: 2022/10/07 11:00:27 by tdameros         ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	ft_toupper(int c);

int	main(int argc, char **argv)
{
	if (argc == 2)
		printf("%c", ft_toupper(argv[1][0]));
	return (0);
}
