/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   validate_required.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: kondoshuji <kondoshuji@student.42.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/24 22:34:47 by kondoshuji        #+#    #+#             */
/*   Updated: 2025/08/24 22:36:38 by kondoshuji       ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./rush02.h"

/**
 * @brief Checks whether all required entries are present in the dictionary.
 *
 * @retval 
 * 1  All entries are present.
 * 0  Some entries are missing (Dict Error).
 *
 */
 
int	validate_required(const t_dict *d)
{
	int	i;

	if (!d || is_empty(d->zero))
		return (0);
	i = 0;
	while (i < NINETEEN)
	{
		if (is_empty(d->nineteen[i]))
			return (0);
		i++;
	}
	i = 0;
	while (i < NINETY)
	{
		if (is_empty(d->ninety[i]))
			return (0);
		i++;
	}
	if (is_empty(d->hundred))
		return (0);
	if (is_empty(d->thousand[0]))
		return (0);
	return (1);
}
