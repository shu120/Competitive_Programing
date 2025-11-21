/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncmp.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: shukondo <shukondo@student.42tokyo.jp>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/03 16:37:31 by shukondo          #+#    #+#             */
/*   Updated: 2025/11/05 21:59:35 by shukondo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_strncmp(const char *s1, const char *s2, size_t n)
{
	unsigned char	*p1;
	unsigned char	*p2;

	p1 = (unsigned char *)s1;
	p2 = (unsigned char *)s2;

	if (n == 0)
		return (0);
	while (n--)
	{
		if (*p1 != *p2)
			return ((int)(*p1 - *p2));
		if (*p1 == '\0')
			break;
		p1++;
		p2++;
	}
}
