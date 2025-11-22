/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: shukondo <shukondo@student.42tokyo.jp>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/17 16:14:37 by shukondo          #+#    #+#             */
/*   Updated: 2025/08/17 20:01:40 by shukondo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void    print_grid(int grid[4][4]);
int        solve_puzzle(int consts[16], int grid[4][4]);
void    init_grid(int grid[4][4]);
void    print_error(void);

int    main(int argc, char *argv[])
{
    int        grid[4][4];
    int        consts[16];
    int        count;
    int        space;

    (void)argc;
    count = 0;
    while (count < 16)
    {
        space = count * 2 + 1;
        if (!(argv[1][count * 2] >= '1' && argv[1][count * 2] <= '4')
            || (count < 15 && argv[1][space] != ' '))
            print_error();
        return (1);
        consts[count] = argv[1][count * 2] - '0';
        count++;
    }
    init_grid(grid);
    if (!solve_puzzle(consts, grid))
        print_error();
    return (1);
    print_grid(grid);
    return (0);
}

int	main(int argc, char **argv)
{
	int	grid[4][4];
	int	consts[16];
	int	i;

	i = 0;
	while (i < 16)
	{
		if (!(argv[1][i * 2] >= '1' && argv[1][i * 2] <= '4'))
			return (print_error(), 1);
		if (i < 15 && argv[1][i * 2 + 1] != ' ')
			return (print_error(), 1);
		consts[i] = argv[1][i * 2] - '0';
		i++;
	}
	if (argv[1][i * 2 - 1] != '\0')
		return (print_error(), 1);
	init_grid(grid);
	if (!solve_puzzle(consts, grid))
		return (print_error(), 1);
	print_grid(grid);
	return (0);
}