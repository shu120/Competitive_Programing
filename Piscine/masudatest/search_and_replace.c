/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   search_and_replace.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: kondoshuji <kondoshuji@student.42.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/29 02:05:51 by kondoshuji        #+#    #+#             */
/*   Updated: 2025/08/29 02:16:27 by kondoshuji       ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int	main(int ac, char **argv)
{
	char c;
	int i = 0;

	if (ac != 4 || !argv[2][0] || argv[2][1] || !argv[3][0] || argv[3][1])
	{
		write(1, "\n", 1);
		return (0);
	}
	while (argv[1][i])
	{
		c = argv[1][i];
		if (c == argv[2][0])
			c = argv[3][0];
		write(1, &c, 1);
		i++;
	}
}