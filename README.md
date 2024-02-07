# DiUS
Coding challenge represented from here https://github.com/DiUS/coding-tests/blob/master/dius_shopping.md
###

Business Rules:
"3 for 2 on Apple TVs - 'buyYgetX' with minimum buy"
"Ipad price drop to 499.99 if min purchase of 4"
"Bundle free VGA adaptor with every MacBook pro sold"


### To run solution:
input shopping cart items as list:  python Store.py 

### Solution explanation:
Store owner maintains a spreadsheet repesenting the items avialable including their discount or bundling rules:
    ipd = Product('ipd','Super ipad','549.99','bulkmin','4','50',None)
    mbp=Product('mbp','MacBook Pro','1399.99','bundled','1','0','vga')
    atv=Product('atv','Apple TV','109.50','buyYgetX','3','73',None)
    vga = Product('vga','VGA adaptor','30.00','bundledfree','0','0',None)
discounttype =['bulkmin','bundled','buyYgetX']
bundleKey-if an item can have another item type bundled, reference the item SKU in this field
minitems - if bulkMin or buyYgetX , specify the min purchase before this form of discount can be applied.

The logic of bundle discounts ,buyYgetX, and bulkMin is programmed and the store owner need only update or add to their list.

