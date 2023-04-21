from .base_page import BasePage
from .locators import BasePageLocators
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_items_in_basket_initially(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
            "Success message is presented, but should not be"

    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), \
            "Empty basket text is absent, but should be present"
