/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   print_grid.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: shukondo <shukondo@student.42tokyo.jp>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/17 16:11:50 by shukondo          #+#    #+#             */
/*   Updated: 2025/08/17 16:23:09 by shukondo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void    print_grid(int grid[4][4])
{
    int col;
    int row;
    char c;

    col = 0;
    row = 0;
    while (row < 4)
    {
        while (col < 4)
        {
            c = grid[row][col] + '0';
            write(1, &c, 1);
            if (col < 3)
            {
                write(1, " ", 1);
            }
            col++;
        }
        write(1, "\n", 1);
        col = 0;
        row++;
    }
}

// int    main(void)
// {
//     static int    grid[4][4] = {{1, 2, 3, 4}, {2, 3, 4, 1}, {3, 4, 1, 2}, {4, 1, 2, 3}};
//     print_grid(grid);
//     return (0);
// }