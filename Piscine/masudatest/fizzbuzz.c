/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   fizzbuzz.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: kondoshuji <kondoshuji@student.42.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/29 01:27:11 by kondoshuji        #+#    #+#             */
/*   Updated: 2025/08/29 01:49:15 by kondoshuji       ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putnbr(int n)
{
	char c;

	if (n >= 10)
		ft_putnbr(n / 10);
	c = '0' + (n % 10);
	write(1, &c, 1);
}

void	ft_putstr(char *s)
{
	while(*s)
		write(1, s++, 1);
}

void	fizzbuzz(void)
{
	int	i;

	i = 0;
	while (i <= 10)
	{
		if (i % 15 == 0)
			ft_putstr("FizzBuzz");
		else if (i % 3 == 0)
			ft_putstr("Fizz");
		else if (i % 5 == 0)
			ft_putstr("Buzz");
		else
			ft_putnbr(i);
		write(1, " ", 1);
		i++;
	}
}

int	main(void)
{
	fizzbuzz();
	return (0);
}