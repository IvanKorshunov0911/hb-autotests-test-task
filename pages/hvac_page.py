import data_for_tests
from .base_page import BasePage
from .locators import HvacPageLocators
from selenium.common.exceptions import NoSuchElementException
from random import randint


class HvacPage(BasePage):
    ENTER_ZIP_CODE_LABEL_TEXT = "Enter ZIP Code"

    def enter_ok_zip_code(self, zip_id='zipCode'):
        self.fill_input(HvacPageLocators.ZIP_INPUT[0], HvacPageLocators.ZIP_INPUT[1].format(zip_id=zip_id),
                        data_for_tests.ZIP_CODE_OK)

    def enter_nok_zip_code(self, zip_id='zipCode'):
        self.fill_input(HvacPageLocators.ZIP_INPUT[0], HvacPageLocators.ZIP_INPUT[1].format(zip_id=zip_id),
                        data_for_tests.ZIP_CODE_NOK)

    def right_icon_should_be_visible(self, zip_id='zipCode'):
        self.should_be_visible(HvacPageLocators.RIGHT_ICON[0], HvacPageLocators.RIGHT_ICON[1].format(zip_id=zip_id))

    def should_be_enter_zip_code_label(self, zip_id='zipCode'):
        self.should_be_visible(HvacPageLocators.ENTER_ZIP_CODE_LABEL[0],
                               HvacPageLocators.ENTER_ZIP_CODE_LABEL[1].format(zip_id=zip_id))
        self.text_should_be_equal_to(HvacPageLocators.ENTER_ZIP_CODE_LABEL[0],
                                     HvacPageLocators.ENTER_ZIP_CODE_LABEL[1].format(zip_id=zip_id),
                                     self.ENTER_ZIP_CODE_LABEL_TEXT)

    def press_get_estimate_button(self, zip_id='zipCode'):
        self.press_button(HvacPageLocators.GET_ESTIMATE_BUTTON[0],
                          HvacPageLocators.GET_ESTIMATE_BUTTON[1].format(zip_id=zip_id))

    def should_be_project_type_question(self):
        self.should_be_visible(*HvacPageLocators.TYPE_OF_PROJECT_QUESTION)

    def right_icon_should_not_be_visible(self, zip_id='zipCode'):
        self.should_not_be_visible(HvacPageLocators.RIGHT_ICON[0], HvacPageLocators.RIGHT_ICON[1].format(zip_id=zip_id))

    def should_be_zip_tip(self, zip_id='zipCode'):
        self.should_be_visible(HvacPageLocators.ZIP_TIP[0], HvacPageLocators.ZIP_TIP[1].format(zip_id=zip_id))

    def press_repair_button(self):
        self.press_button(*HvacPageLocators.REPAIR_BUTTON)

    def press_continue_no_button(self):
        self.press_button(*HvacPageLocators.CONTINUE_NO_BUTTON)

    def press_go_to_homepage_button(self):
        self.press_button(*HvacPageLocators.GO_TO_HOMEPAGE_BUTTON)

    def press_replacement_installation_button(self):
        self.press_button(*HvacPageLocators.REPLACEMENT_INSTALLATION_BUTTON)

    def press_submit_next_button(self):
        self.press_button(*HvacPageLocators.SUBMIT_NEXT_BUTTON)

    def press_equipment_notsure_button(self):
        self.press_button(*HvacPageLocators.EQUIPMENT_NOTSURE_BUTTON)

    def press_energysource_notsure_button(self):
        self.press_button(*HvacPageLocators.ENERGYSOURCE_NOTSURE_BUTTON)

    def press_equipmentage_notsure_button(self):
        self.press_button(*HvacPageLocators.EQUIPMENTAGE_NOTSURE_BUTTON)

    def press_propertytype_detached_button(self):
        self.press_button(*HvacPageLocators.PROPERTYTYPE_DETACHED_BUTTON)

    def enter_ok_squarefeet(self):
        self.fill_input(*HvacPageLocators.SQUAREFEET_INPUT, data_for_tests.SQUAREFEET_OK)

    def press_owner_yes_button(self):
        self.press_button(*HvacPageLocators.OWNER_YES_BUTTON)

    def fill_fullname_email_ok(self):
        self.fill_input(*HvacPageLocators.FULLNAME_INPUT, data_for_tests.FULL_NAME_OK)
        self.fill_input(*HvacPageLocators.EMAIL_INPUT, data_for_tests.EMAIL_ADDRESS_OK)

    def fill_phone_number_ok(self):
        rand_number = str(randint(1000000000, 9999999999))
        self.fill_input(*HvacPageLocators.PHONE_NUMBER_INPUT, rand_number)

    def press_submit_my_request_button(self):
        self.press_button(*HvacPageLocators.SUBMIT_MY_REQUEST_BUTTON)

    def press_phone_number_is_correct_button(self):
        try:
            self.press_button(*HvacPageLocators.PHONE_NUMBER_IS_CORRECT_BUTTON)
        except NoSuchElementException:
            pass

    def should_be_thank_you_text(self):
        self.should_be_visible(HvacPageLocators.THANK_YOU_TEXT[0], HvacPageLocators.THANK_YOU_TEXT[1].format(
            name=data_for_tests.FULL_NAME_OK.split(' ')[0]))
