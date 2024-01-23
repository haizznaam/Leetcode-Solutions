# 181. [Employees Earning More Than Their Managers](https://leetcode.com/problems/employees-earning-more-than-their-managers/description/)

## Easay

<hr><div>

## Table: Employee

| Column Name | Type    |
|-------------|---------|
| id          | int     |
| name        | varchar |
| salary      | int     |
| managerId   | int     |

- `id` is the primary key (column with unique values) for this table.
- Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.

### Problem Statement

Write a solution to find the employees who earn more than their managers.

Return the result table in any order.

The result format is in the following example.

### Example

**Input:**

Employee table:
<<<<<<< HEAD
=======

>>>>>>> 06b1b0c1c9e3cab2be9e94377569041bd5299f53
| id | name  | salary | managerId |
| -- | ----- | ------ | --------- |
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | null      |
| 4  | Max   | 90000  | null      |
<<<<<<< HEAD


**Output:**
| Employee |
| -------- |
| Joe      |
=======



**Output:**

| Employee |
| -------- |
| Joe      |

>>>>>>> 06b1b0c1c9e3cab2be9e94377569041bd5299f53

Explanation: Joe is the only employee who earns more than his manager.
