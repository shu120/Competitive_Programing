/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   split_thousands.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: kondoshuji <kondoshuji@student.42.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/23 16:52:30 by kondoshuji        #+#    #+#             */
/*   Updated: 2025/08/23 18:19:26 by kondoshuji       ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

#define SPLIT 13

int	split_by_thousands(const char *str, int out[SPLIT])
{
	int	len = 0;
	int	count = 0;

	while (str[len])
	{
		if (str[len] < '0' || str[len] > '9')
			return (-1); // 数字以外があればエラー
		len++;
	}
	if (len == 0)
		return (-1);

	// 末尾から3桁ずつ処理
	while (len > 0)
	{
		if (count >= SPLIT)
			return (-1); // undecillionを超えた → Dict Error扱い
	}
	return (count);
}


/**
 * @brief  3桁ブロック列をdictで組み立てて出力する(アメリカ式)
 *
 * @param[in] blocks  下位からの3桁ブロック配列（blocks[0]が一の位）
 * @return  0: 正常出力 / -1: 必要語の欠如などで出力不能
 *
 * @internal
 *変数 i: ブロックを走査するループ変数
 *変数 first: 最初の単語かどうかを管理
 *変数 all_zero: 全ブロックが0かどうかを判定するフラグ
 *変数 n: 現在処理しているブロックの値（0〜999）
 */

int	print_blocks(const int *blocks, int len, char zero[], char nineteen[NINETEEN][], char ninety[NINETY][], char hundred[], char thousand[THOUSAND][])
{
	int	i;
	int	first;
	int	all_zero;
	int	n;

	i = 0;
	all_zero = 1;
	while (i < len)
	{
		if (blocks[i] != 0)
			all_zero = 0;
		i++;
	}
	if (all_zero)
	{
		if (is_empty(zero))
			return (-1);
		ft_putstr(zero);
		return (0);
	}
	first = 1;
	i = len - 1;
	while (i >= 0)
	{
		n = blocks[i];
		if (n != 0)
		{
			if (!first)
				ft_putchar(' ');
			if (print_0_999(n, nineteen, ninety, hundred) < 0)
				return (-1);
			if (i > 0)
			{
				if (is_empty(thousand[i - 1]))
					return (-1);
				ft_putchar(' ');
				ft_putstr(thousand[i - 1]);
			}
			first = 0;
		}
		i--;
	}
	return (0);
}