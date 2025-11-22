/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   judgement.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: shukondo <shukondo@student.42tokyo.jp>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/17 16:09:19 by shukondo          #+#    #+#             */
/*   Updated: 2025/08/17 16:20:31 by shukondo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int    validate_bottom(const int grid[4][4], const int consts[16], int col)
{
    int    i;
    int    reversed_line[4];

    i = 0;
    while (i < 4)
    {
        if (grid[i][col] == 0)
            return (1);
        reversed_line[3 - i] = grid[i][col];
        i++;
    }
    if (count_visible_boxes(reversed_line) != consts[4 + col])
        return (0);
    return (1);
}

int    validate_left(const int grid[4][4], const int consts[16], int row)
{
    int    i;
    int    line[4];

    i = 0;
    while (i < 4)
    {
        if (grid[row][i] == 0)
            return (1);
        line[i] = grid[row][i];
        i++;
    }
    if (count_visible_boxes(line) != consts[8 + row])
        return (0);
    return (1);
}

int    validate_right(const int grid[4][4], const int consts[16], int row)
{
    int    i;
    int    reversed_line[4];

    i = 0;
    while (i < 4)
    {
        if (grid[row][i] == 0)
            return (1);
        reversed_line[3 - i] = grid[row][i];
        i++;
    }
    if (count_visible_boxes(reversed_line) != consts[12 + row])
        return (0);
    return (1);
}

int    validate_top(const int grid[4][4], const int consts[16], int col)
{
    int    i;
    int    line[4];

    i = 0;
    while (i < 4)
    {
        if (grid[i][col] == 0)
            return (1);
        line[i] = grid[i][col];
        i++;
    }
    if (count_visible_boxes(line) != consts[0 + col])
        return (0);
    return (1);
}