# DiUS
Coding challenge represented from here https://github.com/DiUS/coding-tests/blob/master/dius_shopping.md
###

##Business Rules:##

"3 for 2 on Apple TVs - 'buyYgetX' with minimum buy"

"Ipad price drop to 499.99 if min purchase of 4"

"Bundle free VGA adaptor with every MacBook pro sold"


### To run solution:
input shopping cart items as list:  python Store.py 

### Solution explanation:
Store owner maintains a spreadsheet repesenting the items available including their discount or bundling rules:

where discounttype =['bulkmin','bundled','buyYgetX']

and bundleKey is the SKU of the entitled free item for an item whose discounttype is marked as 'bundled'

and minitems is the min number of items to apply a discounttype (for bulkmin and buyYgetX)

`SKU,name,price,discounttype,minitems,discount,bundleKey

'ipd','Super ipad','549.99','bulkmin',4,'50',None

'mpb','MacBook Pro','1399.99','bundled',1,'0','vga'

'atv','Apple TV','109.50','bulkxforx',3,'87.59',None

'vga','VGA adaptor','30.00','bundled',None,'-30.0',None`


products are initialised using the Product class:
e.g. :

` ipd = Product('ipd','Super ipad','549.99','bulkmin','4','50',None)`



The logic of bundle discounts ,buyYgetX, and bulkMin is programmed fully in the code, and the store owner need only update or add new items to the catalogue using the fields above, ensuring discounttype,minitems,discount and bundleKey are filled in appropriately.

 
## Tests 
# Unit tests for the ProductBundles class (out of time for the rest)

`python Test.py` 

Tests for the scenarios on the original git page have not been explicitly coded up but can be checked by commenting/uncommenting the product scenarios on lines 194-197 in Store.py

