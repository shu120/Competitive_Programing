/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   checker.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: shukondo <shukondo@student.42tokyo.jp>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/17 16:13:20 by shukondo          #+#    #+#             */
/*   Updated: 2025/08/17 16:20:32 by shukondo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int check_duplicates(int grid[4][4], int row, int col);
int validate_left(const int grid[4][4], const int consts[16], int row);
int validate_right(const int grid[4][4], const int consts[16], int row);
int validate_top(const int grid[4][4], const int consts[16], int col);
int validate_bottom(const int grid[4][4], const int consts[16], int col);

int    checker(const int grid[4][4], const int consts[16], int row, int col)
{
    if (grid[row][col] == 0)
        return (1);
    if (!check_duplicates(grid, row, col))
        return (0);
    if (!validate_left(grid, consts, row))
        return (0);
    if (!validate_right(grid, consts, row))
        return (0);
    if (!validate_top(grid, consts, col))
        return (0);
    if (!validate_bottom(grid, consts, col))
        return (0);
    return (1);
}