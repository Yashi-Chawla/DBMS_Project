\c shopping
drop role customer;
drop role admin;
create role customer login password 'customer';
create role admin login password 'admin';

-- customer, customer_order, product, brand, supplier, transaction, sold_by, review
grant all on customer to customer;
grant all on customer_order to customer;
grant all on cart to customer;

grant select, insert, update on review to customer;
grant select, update on transaction to customer;

grant select on product to customer;
grant select on brand to customer;
grant select on supplier to customer;
grant select on sold_by to customer;

--all- insert, update, delete.  Read, write, delete. 
grant all on brand to admin;
grant all on supplier to admin;
grant all on product to admin;
grant all on sold_by to admin;

grant select on customer to admin;
grant select on review to admin;
grant select on transaction to admin;
grant select on cart to admin;

--update customer
--select from product
--insert into cart 
--select cart, transaction
--insert review 

--admin can select/read from customer,review,transaction, cart
--admin can insert, update, delete on brand, supplier,product, sold_by