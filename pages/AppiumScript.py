from selenium.webdriver.common.by import By
from Capabilities import app_driver

class Autorize_methods:

    def autorization(self):
        app_driver.implicitly_wait(20)
        # app_driver.find_element(By.ID, S_Locators.btn_skip()).click()
        # app_driver.find_element(By.ID, S_Locators.edit_phone()).send_keys('958584490')
        # app_driver.find_element(By.ID, S_Locators.check_private()).click()
        # app_driver.find_element(By.ID, S_Locators.button_ok()).click()
        # app_driver.find_element(By.ID, S_Locators.pass_edit_code())
        # app_driver.press_keycode(7)
        # app_driver.press_keycode(7)
        # app_driver.press_keycode(8)
        # app_driver.press_keycode(13)
        # app_driver.implicitly_wait(10)
        # app_driver.find_element(By.ID, S_Locators.button_ok()).click()
        # app_driver.implicitly_wait(20)
        # text_info = app_driver.find_element(By.ID, S_Locators.info_on_page())
        # text = text_info.text
        # assert text_info.is_displayed(), 'Text is not displayed'
        # assert "Тепер ви можете користуватися перевагами Власного Рахунку у вашому додатку" in text, 'Incorrect text'
        # app_driver.find_element(By.ID, S_Locators.button_ok()).click()
        # app_driver.implicitly_wait(40)
        # app_driver.find_element(By.ID, S_Locators.btn_next()).click()

    def close_app(self):
        app_driver.close_app()


    def click_ok_button(self):
        app_driver.find_element(By.ID, S_Locators.button_ok()).click()
        app_driver.implicitly_wait(40)
        app_driver.find_element(By.ID, S_Locators.btn_next()).click()


    def bonus_widget(self):
        bonus = app_driver.find_element(By.ID, M_Locators.bonus())
        if bonus.is_enabled() == True:
            bonus_info = app_driver.find_element(By.ID, M_Locators.bonus_value())
            value= bonus_info.text
            print(value)
            bonus_units = app_driver.find_element(By.ID, M_Locators.bonus_units())
            units = bonus_units .text
            print(units)
            text = value + units
            print(text)
            return text
        else:
            print('NO BONUS ELEMENT')

    def rlpoints_widget(self):
        rl_points = app_driver.find_element(By.ID, M_Locators.rl_poins())
        if rl_points.is_enabled() == True:
            points_info = app_driver.find_element(By.ID, M_Locators.rl_points_info())
            text = points_info.text
            print(text)
            return text
        else:
            print('NO RL_POINTS ELEMENT')

    def get_height(self):
        size = app_driver.find_element_by_id('ua.silpo.android.mtest:id/nestedScrollView').size
        print(size)
        for key in size.keys():
            if key=='height':
                self.height = size[key]
                height = self.height
                print(height)
                return height

    def get_horisontal_height(self):
        size = app_driver.find_element_by_id('ua.silpo.android.mtest:id/nestedScrollView').size
        print(size)
        for key in size.keys():
            if key=='height':
                self.height = size[key]
                height = self.height
                print(height)
                return height


    def get_width(self):
        size = app_driver.find_element_by_id('ua.silpo.android.mtest:id/nestedScrollView').size
        print(size)
        for key in size.keys():
            if key=='width':
                self.width = size[key]
                width = self.width
                print(width)
                return width

    def get_horisontal_width(self):
        size = app_driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView[1]').size
        print(size)
        for key in size.keys():
            if key=='width':
                self.width = size[key]
                width = self.width
                print(width)
                return width

    def find_width_from_location(self):
        wind = app_driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView[1]')
        location = wind.location
        print(location)
        for key in location.keys():
            if key=='y':
                self.width = location[key]
                width = self.width
                print(width)
                return width

    def scroll(self):
        print('START SCROLL')
        width = Autorize_methods.get_width(self)
        start_width = int(width * 0.5)
        print(start_width)
        end_width = int(width * 0.5)
        print(end_width)
        height = Autorize_methods.get_height(self)
        start_height = int(height)
        print(start_height)
        end_height = int(height * 0.5)
        print(end_height)
        window = app_driver.find_element_by_id('ua.silpo.android.mtest:id/nestedScrollView')
        app_driver.implicitly_wait(20)
        app_driver.swipe(start_width, start_height,end_width,end_height,500)


    def horisontal_scroll(self):
        print('START HORISONTAL SCROLL')
        width = Autorize_methods.find_width_from_location(self)
        start_width = int(width * 0.2)
        print(start_width)
        end_width = int(width * 0.8)
        print(end_width)
        # height = Autorize_methods.get_height(self)
        # start_height = int(height * 0.5)
        # print(start_height)
        # end_height = int(height * 0.5)
        # print(end_height)
        app_driver.implicitly_wait(10)
        app_driver.swipe(1006, width, 74, width)















