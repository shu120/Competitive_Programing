/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: kondoshuji <kondoshuji@student.42.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/28 21:42:53 by kondoshuji        #+#    #+#             */
/*   Updated: 2025/08/29 00:40:41 by kondoshuji       ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
int	ft_strcmp(char *a, char *b)
{
	while(*a && *a == *b)
	{
		a++;
		b++;
	}
	return (*a - *b);
}

int	main(void)
{
	printf("%d\n", ft_strcmp("abc", "aba"));
}