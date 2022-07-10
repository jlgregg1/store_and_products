import product
import store

safeway = store.Store("Safeway")
apple = product.Product("Apple", 50, "produce", 1234)
safeway.add_product(apple)
banana = product.Product("Banana", 25, "produce", 5678)
safeway.add_product(banana).sell_product(5678).print_product_list()