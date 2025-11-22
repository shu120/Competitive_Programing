/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: shukondo <shukondo@student.42tokyo.jp>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/03 16:35:49 by shukondo          #+#    #+#             */
/*   Updated: 2025/11/10 19:10:57 by shukondo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strrchr(const char *s, int c)
{
	const char *last = NULL;

	while (*s)
	{
		if (*s == (char)c)
			last = s;
		s++;
	}
	if ((char)c == '\0')
		return ((char *)s);
	return ((char *)last);
}
#include <stdio.h>
#include <string.h>

static void	test_case(const char *s, int c)
{
	char *std = strrchr(s, c);
	char *ft = ft_strrchr(s, c);

	if (std != ft)
	{
		printf("❌ NG: s=\"%s\" c=%d('%c') → std:%p ft:%p\n",
			s, c, (char)c, (void *)std, (void *)ft);
	}
	else
	{
		printf("✅ OK: s=\"%s\" c=%d('%c')\n",
			s, c, (char)c);
	}
}

int	main(void)
{
	const char *tests[] = {
		"abcdef",
		"banana",
		"abcabc",
		"abcd\0efgh",
		"",
		NULL
	};
	int chars[] = {'a', 'c', 'z', '\0', 4, 255, -1};

	for (int i = 0; tests[i]; i++)
	{
		for (int j = 0; j < (int)(sizeof(chars) / sizeof(chars[0])); j++)
			test_case(tests[i], chars[j]);
	}
	return 0;
}