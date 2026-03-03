class InventoryPage:
    def __init__(self, page):
        self.page=page
        self.cart_bdg = page.locator('[data-test="shopping-cart-badge"]')

    def get_title_text(self):
        page_title=self.page.locator('[data-test="title"]').inner_text()
        return page_title

    def add_item_to_cart(self, item_name):
        user_select_item=self.page.locator('.inventory_item').filter(has_text=item_name)
        user_select_item.get_by_role('button', name='Add to cart').click()
