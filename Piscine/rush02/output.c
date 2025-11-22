/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   output.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: kondoshuji <kondoshuji@student.42.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/23 17:08:00 by kondoshuji        #+#    #+#             */
/*   Updated: 2025/08/23 18:23:30 by kondoshuji       ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

#define NINETEEN 19
#define NINETY   8
#define THOUSAND 13


/**
 * @brief Structure to store string representations
 */
typedef struct s_dict
{
	/** @brief A standalone string storing the representation of 0 */
	char    *zero;
	/** @brief A two-dimensional array storing string representations
				of numbers 1 to 19 */
	char    *nineteen[NINETEEN];
	/** @brief A two-dimensional array storing string representations
				of numbers 20 to 90 */
	char    *ninety[NINETY];
	/** @brief A standalone string storing the representation of 100 */
	char    *hundred;
	/** @brief A two-dimensional array storing string representations
				of numbers 1000 or more*/
	char    *thousand[THOUSAND];
}            t_dict;
#endif

/**
 * @brief  1文字を標準出力に書き込む
 *
 * @param[in] c 出力する文字
 */

static void	ft_putchar(char c)
{
	write(1, &c, 1);
}

/**
 * @brief  文字列を標準出力に書き込む
 *
 * @param[in] s 出力する文字列('\0'まで)
 */

static void	ft_putstr(const char *s)
{
	while (*s != '\0')
	{
		write(1, s, 1);
		s++;
	}
}

/**
 * @brief  文字列がNULLまたは空かを判定する
 *
 * @param[in] s 判定するべき文字列
 * @retval 1 NULLまたは空
 * @retval 0 それ以外
 */

static int	is_empty(const char *s)
{
	if (!s)
		return (1);
	if (*s == '\0')
		return (1);
	return (0);
}

/**
 * @brief  0-99の数値を英単語に変換して出力する。
 *
 * @param[in] n 変換対象の整数
 *
 * @retval 
 * 0  正常終了
 * -1 辞書に必要な語が存在しない場合。
 *
 * @note 辞書不足のときは何も出力せず-1を返す
 */
 
static int	print_0_99(int n, char nineteen[NINETEEN][], char ninety[NINETY][])
{
	const char	*u;
	const char	*t;

	if (n == 0)
		return (0);
	if (n <= 19)
	{
		u = nineteen[n - 1];
		if (is_empty(u))
			return (-1);
		ft_putstr(u);
		return (0);
	}
	t = ninety[(n / 10) - 2];
	if (is_empty(t))
		return (-1);
	ft_putstr(t);
	if (n % 10)
	{
		ft_putchar(' ');
		u = nineteen[(n % 10) - 1];
		if (is_empty(u))
			return (-1);
		ft_putstr(u);
	}
	return (0);
}

/**
 * @brief 0-999の数値を英単語に変換して出力する
 *
 * @param[in] n 変換対象の整数
 *
 * @retval
 * 0  正常終了
 * -1 辞書に必要な語が存在しない場合
 *
 * @note 100 以上のときは「◯ hundred …」を構成し、残りを print_0_99() で処理する。
 */

static int	print_0_999(int n, char nineteen[NINETEEN][], char ninety[NINETY][], char hundred[])
{
	int			h;
	const char	*u;

	if (n == 0)
		return (0);
	if (n >= 100)
	{
		h = n / 100;
		u = nineteen[h - 1];
		if (is_empty(u) || is_empty(hundred))
			return (-1);
		ft_putstr(u);
		ft_putchar(' ');
		ft_putstr(hundred);
		n = n % 100;
		if (n)
			ft_putchar(' ');
	}
	if (n)
	{
		if (print_0_99(n, nineteen, ninety) < 0)
			return (-1);
	}
	return (0);
}
