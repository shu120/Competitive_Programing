/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: kondoshuji <kondoshuji@student.42.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/28 21:23:05 by kondoshuji        #+#    #+#             */
/*   Updated: 2025/08/28 21:42:16 by kondoshuji       ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putnbr(int nb)
{
	char	buf[11];
	int		i;
	long	n;

	i = 0;
	n = nb;
	if (n == 0)
	{
		write(1, "0", 1);
		return ;
	}
	if (n < 0)
	{
		write (1, "-", 1);
		n = -n;
	}
	while (n > 0)
	{
		buf[i++] = (n % 10) + '0';
		n = n /10;
	}
	while (i--)
		write(1, &buf[i], 1);
}

int	main(void)
{
	ft_putnbr(42);
	write (1, "\n", 1);
}