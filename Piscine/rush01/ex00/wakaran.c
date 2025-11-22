#include <unistd.h>

/* ---------- 出力 ---------- */
void	print_grid(int grid[4][4])
{
	int		r;
	int		c;
	char	buf[2];

	r = 0;
	while (r < 4)
	{
		c = 0;
		while (c < 4)
		{
			buf[0] = '0' + grid[r][c];
			buf[1] = (c == 3) ? '\n' : ' ';
			write(1, buf, 2);
			c++;
		}
		r++;
	}
}

/* ---------- 入力パース（厳格：数字16個＋間に1スペース）---------- */
int	parse_strict16(const char *s, int out[16])
{
	int		i;
	int		pos;
	char	d;

	i = 0;
	while (i < 16)
	{
		pos = i * 2;
		d = s[pos];
		if (!(d >= '1' && d <= '4'))
			return (0);
		out[i] = d - '0';
		if (i < 15)
		{
			if (s[pos + 1] != ' ')
				return (0);
		}
		else
		{
			if (s[pos + 1] != '\0')
				return (0);
		}
		i++;
	}
	return (1);
}

/* ---------- 可視数カウント（左→右の最大更新回数） ---------- */
int	count_visible4(const int a[4])
{
	int	i;
	int	max;
	int	seen;

	i = 0;
	max = 0;
	seen = 0;
	while (i < 4)
	{
		if (a[i] > max)
		{
			max = a[i];
			seen++;
		}
		i++;
	}
	return (seen);
}

/* ---------- 重複チェック ---------- */
int	check_duplicates(const int grid[4][4], int row, int col)
{
	int	i;
	int	val;

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

/* ---------- 左右・上下ヒントチェック（未完成ならスルー） ---------- */
int	validate_left(const int grid[4][4], const int consts[16], int row)
{
	int	i;
	int	line[4];

	i = 0;
	while (i < 4)
	{
		if (grid[row][i] == 0)
			return (1);
		line[i] = grid[row][i];
		i++;
	}
	if (count_visible4(line) != consts[8 + row])
		return (0);
	return (1);
}

int	validate_right(const int grid[4][4], const int consts[16], int row)
{
	int	i;
	int	rev[4];

	i = 0;
	while (i < 4)
	{
		if (grid[row][i] == 0)
			return (1);
		rev[3 - i] = grid[row][i];
		i++;
	}
	if (count_visible4(rev) != consts[12 + row])
		return (0);
	return (1);
}

int	validate_top(const int grid[4][4], const int consts[16], int col)
{
	int	i;
	int	line[4];

	i = 0;
	while (i < 4)
	{
		if (grid[i][col] == 0)
			return (1);
		line[i] = grid[i][col];
		i++;
	}
	if (count_visible4(line) != consts[col])
		return (0);
	return (1);
}

int	validate_bottom(const int grid[4][4], const int consts[16], int col)
{
	int	i;
	int	rev[4];

	i = 0;
	while (i < 4)
	{
		if (grid[i][col] == 0)
			return (1);
		rev[3 - i] = grid[i][col];
		i++;
	}
	if (count_visible4(rev) != consts[4 + col])
		return (0);
	return (1);
}

/* ---------- judge：置いた直後の1マスが妥当か ---------- */
int	judge(const int grid[4][4], const int consts[16], int row, int col)
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

/* ---------- バックトラック（whileのみ） ---------- */
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
		grid[row][col]++; /* 1→2→3→4 */

		if (grid[row][col] > 4)
		{
			grid[row][col] = 0;
			cell--;
			continue;
		}
		if (judge(grid, consts, row, col))
			cell++;
	}
	return (cell == 16);
}

/* ---------- main ---------- */
int	main(int argc, char **argv)
{
	int	grid[4][4];
	int	consts[16];
	int	r;
	int	c;

	/* 0で初期化 */
	r = 0;
	while (r < 4)
	{
		c = 0;
		while (c < 4)
		{
			grid[r][c] = 0;
			c++;
		}
		r++;
	}
	/* 引数パース */
	if (argc != 2 || !parse_strict16(argv[1], consts))
	{
		write(1, "Error\n", 6);
		return (1);
	}
	/* 解く→出力 or Error */
	if (!solve_puzzle(consts, grid))
	{
		write(1, "Error\n", 6);
		return (1);
	}
	print_grid(grid);
	return (0);
}
