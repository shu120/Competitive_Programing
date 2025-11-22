/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rot_13.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: kondoshuji <kondoshuji@student.42.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/29 01:04:14 by kondoshuji        #+#    #+#             */
/*   Updated: 2025/08/29 01:20:51 by kondoshuji       ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

static char	swap_case(char c)
{
	if (c >= 'a' && c <= 'z')
		return (c - 'a' + 'A'); // 小文字→大文字
	if (c >= 'A' && c <= 'Z')
		return (c - 'A' + 'a'); // 大文字→小文字
	return (c);                 // それ以外はそのまま
}

int	main(int ac, char **av)
{
	int	i;

	if (ac != 2)
	{
		write(1, "\n", 1);
		return (0);
	}
	i = 0;
	while (av[1][i])
	{
		char x = swap_case(av[1][i]);
		write(1, &x, 1);
		i++;
	}
	write(1, "\n", 1);
	return (0);
}
