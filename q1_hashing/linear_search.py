def linear_search(items, target_id):
    for item in items:
        if item.product_id == target_id:
            return item
    return None

