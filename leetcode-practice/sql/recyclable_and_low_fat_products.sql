-- Problem: Recyclable and Low Fat Products
-- Approach: Use WHERE
-- Logic: Select product_id only for rows where low_fats = 'Y' AND recyclable = 'Y'
SELECT
        product_id
FROM
        Products
WHERE
        low_fats='Y' AND recyclable='Y'