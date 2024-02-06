
from collections import Counter
import copy


class Product(object):


    def __init__(self, SKU, name, price,discounttype,minitems,discount,bundledKey):
        """
        """        
        self.SKU = SKU
        self.name = name
        self.price = float(price)
        self.discounttype=discounttype
        self.minitems=int(minitems)
        self.discount=float(discount)
        self.bundledKey=bundledKey

    

    def __str__(self):
        return "Name: %s \n Price: %s\n" %(self.name,self.price) 

class Order:
    def __init__(self, products_ordered,total_price=0):
        self.products_ordered=products_ordered
        self.total = total_price

    def __str__(self):

        product_list = "".join('%s    %s   %s   %s\n'%(product[0].name,product[0].price,product[0].discount,product[1]) for product in self.products_ordered)

        return "Item\t price\t disc. price\t quantity\n%s \nTotal Price (inc. discounts): %s" % (product_list,self.total)        

class HandleDiscount:
    def __init__(self, product_count):
        self.product_count = product_count

    def calc_discount(product_count):
 
        product=product_count[0] 
        count=product_count[1]  
        discount_price = product.price  
    #count products with ipad, discount more than 4
        if product.discounttype.startswith('bulkmin') and count > product.minitems:
            discount_price = count*product.discount
            print('sku {0} discounted price {1}'.format(product.SKU,discount_price))
    # count products with SKU = atv apply 3 for 2
        if product.discounttype.startswith('buyYgetX'):
            
            if product.minitems<=count:
                remainder = count%product.minitems
                if remainder==0:
                    discount_price = count*product.discount
                else:
                    discount_price = count*product.price + remainder*product.discount
            else:
                discount_price=count*product.price

        return float(discount_price)


class ProductBundles:
    def __init__(self, products=[],ItemsDict={}):
        self.products=products
        self.indexes_bundle=[]
        self.has_bundles=False
        self.ItemsDict=ItemsDict

    def checkIfAnyBundled(self):
        
        self.indexes_bundle=[self.products[index].bundledKey for index in range(len(self.products)) if self.products[index].discounttype=='bundled']

        count_bundled=len(self.indexes_bundle) # number of products in order that are marked with 'bundled'
        if count_bundled>0:
            self.has_bundles=True
        else:
            self.has_bundles = False
        
        return self

    #def updateProductsList(self):

    def bundledCount(self):
        count_bundled=Counter(self.indexes_bundle)
        print(count_bundled)
        product_sku=[self.products[index].SKU for index in range(len(self.products))]
        countproducts=Counter(product_sku)
        print(countproducts)
        self.newProductsList=self.products

        difference = 0

        # compare number of items to be bundled with number of those items in the products list
        for i in count_bundled:
            bundleItem=self.ItemsDict[i]
            print(bundleItem.SKU)
            bundleItemZero=copy.deepcopy(bundleItem)
            bundleItemZero.price=0.0
            print(bundleItemZero.price)
            for j in countproducts:
                if i==j:
                    numA=count_bundled[i]
                    numB=countproducts[i]
                    print('Num A {0} NumB {1}'.format(numA,numB))
                    if numA==numB:
                        print('number existing in list equals number entitled')
                        for x in self.newProductsList:
                            print('x sku {0}'.format(x.SKU))
                            if x.SKU==i:
                                print('setting existing vga in list to $0')
                                x.price =0.0
                    if numB>numA:
                        # number entitled is more than number existing
                        print('number entitled is less than number existing')
                        difference=numB-numA
                        
                        print('difference {0} i {1}'.format(difference,i))
                        x=0
                        while x < difference-1:                            
                            for y in self.newProductsList:
                                if y.SKU==i:
                                    self.newProductsList.pop()
                                    self.newProductsList.append(bundleItemZero)
                                    x+=1
                                    
                            for y in self.newProductsList:
                                print('sku {0} price {1}'.format(y.SKU,y.price))
                    if numB<numA:
                            # make matching number of products Free
                        print('number entitled is more than number existing')
                        difference=numA-numB
                        print('difference {0} i {1}'.format(difference,i))
                        y=0
                        while y < difference:
                            self.newProductsList.append(bundleItemZero)
                            y+=1
                            print('y {0}'.format(y))

            
        return self.newProductsList





class Checkout:
    def __init__(self, products=[]):
        self.itemised_list=[[x,products.count(x)] for x in set(products)]

    def checkout(self):
        total_price = 0.00        

        for product in self.itemised_list:
            price=HandleDiscount.calc_discount(product)
            print("".join('%s %s %s\n'%(product[0].SKU,product[0].price,price)))

            total_price+=price
        # check product_unit_counts for bundled product?

        return Order(self.itemised_list,total_price)


def main():

    ipd = Product('ipd','Super ipad','549.99','bulkmin','4','499.99',None)
    mbp=Product('mbp','MacBook Pro','1399.99','bundled','1','0','vga')
    atv=Product('atv','Apple TV','109.50','buyYgetX','3','73',None)
    vga = Product('vga','VGA adaptor','30.00','bundledfree','0','0',None)

    ItemsDict={'ipd':ipd, 'mbp':mbp, 'atv':atv,'vga':vga}

    # initialise a dict here -- could also be read from a DB/csv or json file maintained by the user
    #SKUs Scanned: atv, atv, atv, vga Total expected: $249.00
    products=[atv,atv,atv,vga,vga,vga,mbp,mbp,mbp,mbp]
    products=[ atv, atv, atv, vga]
    products=[atv, ipd, ipd, atv, ipd, ipd, ipd]
    products=[mbp, vga, ipd]

    bundles=ProcessProductBundling(products,ItemsDict)
    print(bundles)

    if bundles.checkIfAnyBundled():
        counts=bundles.bundledCount()
        print(counts)
        new_productsList=bundles.products
        # get bundled item Id and check if any are in existing order.
    
        #print(any_bundles.indexes_bundle)

    # append vga to the products list if any mbps are purchased
    else:
        new_productsList=products

    

    #products=[atv,atv,atv,atv,atv,atv,mpd,vga]
    #products = [ipd,ipd,ipd,ipd,ipd]
    shopping_cart = Checkout(new_productsList)

    order = shopping_cart.checkout()
    print(order)



if __name__ == "__main__":
    main()