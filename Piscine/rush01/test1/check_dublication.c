/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   check_dublication.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: shukondo <shukondo@student.42tokyo.jp>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/17 16:12:52 by shukondo          #+#    #+#             */
/*   Updated: 2025/08/17 16:24:55 by shukondo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int    check_duplicates(const int grid[4][4], int row, int col)
{
    int    i;
    int    val;

    val = grid[row][col];
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
    return (1);
}