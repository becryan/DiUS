
import unittest
from Store import Product, ProductBundles, Checkout, Order

class TestProductBundles(unittest.TestCase):
    ipd = Product('ipd','Super ipad','549.99','bulkmin','4','499.99',None)
    mbp=Product('mbp','MacBook Pro','1399.99','bundled','1','0','vga')
    atv=Product('atv','Apple TV','109.50','buyYgetX','3','73',None)
    vga = Product('vga','VGA adaptor','30.00','bundledfree','0','0',None)

    ItemsDict={'ipd':ipd, 'mbp':mbp, 'atv':atv,'vga':vga}
    products=[mbp,mbp,mbp,mbp]
    products_nobundles=[vga,vga,atv]
    products_minusbundles=[vga,vga,mbp,mbp,mbp]
    
    def testBundledCount(self):        
        bundles=ProductBundles(self.products,self.ItemsDict).retrieveBundledItems()
        bundleItems=bundles.indexes_bundle
        print('Check product list contains bundle entitled items')
        self.assertGreater(len(bundleItems),0,'Product list contains 0 bundle entitled items!')
        
    def testNoBundlesInProductList(self):
        bundles = ProductBundles(self.products_nobundles,self.ItemsDict).retrieveBundledItems()
        bundleItems=bundles.indexes_bundle
        print('Check product list contains no bundle entitled items')
        self.assertEqual(len(bundleItems),0,'Product list contains bundled entitled items!')
        
    def testNewProductListAppendBundleKeyItem(self):
        bundles=ProductBundles(self.products,self.ItemsDict).retrieveBundledItems()
        bundles.updateProductsList()
        updatedProducts=bundles.newProductsList 

        newproductList=['mbp','mbp','mbp','mbp','vga','vga','vga','vga']
               
        updatedProductList=[x.SKU for x in updatedProducts]
        print(updatedProductList)
        self.assertEqual(newproductList,updatedProductList,'The product list was not properly updated')

    def testNewProductListAddOneBundleItem(self):
        bundles=ProductBundles(self.products_minusbundles,self.ItemsDict).retrieveBundledItems()
        bundles.updateProductsList()
        updatedProducts=bundles.newProductsList 

        newproductList=['vga','vga','mbp','mbp','mbp','vga']
               
        updatedProductList=[x.SKU for x in updatedProducts]
        print(updatedProductList)
        self.assertEqual(newproductList,updatedProductList,'The product list was not properly updated')
        
        
        
class TestMain(unittest.TestCase):
    '''
    Test the scenarios written in the original git repository
    '''

    #test1=[atv,atv,atv,vga]  # Total expected 249.0
    #test2=[atv,ipd,ipd,atv,ipd,ipd,ipd] # Total expected 2718.95
    #test3=[mbp,vga,ipd] # Total expected 2718.95

    

        
    #def test1(test1):
    #    total=calculateTotal(self.test1,self)
    
    
### Out of time to write more...




if __name__ == '__main__':
    unittest.main()