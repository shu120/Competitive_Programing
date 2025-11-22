/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: shukondo <shukondo@student.42tokyo.jp>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/16 14:40:19 by shukondo          #+#    #+#             */
/*   Updated: 2025/08/17 14:45:43 by shukondo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

/*バックトラック*/
int solve_puzzle(const int consts[16], int grid[4][4])
{
	int cell = 0;

	while (cell>= 0 && cell < 16)
	{
		int row = cell / 4;
		int col = cell % 4;/*マス目を二次元配列にする*/

		/* このマスに置く数字を順に試す */
		grid[row][col]++;

		if (grid[row][col] > 4)
		{
			grid[row][col] = 0;/*リセット*/
			cell--;/*ひとつ戻る*/
			continue;
		}

	}
	return (cell == 16);/*成功*/
}

int	main(void)
{
	const int consts[16] = {};
	int grid[4][4] = {{0}};

	if (!solve_puzzle(consts, grid))
	{
		write(1, "Error", 5);
		return 1;
	}
	/* print_grid(grid);  // 解ありなら出力 */
	return 0;
}

int	judge(int grid[4][4], const int consts[16], int row, int col)
{
	int	i, j, max, seen;
	int	val;

	val = grid[row][col];
	if (val == 0)
		return (1);

	/*重複*/
	i = 0;
	while (i < 4)
	{
		if (i != col && grid[row][i] == val)
			return (0);
		i++;
	}
	i = 0;
	while (i < 4)
	{
		if (i != row && grid[i][col] == val)
			return (0);
		i++;
	}

	/*左右のヒントを参照して判断*/
	i = 0;
	while (i < 4 && grid[row][i] != 0)
		i++;
	if (i == 4)
	{
		/*左から*/
		j = 0; max = 0; seen = 0;
		while (j < 4)
		{
			if (grid[row][j] > max)
			{
				max = grid[row][j];
				seen++;
			}
			j++;
		}
		if (seen != consts[8 + row])
			return (0);

		/*右から*/
		j = 3; max = 0; seen = 0;
		while (j >= 0)
		{
			if (grid[row][j] > max)
			{
				max = grid[row][j];
				seen++;
			}
			j--;
		}
		if (seen != consts[12 + row])
			return (0);
	}

	/*上下のヒントを参照して判断*/
	i = 0;
	while (i < 4 && grid[i][col] != 0)
		i++;
	if (i == 4)
	{
		/* 上から */
		j = 0; max = 0; seen = 0;
		while (j < 4)
		{
			if (grid[j][col] > max)
			{
				max = grid[j][col];
				seen++;
			}
			j++;
		}
		if (seen != consts[0 + col])
			return (0);

		/* 下から */
		j = 3; max = 0; seen = 0;
		while (j >= 0)
		{
			if (grid[j][col] > max)
			{
				max = grid[j][col];
				seen++;
			}
			j--;
		}
		if (seen != consts[4 + col])
			return (0);
	}
	return (1);
}
