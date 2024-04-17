def products_by_cat_dict(products):
    products_by_cat = {}
    for i in products:
        if not i.brand_name in products_by_cat:
            products_by_cat[i.brand_name] = {
                i.category: {
                    i.product_group: [i]
                }
            }
        else:
            if not i.category in products_by_cat[i.brand_name]:
                products_by_cat[i.brand_name][i.category] = {i.product_group: [i]}
            else:
                if not i.product_group in products_by_cat[i.brand_name][i.category]:
                    products_by_cat[i.brand_name][i.category][i.product_group] = [i]
                else:
                    products_by_cat[i.brand_name][i.category][i.product_group].append(i)
    return products_by_cat


def products_table_lst(prod_dict):
    result = []
    for brand_name in prod_dict:
        result.append({'brand_name': brand_name})
        for category in prod_dict[brand_name]:
            result.append({'category': category})
            for product_group in prod_dict[brand_name][category]:
                result.append({'product_group': product_group})
                result.append(prod_dict[brand_name][category][product_group])
    return result
