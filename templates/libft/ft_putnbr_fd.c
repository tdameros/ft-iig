/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdameros <tdameros@student.42lyon.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/10/11 13:25:04 by tdameros          #+#    #+#             */
/*   Updated: 2022/10/11 14:06:13 by tdameros         ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

void	ft_putnbr_fd(int n, int fd);

int	main(int argc, char **argv)
{
	if (argc == 3)
		ft_putnbr_fd(atoi(argv[1]), atoi(argv[2]));
}
