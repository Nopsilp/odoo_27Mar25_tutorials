# Software Requirements Specification (SRS)
**Project Name:** Sales & Inventory KPI Dashboard
**Version:** 18.0.1.0.0
**Date:** April 10, 2025
**Prepared By:** Nop_BKK (with Gemini's & ChatGPT's assistance)


## 1. Introduction


### 1.1 Purpose

* **Identification of the System:** Sales & Inventory KPI Dashboard
* **Primary Goal of the Document:** Outlines the software requirements for the Sales & Inventory KPI Dashboard.
* **Core Functionality of the System (High-Level):** Provides users with a clear and real-time overview of key performance indicators related to sales (total sales, total orders) and inventory (total available stock), along with the ability to manually refresh this data for the most up-to-date insights.
* **Intended Benefit:** It enables users to quickly monitor business performance and make informed decisions.


### 1.2 Scope

**Key features Included:** 
    - Display of Key Sales and Stock Metrics
    - Near Real-time Data Updates and Manual Refresh Capability
    - Easy Access via Odoo Reporting Menu
    
**The following are explicitly OUT OF SCOPE for this initial phase:**

    - Displaying KPIs for specific time periods (e.g., monthly, quarterly).
    - Data visualization using charts or graphs.
    - Inclusion of additional KPIs beyond total sales, orders, and stock.
    - Automated data refresh mechanisms.
    - Drill-down capabilities to view underlying data.
    - User customization of the dashboard layout or displayed KPIs.


### 1.3 Intended Audience

This document is intended for the following stakeholders:
* **Developers:** To understand the technical requirements for building the module.
* **Testers:** To create test cases and verify the functionality of the module.
* **Users:** To understand the features and functionality of the KPI Dashboard.
* **Project Manager:** To track the progress and ensure the project stays within scope.


### 1.4 References

* Odoo 18.0 Documentation
* Python Programming Language
* XML Specification


### 1.5 Definitions, Acronyms, and Abbreviations

* KPI – Key Performance Indicator.
* Odoo ORM – Object Relational Mapping system used in Odoo for handling database operations.
* SCSS – Sassy CSS, used for styling frontend components.


## 2. Overall Description


### 2.1 Product Perspective

* **Product's Environment:** Sales & Inventory KPI Dashboard will be implemented as a custom module within the existing Odoo 18.0 environment. 
* **User's Accessibility:** It will be accessible through the Odoo web interface as a new menu item under the "Reporting" menu.
* **Relationship to Other Products:** It will leverage Odoo's ORM (Object-Relational Mapping) to access and process data from other Odoo modules, specifically `sale.order` and `product.product`. 

### 2.2 Product Functions

    - KPI Dashboard Display:  
        - Total Sales (sum of confirmed sales)
        - Total Orders (count of confirmed sales)
        - Total Available Stock (total quantity of all products).
    - Near Real-time Data Updates and Manual Refresh Capability
        - Displays KPI data with near real-time updates.
        - Provides a user interface for manual refresh of KPI values.
    - Easy Access via Odoo Reporting Menu
        - The KPI Dashboard is accessible through a dedicated "KPI Dashboard" menu item under Odoo's "Reporting" menu.

### 2.3 User Classes and Characteristics

* **CEO (Chief Executive Officer):**
    * **Business Acumen:** High. Highly familiar with KPIs and business metrics.
    * **Usage Frequency:** Low to Medium. Often focusing on trends and overall performance rather than granular details.
    * **Data Requirements:** Primarily interested in summarized and high-level data, potentially visualized through charts and trend lines .
    * **Technical Expertise:** Medium to High. Likely comfortable with dashboards and data visualization tools, expecting intuitive interfaces and the ability to quickly grasp key insights.
    * **Pain Points:**
        *  Struggles with getting a high-level business overview without digging through multiple reports.
        *  Needs quick insights to make strategic decisions but often gets buried in excessive details.
        *  Lacks real-time visibility into overall company sales trends and inventory efficiency.
    * **Use Case:**
        * The CEO logs into Odoo and accesses the KPI Dashboard under "Reporting."
        * Views Total Sales, Total Orders, and Total Stock instantly in a visually clear format.
        * Uses high-level KPI insights to decide whether to adjust pricing strategies or expand stock availability.

