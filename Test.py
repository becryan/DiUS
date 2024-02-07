
import unittest
from Store import Product, ProductBundles, ProductDiscount

class TestProductBundles(unittest.TestCase):
    ipd = Product('ipd','Super ipad','549.99','bulkmin','4','499.99',None)
    mbp=Product('mbp','MacBook Pro','1399.99','bundled','1','0','vga')
    atv=Product('atv','Apple TV','109.50','buyYgetX','3','73',None)
    vga = Product('vga','VGA adaptor','30.00','bundledfree','0','0',None)

    ItemsDict={'ipd':ipd, 'mbp':mbp, 'atv':atv,'vga':vga}
    products=[mbp,mbp,mbp,mbp]
    products_nobundles=[vga,vga,atv]
    def testBundledCount(self):
        
        bundles=ProductBundles(self.products,self.ItemsDict)
        self.assertGreater(bundles.checkIfAnyBundled().count_bundled,0,
                           'No bundles in products')
        
    def testNoBundlesInProductList(self):
        
        bundles=ProductBundles(self.products,self.ItemsDict)
        self.assertEqual(bundles.checkIfAnyBundled().count_bundled,0,
                           'No bundles in products')


#def test_total(items):
#SKUs Scanned: atv, atv, atv, vga Total expected: $249.00


#SKUs Scanned: atv, ipd, ipd, atv, ipd, ipd, ipd Total expected: $2718.95
#109.5+109.5+5*(549.99-50) = 2 atv + 5 ipd

#SKUs Scanned: mbp, vga, ipd Total expected: $1949.98
#1399.99+0+549.99 = 1949.88

#class TestProduct(unittest.TestCase):
#    ''' Purpose of test'''
    
    
    
#    self.assertEqual(....)
    




#class TestProductCollection(unittest.TestCase):
    # can we findfrom dict of products





if __name__ == '__main__':
    unittest.main()