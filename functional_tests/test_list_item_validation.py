from .base import FunctionalTest
MAX_WAIT = 10


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits enter on the empty input obx

        # The homepages refreshes, and there is an error message saying
        # that list items cannot be blank

        # She tries again with some test for the items, which now works

        # Perversely, now she decides to submit a second blank list item

        # She receives a similar warning on the list page

        # And she can correct it by filling some text in
        self.fail('write me!')
