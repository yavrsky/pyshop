from django.shortcuts import render
from orders.models import OrderItem


# def best_customers(request):
# 	customers = Order.objects.raw('''
# SELECT id, first_name, last_name, email, sum(total_price) as total_price
# from
# (SELECT 'orders_order'.id, first_name, last_name, email, sum(quantity*price) as total_price
# FROM 'orders_orderitem', 'orders_order'
# where 'orders_orderitem'.order_id = 'orders_order'.id
# group by order_id
# order by sum(quantity*price))
# group by email
# order by sum(total_price) desc
# ''')
# 	return render(request, 'customers/best_custom.html', {'customers':customers})


def best_customers(request):
	customers = OrderItem.objects.raw('''
SELECT id, name, quantity
FROM (	SELECT sum(quantity) as quantity, category_id
		FROM (	SELECT  product_id, sum(quantity) as quantity
				FROM 'orders_orderitem'
				GROUP BY product_id
				ORDER BY sum(quantity) desc) as '1', 'shop_product'
		WHERE 'shop_product'.id = '1'.product_id
		GROUP BY category_id
		ORDER BY sum(quantity) desc) as '2', 'shop_category'
WHERE '2'.category_id='shop_category'.id



''')
	return render(request, 'customers/best_custom.html', {'customers':customers})