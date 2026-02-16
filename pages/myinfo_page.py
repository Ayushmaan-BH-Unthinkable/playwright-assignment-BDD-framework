from time import sleep
import os


class MyInfoPage:
    def __init__(self, page):
        self.page = page

        # Tabs & Sections
        self.myinfo_tab = "a[href='/web/index.php/pim/viewMyDetails']"
        self.personal_details_section = "h6:has-text('Personal Details')"

        self.edit_button = "button.oxd-button--secondary"
        self.save_button = "(//button[normalize-space()='Save'])[1]"

        # Editable fields
        self.first_name_input = "xpath=//input[@name='firstName']"
        self.middle_name_input = "xpath=//input[@name='middleName']"
        self.last_name_input = "xpath=//input[@name='lastName']"

        # Restricted fields
        self.employee_id_input = "xpath=//label[normalize-space()='Employee Id']/ancestor::div[contains(@class,'oxd-input-group')]//input"

        # Photo upload
        self.upload_button = "div.orangehrm-employee-image button[type='submit']"
        self.upload_success_msg = "text=Successfully Updated"
        self.upload_error_msg = "text=Attachment Size Exceeded"
        self.profile_image = ".orangehrm-edit-employee-image"
        self.photo_input = "input[type='file']"

        # Common Table
        self.table_rows = "div.oxd-table-body div.oxd-table-row"
        self.delete_button = "button:has-text('Delete')"
        self.confirm_delete_button = "button:has-text('Yes, Delete')"
        self.add_button = "button:has-text('Add')"

    # -------------------------------
    # Navigation
    # -------------------------------

    def open_myinfo_tab(self):
        self.page.click(self.myinfo_tab)
        self.page.wait_for_selector(self.personal_details_section)

    def save_personal_details(self):
        self.page.click(self.save_button)
        self.page.wait_for_selector("text=Successfully Updated")

    def open_dependents_section(self):
        self.page.click("a:has-text('Dependents')")
        self.page.wait_for_selector("text=Assigned Dependents")

    def open_section(self, section_name):
        self.page.click(f'a:has-text("{section_name}")')
        self.page.wait_for_selector(f"text={section_name}")

    # -------------------------------
    # Getters for Validation
    # -------------------------------

    def get_first_name(self):
        return self.page.input_value(self.first_name_input)

    def get_last_name(self):
        return self.page.input_value(self.last_name_input)

    # -------------------------------
    # Edit fields
    # -------------------------------

    def edit_personal_details(self, first=None, middle=None, last=None):
        if first:
            self.enter_text(self.first_name_input, first)

        if middle:
            self.enter_text(self.middle_name_input, middle)

        if last:
            self.enter_text(self.last_name_input, last)

    # -------------------------------
    # Restricted fields
    # -------------------------------

    def is_field_editable(self, selector):
        return self.page.is_enabled(selector)

    def is_field_editable_by_label(self, label):
        locator = f"xpath=//label[normalize-space()='{label}']/ancestor::div[contains(@class,'oxd-input-group')]//input"
        return self.page.locator(locator).is_editable()

    # -------------------------------
    # Photograph upload
    # -------------------------------

    def upload_photo(self, file_path):
        absolute_path = os.path.abspath(file_path)

        self.page.locator(self.profile_image).click()

        file_input = self.page.locator(self.photo_input)
        file_input.wait_for(state="attached")
        file_input.set_input_files(absolute_path)

        save_btn = self.page.locator(self.save_button)
        save_btn.click()

        try:
            self.page.wait_for_selector(self.upload_success_msg)
            return True
        except:
            self.page.wait_for_selector(self.upload_error_msg)
            return False

    def is_upload_successful(self):
        return self.page.is_visible(self.upload_success_msg)

    def is_upload_failed(self):
        return self.page.is_visible(self.upload_error_msg)

    # -------------------------------
    # Emergency Contacts
    # -------------------------------
    def add_emergency_contact(self, name, relation, home, mobile, work):
        # Open the Add modal
        self.page.click(self.add_button)

        # Scope the modal by its heading to avoid multiple matches
        modal = self.page.locator("div.orangehrm-horizontal-padding", has_text="Save Emergency Contact")

        # Fill the form fields
        modal.locator("xpath=.//label[text()='Name']/ancestor::div[contains(@class,'oxd-input-group')]//input").fill(
            name)
        modal.locator(
            "xpath=.//label[text()='Relationship']/ancestor::div[contains(@class,'oxd-input-group')]//input").fill(
            relation)
        modal.locator(
            "xpath=.//label[text()='Home Telephone']/ancestor::div[contains(@class,'oxd-input-group')]//input").fill(
            home)
        modal.locator("xpath=.//label[text()='Mobile']/ancestor::div[contains(@class,'oxd-input-group')]//input").fill(
            mobile)
        modal.locator(
            "xpath=.//label[text()='Work Telephone']/ancestor::div[contains(@class,'oxd-input-group')]//input").fill(
            work)

        # Click Save
        modal.locator("button[type='submit']").click()


    # -------------------------------
    # Dependants
    # -------------------------------
    def add_dependant(self, name, relationship, dob):
        self.page.click(self.add_button)

        form = self.page.locator("form.oxd-form")
        form.wait_for()

        form.locator("div:has(label:has-text('Name')) input").fill(name)

        form.locator("div:has(label:has-text('Relationship')) .oxd-select-text").click()
        self.page.locator(f"span:has-text('{relationship}')").click()

        dob_input = form.locator("div:has(label:has-text('Date of Birth')) input")
        dob_input.fill(dob)
        dob_input.press("Enter")


    # -------------------------------
    # Immigration
    # -------------------------------

    def add_immigration(self, number):
        self.page.click(self.add_button)

        self.enter_text("xpath=//label[text()='Number']/ancestor::div[contains(@class,'oxd-input-group')]//input", number)

        self.page.click("button[type='submit']")
        return self.wait_for_success_message()

    # -------------------------------
    # Qualifications - Work Experience
    # -------------------------------

    def add_work_experience(self, company):
        self.page.click(self.add_button)

        self.enter_text("//label[normalize-space()='Company']/ancestor::div[contains(@class,'oxd-input-group')]//input", company)
        self.enter_text("//label[normalize-space()='Job Title']/ancestor::div[contains(@class,'oxd-input-group')]//input", "QA Engineer")

        self.page.click("button[type='submit']")
        return self.wait_for_success_message()

    # -------------------------------
    # Qualifications - Education
    # -------------------------------

    def add_education(self, institute, year, major):
        self.page.click('//h6[normalize-space()="Education"]//following-sibling::button')


        self.page.click('//h6[normalize-space()="Add Education"]//following-sibling::form//div[@class="oxd-select-text-input"]')
        # Python Playwright
        self.page.locator('//div[@role="listbox"]//div[normalize-space()="Bachelor\'s Degree"]').click()

        self.enter_text("//label[normalize-space()='Institute']/ancestor::div[contains(@class,'oxd-input-group')]//input", institute)

        self.enter_text(
            "//label[normalize-space()='Year']/ancestor::div[contains(@class,'oxd-input-group')]//input",
            year)
        self.enter_text(
            "//label[normalize-space()='Major/Specialization']/ancestor::div[contains(@class,'oxd-input-group')]//input",
            major)
        self.page.click("//h6[normalize-space()='Add Education']//following-sibling::form//button[normalize-space()='Save']")
        return self.wait_for_success_message()

    # -------------------------------
    # Report-To Section
    # -------------------------------

    def is_supervisors_list_visible(self):
        table = self.page.locator('(//div[@class="oxd-table-body"])[1]')
        table.wait_for(timeout=5000)
        return table.is_visible()


    # -------------------------------
    # Generic Delete
    # -------------------------------

    def delete_record(self, text_value):
        row = self.page.locator(self.table_rows).filter(has_text=text_value)
        row.locator("i.oxd-icon.bi-check").click()

        self.page.click(self.delete_button)
        self.page.click(self.confirm_delete_button)



    # -------------------------------
    # Generic Table Validation
    # -------------------------------

    def is_record_present(self, name):
        table_rows = self.page.locator("div.oxd-table-body div.oxd-table-row")
        count = table_rows.filter(has_text=name).count()
        return count > 0

    # -------------------------------
    # Common Toast Wait
    # -------------------------------

    def wait_for_success_message(self, timeout=5000):
        try:
            self.page.wait_for_selector("text=Successfully Saved", timeout=timeout)
            return True
        except:
            return False

    # -------------------------------
    # Common Input Utility
    # -------------------------------

    def enter_text(self, selector, value):
        locator = self.page.locator(selector)
        locator.wait_for(state="visible")

        if not locator.is_editable():
            raise Exception(f"Field {selector} is not editable")

        locator.click()
        locator.press("Control+A")
        locator.press("Backspace")
        locator.type(value)
