### 📄 **Feature Implementation Report**

#### **Feature Name:**

Flask API Backend with Data Filtering, Pagination, and Tool Management

#### **Date Implemented:**

\[Insert Date]

#### **Developer:**

\[Your Name]

---

### ✅ **Objective**

To create a full-stack project with a Flask API backend that communicates with a SQL Server database. This API supports:

1. Retrieving data from the database.
2. Implementing pagination and filtering on large datasets.
3. Serving dynamic SQL queries through Jinja2 templating.
4. Handling vendor and inventory-related queries.

---

### 🛠️ **Project Setup Overview**

**File Structure:**

```
project/
├── .venv                # Virtual environment for the project
├── api-front            # Frontend directory (React app)
├── sql                  # SQL query files
├── .env                 # Environment variables
├── requirements.txt     # Python dependencies
├── main.py              # Flask app
├── README.md            # Project documentation
```

**Key Tools/Technologies:**

- **Flask**: Web framework for the backend API.
- **SQLAlchemy**: ORM used for database interactions.
- **Jinja2**: Templating engine used for dynamic SQL query generation.
- **Flask-CORS**: Cross-Origin Resource Sharing for frontend-backend communication.
- **Flask-Compress**: Middleware for gzip compression of API responses.
- **dotenv**: Loads environment variables from a `.env` file.

---

### 🧩 **Features and Routes**

1. **Database Configuration**:

   - **ODBC Connection**: Uses SQLAlchemy's `pyodbc` dialect to connect to a Microsoft SQL Server database.

   **Connection Example**:

   ```python
   odbc_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server},{port};DATABASE={database};UID={username};PWD={password}"
   engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")
   ```

2. **Main Routes**:

   - **`/`**: Returns a simple "Index" message.
   - **`/data`**: Fetches data from the database and returns it as a JSON object.
   - **`/cols`**: Returns the column names from the database table.
   - **`/colHeaders`**: Returns a predefined list of column headers for tools data.
   - **`/data_inventory`**: Handles pagination and filtering of inventory data with SQL query templating.
   - **`/data_vendor`**: Handles pagination and filtering of vendor data similarly.

3. **Utility Functions**:

   - **`convert_to_serializable(data)`**: Ensures `datetime` objects are converted to a serializable format (ISO format).
   - **`render_sql_template(filename, **kwargs)`\*\*: Loads and renders SQL templates using Jinja2, allowing dynamic query generation based on filters.

---

### 📊 **Pagination and Filtering**

Pagination and filtering are crucial features for handling large datasets. The following logic is implemented for both inventory and vendor data:

- **Pagination**:

  - The API supports `page` and `limit` query parameters to manage the dataset size.
  - Example request: `/data_inventory?page=2&limit=10`.

- **Filtering**:

  - Filters are passed as query parameters (e.g., `process`, `machine`, `tool`, `plug`).
  - The `render_sql_template()` function dynamically builds the query based on these filters.

Example Filter Logic in the `/data_inventory` endpoint:

```python
filters = {
    'process': request.args.get('process'),
    'machine': request.args.get('machine'),
    'tool': request.args.get('tool'),
    'plug': request.args.get('plug')
}
```

---

### 📦 **Frontend Integration: React**

The project also includes a frontend in the `api-front` directory, built with **React**.

1. **Frontend Components**:

   - **Filter.jsx**: Component for filtering tool data.
   - **GenericTable.jsx**: Displays tabular data based on filtered results.
   - **PaginationControls.jsx**: Manages the pagination logic for the frontend.
   - **IsInventory.jsx** and **IsVendor.jsx**: Displays inventory and vendor data respectively.

**App.js**:

```jsx
import React from "react";
import Filter from "./components/Filter";
import IsInventory from "./components/IsInventory";
import IsVendor from "./components/IsVendor";
import PaginationControls from "./components/PaginationControls";

function App() {
  return (
    <div>
      <Filter />
      <IsInventory />
      <IsVendor />
      <PaginationControls />
    </div>
  );
}

export default App;
```

---

### ⚡ **Key Features & Benefits**

1. **Dynamic Data Fetching**:

   - The backend dynamically responds to frontend requests with filtered and paginated data, ensuring efficient handling of large datasets.

2. **SQL Query Templating**:

   - By utilizing Jinja2 for SQL query generation, the project allows flexible, dynamic, and reusable SQL queries for different filter conditions.

3. **Seamless Integration**:

   - CORS is enabled to allow smooth communication between the Flask backend and React frontend.
   - The frontend provides real-time filtering and pagination for a better user experience.

4. **Compression**:

   - Flask-Compress is used to minimize the size of API responses, improving load times and performance.

---

### 🧪 **Testing Scenarios**

| Route             | Test Scenario                                 | Expected Result                                 |
| ----------------- | --------------------------------------------- | ----------------------------------------------- |
| `/data`           | Fetch data from the database                  | Return formatted data in JSON                   |
| `/cols`           | Fetch column names                            | Return a list of column names from the database |
| `/data_inventory` | Fetch paginated data with filters             | Return filtered data based on query parameters  |
| `/data_vendor`    | Fetch vendor data with pagination and filters | Return filtered vendor data                     |
| `/colHeaders`     | Fetch predefined column headers               | Return a static list of column names            |

---

### 📌 **Next Steps / Recommendations**

1. **Frontend Enhancements**:

   - Add form validation for filter inputs in React components.
   - Provide visual indicators for active filters and pagination.

2. **Performance Improvements**:

   - Implement caching for frequently requested data to reduce load on the database.
   - Add error handling for empty query results and timeouts.

3. **Deployment**:

   - Set up a production environment with proper configuration for secure access to the database.
   - Deploy the Flask backend to a platform like Heroku or AWS.