* **Sales Managers:**
    * **Business Acumen:** High. Very familiar with sales-related KPIs.
    * **Usage Frequency:** Medium to High. Sales Managers will likely use the dashboard regularly to monitor team performance against targets, track order volumes, and identify sales trends.
    * **Data Requirements:** Require detailed sales data, including total sales, order counts, and potentially breakdowns by sales team, region, or product category. May benefit from tabular views for detailed analysis and comparisons, as well as charts showing sales trends over time.
    * **Technical Expertise:** Medium. Generally comfortable with dashboards and data analysis tools, needing clear and actionable information to manage their teams and drive sales.
    * **Pain Points:**
        * Hard to track team sales performance efficiently without a centralized view.
        * Needs detailed sales breakdowns but manual reporting takes too much time.
        * No quick way to identify low-performing sales periods or peak trends.
    * **Use Case:**
        * The Sales Manager checks the KPI Dashboard daily to monitor total revenue and order count.
        * Uses manual refresh to update KPIs in real time.
        * Identifies that sales dropped compared to last month and adjusts team targets accordingly.

* **Inventory Managers:**
    * **Business Acumen:** Medium to High. Inventory Managers understand stock levels, supply chains, and the impact of inventory on operational efficiency and costs. They are highly familiar with inventory-related metrics.
    * **Usage Frequency:** Medium to High. Inventory Managers will use the dashboard frequently to monitor total stock levels, identify potential stockouts or overstock situations, and ensure optimal inventory management.
    * **Data Requirements:** Primarily interested in total stock levels, potentially broken down by product category or location. May benefit from tabular views showing current quantities and thresholds, as well as visualizations highlighting low-stock items.
    * **Technical Expertise:** Medium. Comfortable with dashboards, needing clear data on inventory levels to make informed decisions about purchasing and stock management.
    * **Pain Points:**
        * Difficult to monitor stock levels and forecast shortages.
        * No instant visibility into which products are overstocked or about to run out.
        * Requires clear data but often has to sort through complex inventory spreadsheets.
    * **Use Case:**
        * The Inventory Manager checks Total Stock on the dashboard.
        * Notices that a high-demand product is running low and quickly requests replenishment.
        * Uses KPI insights to prevent overstocking slow-moving items, optimizing warehouse space.


### 2.4 Operating Environment

The module will operate within an Odoo 18.0 environment. The following are the key aspects of the operating environment:

    * **Software:**
        * Odoo Server: Version 18.0
        * Database: PostgreSQL (Version supported by Odoo 18.0)
        * Web Browser: Compatible with Odoo 18.0 (e.g., Google Chrome (latest stable), Mozilla Firefox (latest stable))
        * Python: Version supported by Odoo 18.0

    * **Hardware:**
        * Server: As per Odoo 18.0 recommended hardware specifications.
        * Client (for accessing via browser): Standard desktop or laptop computer capable of running a supported web browser.

    * **Network:**
        * Standard TCP/IP network connection between the client browser and the Odoo server.
        * Recommended network speed as per Odoo 18.0 recommendations for optimal performance.

    * **Other Dependencies:**
        * None specifically for this module beyond the core Odoo 18.0 installation and its dependencies.

### 2.5 Design and Implementation Constraints

#### 2.5.1 Technology Stack and Framework:

* **Odoo Framework:** The module **must** be developed as an Odoo module, leveraging the Odoo 18.0 framework. This includes adherence to Odoo's module structure, ORM (Object-Relational Mapping), and core APIs.
* **Programming Languages:**
    * **Python:** All server-side logic and module functionality **must** be implemented using Python, adhering to Odoo's Python coding conventions and best practices.
    * **XML:** All view definitions (Form, etc.), menu structures, and basic data loading **must** be defined using Odoo's XML format.
    * **QWeb:** Dynamic UI elements and more complex view rendering within the dashboard **may** utilize Odoo's QWeb templating engine.
    * **CSS (SCSS):** Styling of the dashboard elements **must** be done using standard CSS or Odoo's SCSS conventions for better maintainability and integration with Odoo's theme. The provided `dashboard.css` file should serve as the initial styling guideline.

#### 2.5.2 Data Handling:

* **Data Source:** All data required for the KPIs **must** be retrieved from existing Odoo data models, specifically:
    - `sale.order`: For fetching total sales and total order counts. 
        - The `state` field **must** be used to filter confirmed sales orders ('sale'). 
        = The `amount_total` field **must** be used for calculating total sales.
    = `product.product`: For fetching total available stock quantities, leveraging the `_compute_quantities_dict` method or relevant inventory management functions provided by Odoo. Direct SQL queries are **prohibited** unless explicitly approved and justified.
* **Data Integrity:** The module **must** ensure data integrity and accuracy when retrieving and calculating KPIs. Proper error handling and data validation mechanisms **should** be implemented where necessary.

