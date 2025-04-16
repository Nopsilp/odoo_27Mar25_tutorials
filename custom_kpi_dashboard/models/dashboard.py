from odoo import models, fields, api, _
import logging


_logger = logging.getLogger(__name__)


class KpiDashboard (models.Model):
    _name = 'kpi.dashboard'
    _description = 'KPI Dashboard'

    total_sales = fields.Float(string='Total Sales', readonly=True)
    total_orders = fields.Integer(string='Total Orders', readonly=True)
    total_available_stock = fields.Float(string='Total Available Stock', readonly=True)

    def compute_dashboard_kpis(self):
        """ Compute total_sales, total_orders, & total_available_stock """
        _logger.info("Starting KPI Computation...")
        
        total_sale_orders = self.env['sale.order'].search([('state', '=', 'sale')])
        total_sales = sum(total_sale_orders.mapped('amount_total'))

        _logger.info("Computing Total Orders...")
        total_orders = self.env['sale.order'].search_count(['state', '=', 'sale'])

        total_products = self.env['product.product'].search([])
        product_quantities = total_products._compute_quantities_dict(None, None, None)
        total_available_stock = sum(quantity_available.get('qty_available', 0) for quantity_available in product_quantities.values())

        _logger.info("Returning KPI Values...")
        return {
            'total_sales': total_sales,
            'total_orders': total_orders,
            'total_available_stock': total_available_stock,
        }


    def action_refresh_kpi_dashboard(self):
        """ Manually refresh KPI dashboard """
        try:
            kpi_values = self.compute_dashboard_kpis()  
            
            #  check if there's any record in 'kpi.dashboard' Model
            kpi_dashboard_record = self.search([])
            
            if kpi_dashboard_record:
                kpi_dashboard_record.write(kpi_values)
            else:
                self.create(kpi_values)

            _logger.info(
                f"KPI Dashboard Updated - Sales: {kpi_values['total_sales']}, "
                f"Orders: {kpi_values['total_orders']}, "
                f"Stock: {kpi_values['total_available_stock']}"
                )

        except KeyError as e:
            _logger.error(f"KeyError in KPI update: {e}")
        except Exception as e:
            _logger.error(f"Unexpected error: {e}")


    
