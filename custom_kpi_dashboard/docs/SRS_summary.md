# Goals: KPI Dashboard Display:  
    - Total Sales (sum of confirmed sales)
    - Total Orders (count of confirmed sales)
    - Total Available Stock (total quantity of all products).

Model: 'sale.order' for Total Sales & Total Orders and  'product.product' for Total Available Stock
Related Fields:
    - Total Sales (sum of confirmed sales)
        * 'state' in 'sale.order' to pull only 'sale' state order
        * 'amount_total' in each record in 'sale.order'
    - Total Orders (count of confirmed sales)
        * 'state' in 'sale.order' to pull only 'sale' state order
    - Total Available Stock (total quantity of all products).
        * n/a because we use recordset._compute_quantities_dict()

*V.1 Pseudocode (written by myself):*
    - CREATE 3 fields in a class inherited from (models.Model)
        * Total Sales (sum of confirmed sales)
        * Total Orders (count of confirmed sales)
        * Total Available Stock (total quantity of all products).   
    - CREATE a method named 'action_refresh_dashboard(self)' in the class
    - Deal with Total Sales (sum of confirmed sales)  
        sale_order_model = Access Odoo Model 'sale.order'
        confirmed_sales_orders = sale_order_model.search([('state', '=', 'sale')])
        sales_amounts = confirmed_sales_orders.mapped('amount_total')
    - Deal with Total Orders (count of confirmed sales)
        count_confirmed_sales_orders = sale_order_model.search_count(['state', '=', 'sale'])
    - Deal with Total Available Stock (total quantity of all products)
        product_model = Access Odoo Model 'product.product'
        all_products = product_model.search([])
        product_quantities = all_products._compute_quantities_dict(None, None, None, False, False)
        total_available_stock = 0
        FOR each product_id IN product_quantities:
            quantity_data = product_quantities[product_id]
            available_quantity = quantity_data.get('qty_available', 0) // Use .get to prevent KeyError if 'qty_available' is missing
            total_stock = total_stock + available_quantity
    - FOR LOOP record in self
        - IF record is False (no record)
            CREATE a variable named 'new_record' = {
                total_sales = SUM of sales_amounts
                total_orders = count_confirmed_sales_orders
                total_available_stock = total_stock 
            } 
            CREATE  self.env['the_class'].create(new_record)       
        - ELSE WRITE
            record.total_sales = SUM of sales_amounts
            record.total_orders = count_confirmed_sales_orders
            record.total_stock = total_available_stock

V.2 Pseudocode (improved by Copilot):

DEFINE class KPI_Dashboard (inherit models.Model)
    CREATE 3 fields:
        total_sales → Sum of confirmed sales
        total_orders → Count of confirmed sales
        total_available_stock → Total quantity of all products

    CREATE Method: compute_dashboard_kpis(self) -> dict
        # Fetch Total Sales & Total Orders
        ACCESS 'sale.order' Model
        SEARCH confirmed orders where state = 'sale'
        SUM total_sales -> SUM of 'amount_total' from confirmed orders
        COUNT total_orders -> 'sale.order' Model.search_count()
        
        # Fetch Total Available Stock
        ACCESS 'product.product' Model
        SEARCH all products
        COMPUTE product quantities using `_compute_quantities_dict()`
        SUM all 'qty_available' → total_available_stock
        
        RETURN calculated KPI values in dictionary

    Method: action_refresh_kpi_dashboard(self)
        kpi_values = CALL compute_dashboard_kpis()
        
        SEARCH existing dashboard record
        IF record exists THEN:
            UPDATE fields with calculated values
        ELSE:
            CREATE new record with calculated values
       
        # LOG updated values for tracking
        LOG "Dashboard Updated - Sales:", total_sales
        LOG "Dashboard Updated - Orders:", total_orders
        LOG "Dashboard Updated - Stock:", total_available_stock


