import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from . import metrics


@login_required(login_url='login')  # para function based views
def home(request):
    # product_metrics = {
    #     'total_cost_price': 500000,
    #     'total_selling_price': 1500000,
    #     'total_quantity': 5000,
    #     'total_profit': 1000000,
    # } esse era o código para ver com funciona

    product_metrics = metrics.get_products_metrics()
    sales_metrics = metrics.get_sales_metrics()
    daily_sales_data = metrics.get_daily_sales_data()
    daily_sales_quantity_data = metrics.get_daily_sales_quantity_data()
    graphic_product_category_metric = metrics.get_graphic_product_category_metric()
    graphic_product_brand_metric = metrics.get_graphic_product_brand_metric()

    context = {
        'product_metrics': product_metrics,
        'sales_metrics': sales_metrics,
        'daily_sales_data': json.dumps(daily_sales_data),  # trnsforma em json
        'daily_sales_quantity_data': json.dumps(daily_sales_quantity_data),
        'product_count_by_category': json.dumps(graphic_product_category_metric),
        'product_count_by_brand': json.dumps(graphic_product_brand_metric),
    }
    return render(request, 'home.html', context)
