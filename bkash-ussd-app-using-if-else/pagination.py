# box-sizing: border-box;//content er moddhe padding r boarder dhore,(except margin)
def paginate(items, page_size, page_number):
    """
    Paginates a list of items.

    Args:
        items (list): The list of items to paginate.
        page_size (int): The number of items per page.
        page_number (int): The page number to retrieve.

    Returns:
        list: The items for the specified page.
    """
    start_index = (page_number - 1) * page_size
    end_index = start_index + page_size
    return items[start_index:end_index]

# Example usage
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
page_size = 3
page_number = 2

result = paginate(items, page_size, page_number)
print(result)  # Output: [4, 5, 6]
