# 1045. [Customers Who Bought All Products](https://leetcode.com/problems/customers-who-bought-all-products/description/)

## Medium

## [Link to my solution](https://leetcode.com/problems/customers-who-bought-all-products/solutions/4613547/customer-who-bought-all-product-an-efficient-solution-using-group-by-beat-96-users/)

<hr><div>

## Problem Description

Given two tables, `Customer` and `Product`, find the customer IDs from the `Customer` table who bought all the products listed in the `Product` table.

### Customer Table

| Column Name | Type |
|-------------|------|
| customer_id | int  |
| product_key | int  |

This table may contain duplicate rows. `customer_id` is not NULL, and `product_key` is a foreign key (reference column) to the `Product` table.

### Product Table

| Column Name | Type |
|-------------|------|
| product_key | int  |

`product_key` is the primary key (column with unique values) for this table.


## Example

### Input

**Customer Table:**

| customer_id | product_key |
|-------------|-------------|
| 1           | 5           |
| 2           | 6           |
| 3           | 5           |
| 3           | 6           |
| 1           | 6           |

**Product Table:**

| product_key |
|-------------|
| 5           |
| 6           |

### Output

| customer_id |
|-------------|
| 1           |
| 3           |

## Explanation

The customers who bought all the products (5 and 6) are customers with IDs 1 and 3.
