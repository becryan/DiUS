Coding challenge represente from here https://github.com/DiUS/coding-tests/blob/master/dius_shopping.md
###

Business Rules:
"As we're launching our new computer store, we would like to have a few opening day specials.

we're going to have a 3 for 2 deal on Apple TVs. For example, if you buy 3 Apple TVs, you will pay the price of 2 only
the brand new Super iPad will have a bulk discounted applied, where the price will drop to $499.99 each, if someone buys more than 4
we will bundle in a free VGA adapter free of charge with every MacBook Pro sold"

### To run solution:
input shopping cart items as list:  python Store.py vtp,ipd,xyz

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
** not included -- handling the input list of store items must only be in