#### 2.5.3 User Interface (UI) and User Experience (UX):

* **Consistent Odoo Look and Feel:** 
    - The dashboard's UI **must** strictly adhere to Odoo 18.0's standard UI/UX guidelines, including the use of Odoo's standard widget library (e.g., `oe_kanban_view`, `o_list_view`), button styles (`btn-primary`, `btn-secondary`), and form layout conventions. Any custom UI elements **must** be visually consistent with Odoo's native design.

* **Responsive Layout with Breakpoints:** The dashboard layout **must** be fully responsive, adapting seamlessly to the following screen width breakpoints:
    * **Desktop:** Minimum width of 1200 pixels.
    * **Tablet (Landscape):** Width between 992 and 1199 pixels.
    * **Tablet (Portrait):** Width between 768 and 991 pixels.
    * **Mobile:** Maximum width of 767 pixels.
    Standard Odoo responsiveness features and the underlying Bootstrap grid system **must** be utilized to achieve this.

* **Basic Accessibility Compliance (WCAG 2.1 AA):** The dashboard **should** aim to meet WCAG 2.1 Level AA guidelines where applicable within the Odoo framework. This includes:
    * Providing descriptive `alt` text for all visual elements (images, icons).
    * Ensuring sufficient color contrast (as defined in WCAG 2.1 AA) using the color palette from `dashboard.css`.
    * Making the dashboard navigable using the keyboard.

* **Clear and Concise KPI Presentation:** 
    - Each KPI **must** be presented with a clear label and its corresponding value. 
    - Refer to the "User Interface Requirements" section for specific visual representations (e.g., "Total Sales should be displayed using a large font size with the currency symbol and thousands separator"). 
    - The color palette defined in `dashboard.css` **must** be used consistently to visually differentiate KPIs and indicate status or trends as specified in the UI Requirements.

####  2.5.4 Security:

    * **Authentication:**
        * User authentication will leverage Odoo's standard user authentication mechanisms.
        * Secure session management will be enforced as per Odoo's default settings.

    * **Authorization:**
        * Access to the KPI Dashboard module and its views will be controlled through Odoo's security groups, initially granting access to users in the `base.group_user` group.
  
    * **Data Security:**
        * All data transmission between the user's browser and the Odoo server **must** occur over HTTPS.
        * Data at rest (in the database) will be secured by Odoo's standard database security measures. Encryption at rest may be considered in future phases if deemed necessary for the sensitivity of the underlying data.
        * Regular database backups will be performed as part of the overall Odoo system administration.

    * **Input Validation and Sanitization:**
        * Currently, the dashboard primarily displays data retrieved from existing Odoo models. If future enhancements introduce user input, appropriate validation and sanitization techniques will be implemented to prevent security vulnerabilities.

    * **Auditing and Logging:**
        * Access to the KPI Dashboard will be logged as part of Odoo's standard access logs. More detailed logging of specific actions (e.g., manual refresh) may be implemented if required for auditing purposes.

    * **Security Updates and Patch Management:**
        * The Odoo instance and the underlying operating system **must** be kept up-to-date with the latest security patches and updates.

#### 2.5.5 Maintainability and Scalability:

    This section outlines the considerations for ensuring the long-term maintainability and the ability of the Sales & Inventory KPI Dashboard module to scale with future growth.

    * **2.5.5.1 Maintainability:**
        * **Code Structure and Readability:**
            * All code will adhere to established Odoo Python and XML coding standards.
            * Comprehensive and clear comments will be included to explain code logic.
            * Meaningful and consistent naming conventions will be used throughout the codebase.
            * The module will be designed with a modular structure to facilitate easier updates and modifications.
        * **Ease of Debugging and Troubleshooting:**
            * Standard Odoo logging mechanisms will be utilized to record relevant events and potential errors.
            * Clear error handling will be implemented to provide informative feedback.
        * **Testability:**
            * Unit tests will be developed for key functional components of the module.
            * Integration tests will be performed to ensure proper interaction with other Odoo modules.
        * **Documentation:**
            * Developer-focused documentation outlining the module's architecture and key functionalities will be provided.

    * **2.5.5.2 Scalability:**
        * **Database Considerations:** Data retrieval queries will be optimized for performance. Appropriate indexing on relevant database fields will be considered.
        * **Performance Optimization:** Code will be written with efficiency in mind to handle increasing data volumes.
        * **(Future Consideration)** Asynchronous operations may be explored for data refresh processes if performance becomes a bottleneck with larger datasets.


#### 2.5.6 Error Handling