V.3 Pseudocode -> near real code (improved by myself):
class KpiDashboard (models):
    _name = kpi.dashboard
    _description = 'KPI Dashboard'

    total_sales = fields.Float(string='Total Sales')
    total_orders = fields.Integer(string='Total Orders')
    total_available_stock = fields.Float(string='Total Available Stock')

    def compute_dashboard_kpis(self):
        total_sale_orders = self.env['sale.order'].search([('state', '=', 'sale')])
        total_sales = sum(total_sale_orders.mapped('amount_total'))
        total_orders = total_sale_orders.search_count()

        total_products = self.env['product.product'].search([])
        product_quantities = total_products._compute_quantities_dict(None, None, None)
        total_available_stock = product_quantities.mapped('qty_available'))

        return {
            'Total Sales' = total_sales,
            'Total Orders' = total_orders,
            'Total Available Stock' = total_available_stock,
        }

---

## Goal: Pull Total Sales (sum of confirmed sales) to display to the users
Model: 'sale.order'
Related Fields: 
    * 'state' in 'sale.order' to pull only 'sale' state order
    * 'amount_total' in each record in 'sale.order'
How: 
    * access 'sale.order' by self.env['sale.order']
    * search(['state', '=', 'sale'])
    * mapped(result.amount_total)
    * sum(mapped(result.amount_total))

Goal: Pull Total Sales (sum of confirmed sales)

    1. Access the 'sale.order' Model
sale_order_model = Access Odoo Model 'sale.order'

    2. Search for sale orders with the state 'sale' (confirmed)
confirmed_sales_orders = sale_order_model.search([('state', '=', 'sale')])

    3. Extract the 'amount_total' from each confirmed sales order
sales_amounts = confirmed_sales_orders.mapped('amount_total')

    4. Calculate the sum of the extracted sales amounts
total_sales = SUM of sales_amounts

    5. Display the Total Sales
DISPLAY total_sales

Code:
    # Access 'sale.order' Model
    sale_order_model = self.env['sale.order']

    # Search for confirmed sale orders ('state' = 'sale')
    confirmed_sales_orders = sale_order_model.search([('state', '=', 'sale')])

    # Extract 'amount_total' from each confirmed sales order
    sales_amounts = confirmed_sales_orders.mapped('amount_total')

    # Calculate the sum of the extracted sales amounts
    total_sales = sum(sales_amounts)

    # Display the Total Sales
    self.total_sales_display = total_sales  # สมมติว่ามี field `total_sales_display` ใน model
    _logger.info(f"Total Confirmed Sales: {total_sales}")  # หรือแสดงผ่าน log

OR 
    sales_orders = sum(self.env['sale.order'].search([('state', '=', 'sale')]).mapped('amount_total'))

---


*Goal: Pull Total Orders (count of confirmed sales) to display to the users*
Model: 'sale.order'
Related Fields: 
    * 'state' in 'sale.order' to pull only 'sale' state order
How: 
    * access 'sale.order' by self.env['sale.order']
    * search_count(['state', '=', 'sale'])
Code:  self.env["sale.order"].search_count([("state", "=", "sale")])

---


*Goal: Pull Total Available Stock (total quantity of all products) to display to the users*
Model: 'product.product'
Related Fields: n/a
How: 
    * access 'product.product' by self.env['product.product']
    * search([]) 
    * recordset._compute_quantities_dict()
    * for loop each record for qty_available
    * Sum the result
Pseudocode:

// Goal: Pull Total Available Stock (total quantity of all products)

// 1. Access the 'product.product' Model
product_model = Access Odoo Model 'product.product'

// 2. Search for all products
all_products = product_model.search([])

// 3. Call _compute_quantities_dict on the recordset of all products
//    This function requires parameters: lot_id, owner_id, package_id, from_date, to_date
//    Since we want the total across all, without specific filters, we pass None or False
product_quantities = all_products._compute_quantities_dict(None, None, None, False, False)

// 4. Loop through the results and sum qty_available
total_available_stock = 0
FOR each product_id IN product_quantities:
    quantity_data = product_quantities[product_id]
    available_quantity = quantity_data.get('qty_available', 0) // Use .get to prevent KeyError if 'qty_available' is missing
    total_available_stock = total_available_stock + available_quantity

// 5. Display the Total Available Stock
DISPLAY total_available_stock

---

