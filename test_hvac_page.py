import pytest
from pages.hvac_page import HvacPage

url = "https://hb-autotests.stage.sirenltd.dev/"
hvac_url = url + "hvac"
zip_ids = ['zipCode', 'zip_content1', 'zip_footer1']


@pytest.mark.parametrize('zip_id', zip_ids)
def test_zip_code_positive(browser, zip_id):
    page = HvacPage(browser, hvac_url)
    page.open()
    page.should_be_enter_zip_code_label(zip_id=zip_id)
    page.enter_ok_zip_code(zip_id=zip_id)
    page.right_icon_should_be_visible(zip_id=zip_id)
    page.press_get_estimate_button(zip_id=zip_id)
    page.should_be_project_type_question()


@pytest.mark.parametrize('zip_id', zip_ids)
def test_zip_code_negative(browser, zip_id):
    page = HvacPage(browser, hvac_url)
    page.open()
    page.should_be_enter_zip_code_label(zip_id=zip_id)
    page.enter_nok_zip_code(zip_id=zip_id)
    page.right_icon_should_not_be_visible(zip_id=zip_id)
    page.press_get_estimate_button(zip_id=zip_id)
    page.should_be_zip_tip(zip_id=zip_id)


def test_repair_no(browser):
    page = HvacPage(browser, hvac_url)
    page.open()
    page.enter_ok_zip_code()
    page.press_get_estimate_button()
    page.press_repair_button()
    page.press_continue_no_button()
    page.press_go_to_homepage_button()
    page.url_should_be_equal_to(url)


def test_full_questionnaire_fill(browser):
    page = HvacPage(browser, hvac_url)
    page.open()
    page.enter_ok_zip_code()
    page.press_get_estimate_button()
    page.press_replacement_installation_button()
    page.press_submit_next_button()
    page.press_equipment_notsure_button()
    page.press_submit_next_button()
    page.press_energysource_notsure_button()
    page.press_submit_next_button()
    page.press_equipmentage_notsure_button()
    page.press_submit_next_button()
    page.press_propertytype_detached_button()
    page.press_submit_next_button()
    page.enter_ok_squarefeet()
    page.press_submit_next_button()
    page.press_owner_yes_button()
    page.press_submit_next_button()
    page.fill_fullname_email_ok()
    page.press_submit_next_button()
    page.fill_phone_number_ok()
    page.press_submit_my_request_button()
    page.press_phone_number_is_correct_button()
    page.should_be_thank_you_text()
