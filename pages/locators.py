from selenium.webdriver.common.by import By


class HvacPageLocators:
    ZIP_INPUT = (By.CSS_SELECTOR, '#{zip_id}')
    RIGHT_ICON = (By.XPATH, '//input[@id="{zip_id}"]/following-sibling::div[@class="rightIcon"]')
    ENTER_ZIP_CODE_LABEL = (By.XPATH, '//input[@id="{zip_id}"]/following-sibling::label[@for="{zip_id}"]')
    GET_ESTIMATE_BUTTON = (By.XPATH, '//input[@id="{zip_id}"]/../following-sibling::button[@type="submit"]')
    TYPE_OF_PROJECT_QUESTION = (By.XPATH, '//h4[contains(text(), "What type of project is this?")]')
    ZIP_TIP = (By.XPATH, '//input[@id="{zip_id}"]/../../../div[contains(text(), "The ZIP Code must be 5 digits with no spaces")]')
    REPAIR_BUTTON = (By.XPATH, '//input[@data-autotest-radio-projecttype-repair]/..')
    CONTINUE_NO_BUTTON = (By.XPATH, '//button[@data-autotest-button-button-no]')
    GO_TO_HOMEPAGE_BUTTON = (By.XPATH, '//button[@data-autotest-button-button-go-to-homepage]')

    SUBMIT_NEXT_BUTTON = (By.XPATH, '//button[@data-autotest-button-submit-next]')

    REPLACEMENT_INSTALLATION_BUTTON = (By.XPATH, '//input[@data-autotest-radio-projecttype-replacementorinstallation]/..')

    EQUIPMENT_NOTSURE_BUTTON = (By.XPATH, '//input[@data-autotest-checkbox-equipment-notsure]/..')

    ENERGYSOURCE_NOTSURE_BUTTON = (By.XPATH, '//input[@data-autotest-radio-energysource-notsure]/..')

    EQUIPMENTAGE_NOTSURE_BUTTON = (By.XPATH, '//input[@data-autotest-radio-equipmentage-notsure]/..')

    PROPERTYTYPE_DETACHED_BUTTON = (By.XPATH, '//input[@data-autotest-radio-propertytype-detached]/..')

    SQUAREFEET_INPUT = (By.XPATH, '//input[@data-autotest-input-squarefeet-tel]')

    OWNER_YES_BUTTON = (By.XPATH, '//input[@data-autotest-radio-owner-yes]/..')

    FULLNAME_INPUT = (By.XPATH, '//input[@data-autotest-input-fullname-text]')
    EMAIL_INPUT = (By.XPATH, '//input[@data-autotest-input-email-email]')

    PHONE_NUMBER_INPUT = (By.XPATH, '//input[@data-autotest-input-phonenumber-tel]')
    SUBMIT_MY_REQUEST_BUTTON = (By.XPATH, '//button[@data-autotest-button-submit-submit-my-request]')
    PHONE_NUMBER_IS_CORRECT_BUTTON = (By.XPATH, '//button[@data-autotest-button-submit-phone-number-is-correct]')

    THANK_YOU_TEXT = (By.XPATH, '//h4[contains(text(), "Thank you {name}, your contractor") and contains(text(), "will call soon!")]')
