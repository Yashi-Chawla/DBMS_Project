\c shopping
drop role customer;
drop role admin;
create role customer login password 'customer';
create role admin login password 'admin';

-- customer, customer_order, product, brand, supplier, transaction, sold_by, review
grant all on customer to customer;
grant all on customer_order to customer;
grant select, insert, update on review to customer;
grant all on cart to customer;
grant select,update on transaction to customer;
grant select on product to customer;
grant select on brand to customer;
grant select on supplier to customer;
grant select on sold_by to customer;

grant all on brand to admin;
grant all on supplier to admin;
grant all on product to admin;
grant all on transaction to admin;
grant all on cart to admin;
grant all on sold_by to admin;
grant select on customer to admin;
grant select on review to admin;

grant yashi to customer;