This section outlines the strategies for handling potential errors within the Sales & Inventory KPI Dashboard module.

* **2.5.6.1 Error Detection:**
    * The module will implement `try...except` blocks in Python code to catch potential exceptions during data retrieval and processing.
    * Input validation will be performed where applicable (e.g., if future enhancements allow user input).

* **2.5.6.2 Error Reporting:**
    * User-friendly error messages will be displayed in the UI if any issues prevent the dashboard from loading or refreshing data correctly.
    * Detailed error logs, including stack traces, will be recorded using Odoo's logging system for debugging purposes.

* **2.5.6.3 Error Recovery:**
    * The dashboard is designed to handle potential errors gracefully. If data retrieval for one KPI fails, the other KPIs should still attempt to load and display.
    * (Future Consideration) Retry mechanisms may be implemented for transient network-related errors during data fetching.

* **2.5.6.4 Specific Error Scenarios:**
    * **Database Errors:** The module will handle potential database connection or query errors by displaying a general error message to the user and logging the details for investigation.
    * **Network Errors:** If there are issues fetching data due to network connectivity problems, an appropriate message will be shown to the user, suggesting they check their connection and try again.


### 2.6 Assumptions and Dependencies

This section outlines the assumptions made during the requirements gathering and the dependencies that the Sales & Inventory KPI Dashboard module relies upon.

* **2.6.1 Assumptions:**
    * The `sale` Odoo module is installed, configured, and functioning correctly within the Odoo 18.0 instance.
    * The `stock` Odoo module (or a similar module managing product inventory) is installed, configured, and functioning correctly.
    * The `sale.order` model contains the fields `state` and `amount_total` with accurate and relevant data.
    * The `product.product` model provides accurate and up-to-date inventory information accessible through standard Odoo methods (e.g., `_compute_quantities_dict`).
    * Users accessing the dashboard have a basic understanding of the Odoo web interface and the concept of KPIs.
    * The Odoo 18.0 environment is stable and functioning as expected.

* **2.6.2 Dependencies:**
    * **Odoo Modules:**
        * `sale`
        * `stock` (or equivalent inventory management module)
        * `base`
    * **Odoo Core Functionality:**
        * Odoo ORM
        * Odoo Security System
        * Odoo Web Framework


## 3. Specific Requirements


### 3.1 Functional Requirements


ID	Requirement	Priority
FR01	Display total sum of 'amount_total' for confirmed ('sale' state) sales orders.	High
FR02	Display total count of confirmed ('sale' state) sales orders.	High
FR03	Display total available quantity of all products.	High
FR04	Provide a button to manually refresh KPI values.	High
FR05	On refresh, recalculate and update total sales, orders, and stock.	High
FR06	Provide "KPI Dashboard" menu under "Reporting."	High
FR07	Grant 'base.group_user' access to the KPI Dashboard menu and view.	High


### 3.2 Non-Functional Requirements

ID	Requirement	Priority
NFR01	Performance: Load/refresh within 3-5 seconds.	Medium
NFR02	Usability: Intuitive and easy to understand.	High
NFR03	Maintainability: Well-structured and easy to modify.	Medium
NFR04	Scalability: Design scalable for future KPI additions.	Low
NFR05	Security: Access controlled by standard Odoo security.	High

### 3.3 User Interface Requirements

* The dashboard shall be presented as a Form View in Odoo.
* Each KPI (Total Sales, Total Orders, Total Stock) shall be displayed in a distinct visual element (e.g., a colored card).
* The value of each KPI shall be prominently displayed.
* A "Refresh Data" button shall be clearly visible and accessible on the dashboard.
* Basic styling (as defined in `dashboard.css`) shall be applied to enhance the visual presentation of the KPIs.

### 4. Future Enhancements (Out of Scope)

The following are potential future enhancements that are not part of the current project scope:

* Displaying KPIs for specific time periods (e.g., current month, last month).
* Visualizing data using charts and graphs.
* Adding more KPIs related to inventory valuation, sales trends, etc.
* Implementing automatic data refresh at определенный intervals.
* Providing drill-down capabilities to view the underlying data.
* User-specific dashboard configurations.

### 5. Acceptance Criteria

The Sales & Inventory KPI Dashboard module will be considered acceptable upon meeting the following criteria:

* All functional requirements outlined in Section 3.1 are implemented and working correctly.
* The user interface matches the description in Section 3.3 and the basic styling is applied.
* The dashboard loads and refreshes data within an acceptable timeframe as defined in NFR01.
* No critical errors or bugs are identified during testing.

