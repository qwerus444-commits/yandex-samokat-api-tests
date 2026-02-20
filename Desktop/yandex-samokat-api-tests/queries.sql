-- Задание 1: логины курьеров и количество заказов в доставке
SELECT c.login, COUNT(o.id) AS "delivery_count"
FROM "Couriers" c
LEFT JOIN "Orders" o ON c.id = o."courierId" AND o."inDelivery" = true
GROUP BY c.login;

-- Задание 2: трекеры заказов и их статусы
SELECT track,
       CASE
           WHEN finished = true THEN 2
           WHEN cancelled = true THEN -1
           WHEN "inDelivery" = true THEN 1
           ELSE 0
       END AS status
FROM "Orders";