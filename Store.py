
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


class Checkout:
    ''''''
    def __init__(self, products=[]):
        self.itemised_list=[[x,products.count(x)] for x in set(products)]

    def checkout(self):
        total_price = 0.00        

        for product in self.itemised_list:
            price=ProductDiscount.calc_discount(product)

            total_price+=price

        return Order(self.itemised_list,total_price)

class Order:
    def __init__(self, products_ordered,total_price=0):
        self.products_ordered=products_ordered
        self.total = total_price

    def __str__(self):

        product_list = "".join('%s\t%s\t%s\t%s\t%s\n'%(product[0].SKU,product[0].name,product[0].price,product[0].discount,product[1]) for product in self.products_ordered)

        return "SKU\tItem \t Unit price\t disc. price\t quantity\n%s \nTotal Price (inc. discounts): %s" % (product_list,self.total)        

class ProductDiscount:
    def __init__(self, product_count):
        self.product_count = product_count

    def calc_discount(product_count): 
        product=product_count[0] 
        count=product_count[1]  
        discount_price = product.price  
        if product.discounttype.startswith('bulkmin') and count > product.minitems:
            discount_price = count*product.discount
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
        self.ItemsDict=ItemsDict
        
    def retrieveBundledItems(self):
        self.indexes_bundle=[self.products[index].bundledKey
                             for index in range(len(self.products)) if self.products[index].discounttype=='bundled']
        return self
        
        
    def checkBundleKeyExistsInItemDict(self):
        '''
        Check that bundleKey object for object that is entitled to bundling exists in the catalogue
        '''
        print('checking bundled keys_')
        print(self.indexes_bundle)
        for i in self.indexes_bundle:
            if i in self.ItemsDict:
                print('matched bundleKey exists in catalogue')
                entitledItemExists=True
            else:
                print('There is no matching object to bundle')
                entitledItemExists=False
                #exit()

        
        return entitledItemExists
        


    def updateProductsList(self):
        '''
        Check the product list for existing items entitled, by bundleKey matching SKU
        and adjust the products and prices in the list accordingly for three cases:
        
        Case 1: no. of bundle entitled items == no. of bundleKey items in product list 
        Case 2: no. of bundle entitled items  > no of bundleKey items in product list
        Case 3: no. of bundle entitled items < no. of bundleKey items in product list
                    
        '''
        product_sku=[self.products[index].SKU for index in range(len(self.products))]
        countproducts=Counter(product_sku)
        self.newProductsList=self.products
        count_bundled=Counter(self.indexes_bundle)
        for i in count_bundled:
            bundleItem=self.ItemsDict[i]
            bundleItemZero=copy.deepcopy(bundleItem)
            bundleItemZero.price=0.0
            for j in countproducts:
                if i==j:
                    
                    bundleEntitledCount=count_bundled[i] # no. of bundle entitled items
                    bundleKeyCount=countproducts[i] # no. of corresponding bundleKey items in list
                    
                    if bundleEntitledCount==bundleKeyCount: # Case 1
                        print('Bundle Entitled items equals number of existing BundleKey items')
                        for x in self.newProductsList:
                            print('x sku {0}'.format(x.SKU))
                            if x.SKU==i:
                                x.price =0.0
                                
                    if bundleKeyCount>bundleEntitledCount: # Case 2
                        # delete bundleEntitledCount number of bundleKey items in product list
                        # and append new bundleKey item (with price set to 0) to the list
                        print('Buntle entitled items is less than existing number of bundleKey items')
                        difference=bundleKeyCount-bundleEntitledCount
                        # 
                        x=0
                        while x < difference-1:                            
                            for y in self.newProductsList:
                                if y.SKU==i:
                                    self.newProductsList.pop()
                                    self.newProductsList.append(bundleItemZero)
                                    x+=1
                                    
                    if bundleKeyCount<bundleEntitledCount: # Case 3
                        # append extra entitled bundleKey items to the product list
                        print('Number entitled is more than number existing in list')
                        difference=bundleEntitledCount-bundleKeyCount
                        y=0
                        while y < difference:
                            self.newProductsList.append(bundleItemZero)
                            y+=1

            
        return self.newProductsList



def main():
    
    # initialise a dict here -- could also be read from a DB/csv or json file maintained by the user

    ipd = Product('ipd','Super ipad','549.99','bulkmin','4','499.99',None)
    mbp=Product('mbp','MacBook Pro','1399.99','bundled','1','0','vga')
    atv=Product('atv','Apple TV','109.50','buyYgetX','3','73',None)
    vga = Product('vga','VGA adaptor','30.00','bundledfree','0','0',None)

    ItemsDict={'ipd':ipd, 'mbp':mbp, 'atv':atv,'vga':vga}

    
    #SKUs Scanned: atv, atv, atv, vga Total expected: $249.00
    products=[atv,atv,atv,vga,vga,vga,mbp,mbp,mbp,mbp]
    #products=[ atv, atv, atv, vga]
    #products=[atv, ipd, ipd, atv, ipd, ipd, ipd]
    #products=[mbp, vga, ipd]

    bundles=ProductBundles(products,ItemsDict)
    count_bundles=len(bundles.retrieveBundledItems().indexes_bundle)
    print(count_bundles)
    bundles.checkBundleKeyExistsInItemDict()
    

    if count_bundles>0:
        newProductList=bundles.updateProductsList()

        new_productsList=newProductList

    else:
        new_productsList=products

    

    #products=[atv,atv,atv,atv,atv,atv,mpd,vga]
    #products = [ipd,ipd,ipd,ipd,ipd]
    shopping_cart = Checkout(new_productsList)

    order = shopping_cart.checkout()
    print(order)



if __name__ == "__main__":
    main()