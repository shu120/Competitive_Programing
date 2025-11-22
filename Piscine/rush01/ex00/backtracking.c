/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   backtracking.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: shukondo <shukondo@student.42tokyo.jp>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/17 15:00:31 by shukondo          #+#    #+#             */
/*   Updated: 2025/08/17 15:03:26 by shukondo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	solve_puzzle(const int consts[16], int grid[4][4])
{
	int	cell;
	int	row;
	int	col;

	cell = 0;
	while (cell >= 0 && cell < 16)
	{
		row = cell / 4;
		col = cell % 4;

		/*順に試す*/
		grid[row][col]++;

		/*全てがNGなら、空に戻してひとつ前にバックトラック*/
		if (grid[row][col] > 4)
		{
			grid[row][col] = 0;
			cell--;
			continue;
		}

		/*置いた値が妥当なら次のマスへ。NGなら同じマスで次の値を試す*/
		if (judge(grid, consts, row, col))
		{
			cell++;
		}
	}
	return (cell == 16);
}
