/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   split_dict.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: kondoshuji <kondoshuji@student.42.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/24 20:13:00 by kondoshuji        #+#    #+#             */
/*   Updated: 2025/08/24 20:28:16 by kondoshuji       ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "./rush02.h"

char	*ft_strdup(char *src);
char	*ft_trim(char *str);

/**
 * @brief 最初のコロンを探す
 * 
 * @param s 入力文字列
 */
static char	*find_colon(char *s)
{
	int	i;

	if (!s)
		return (0);
	i = 0;
	while (s[i] != '\0')
	{
		if (s[i] == ':')
			return (s + i);
		i++;
	}
	return (0);
}

/**
 * @brief 文字列が空でなく、すべて数字かを判定
 * 
 * @param s 入力文字列

 * @retval 
 * 1: 数字のみ 
 * 0: otherwise
 */
static int	is_all_digit(const char *s)
{
	int	i;

	if (!s || *s == '\0')
		return (0);
	i = 0;
	while (s[i] != '\0')
	{
		if (s[i] < '0' || s[i] > '9')
			return (0);
		i++;
	}
	return (1);
}

/**
 * @brief "num : str" を分割する
 * 
 * @param[in,out] line GNL行バッファ
 * @param[out]    left 数字(左)の先頭ポインタ
 * @param[out]    right 単語(右)の先頭ポインタ

 */
static int	split_view(char *line, char **left, char **right)
{
	char *p;
	char *c;

	if (!line || !left || !right)
		return (0);
	p = ft_trim(line);
	if (*p == '\0')
		return (0);
	c = find_colon(p);
	if (!c)
		return (0);
	*c = '\0';
	*left = ft_trim(p);
	*right = ft_trim(c + 1);
	if (!is_all_digit(*left))
		return (0);
	if (**right == '\0')
		return (0);
	return (1);
}

/**
 * @brief split で確保したt_splitを解放
 */
void	free_split(t_split *sp)
{
	if (!sp)
		return ;
	if (sp -> num)
	{
		free(sp -> num);
		sp -> num = 0;
	}
	if (sp -> str)
	{
		free(sp -> str);
		sp -> str = 0;
	}
}
