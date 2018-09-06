# !/uer/bin/env python3
# coding=utf-8
from base.apper import Apper
from base.test_runner import TestRunner
from base.base_assert import TestCase
from base.run_sql import GetData
from base.log import LOGGER
from base.my_exception import MyException
from parameterized import parameterized


class MainProcess(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = Apper()

    @classmethod
    def tearDownClass(cls):
        pass

    @parameterized.expand([('18515966636', '123456', '微信'), ])
    def test_android_main(self, phone, pwd, pay_op):
        """测试android主流程:"""
        self.android_element_wait("id", "com.czb.chezhubang:id/guide_image")
        self.swipe_left()
        self.swipe_left()
        self.android_element_wait("id", "com.czb.chezhubang:id/button")
        close_lunch_button = self.driver.find_element_by_android_uiautomator('new UiSelector().text("立即体验")')
        close_lunch_button.click()
        self.click("class=>android.widget.RelativeLayout")
        self.click("class=>android.widget.RelativeLayout")
        self.click("css=>#com.czb.chezhubang:id/add_Oil_btn")
        if self.android_element_wait("id", "com.czb.chezhubang:id/ad_close"):
            self.click("id=>com.czb.chezhubang:id/ad_close")
        self.driver.switch_to.alert().accept()
        gas_list = self.driver.find_element_by_id("id=>com.czb.chezhubang:id/recyclerView").text
        print(gas_list)
        self.compel_waiting(10)
        self.quit_()

    # @parameterized.expand([('01', '18515966636', '123456', '微信'), ])
    # def test_ios_logout_main(self, phone, pwd, pay_op):
    #     self.sys_alert()
    #     # ios模拟器测试时需要注释掉下边这行代码，因为真机会弹2个权限
    #     # self.sys_alert()
    #     self.compel_waiting(2)
    #     self.swipe_left()
    #     self.compel_waiting(1)
    #     self.swipe_left()
    #     self.get_element_by_ios_predicate_('name == "立即体验"').click()
    #     if self.get_element_by_ios_predicate_('name == "login close"'):
    #         self.get_element_by_ios_predicate_('name == "login close"').click()
    #     self.compel_waiting()
    #     self.tap_([(100, 20)], 500)
    #     self.tap_([(100, 20)], 500)
    #     self.compel_waiting()
    #     self.get_element_by_ios_predicate_('name == "guide openMode"').click()
    #     self.get_element_by_ios_predicate_('name == "wxm预存商户一级下油站"').click()
    #     self.find_accessibility_id("付油费").click()
    #     login = self.driver.find_elements_by_ios_predicate('type == "XCUIElementTypeTextField"')
    #     login[0].clear()
    #     login[0].send_keys(phone)
    #     self.driver.find_element_by_ios_predicate('name == "获取验证码"').click()
    #     msg = GetData().get_msg(phone)
    #     login[1].send_keys(msg)
    #     self.driver.find_element_by_ios_predicate('name == "登录"').click()
    #     self.find_accessibility_id("付油费").click()
    #     if self.driver.find_element_by_ios_predicate("name == '继续支付'"):
    #         self.driver.find_element_by_ios_predicate('name == "继续支付"').click()
    #     self.driver.find_element_by_ios_predicate("name == '1号枪'").click()
    #     amount_input = self.driver.find_element_by_ios_predicate("type == 'XCUIElementTypeTextField'")
    #     amount_input.clear()
    #     amount_input.send_keys("100")
    #     self.driver.find_element_by_ios_predicate("name == '确定'").click()
    #     # 余额支付
    #     if pay_op == '余额':
    #         LOGGER.info("---余额支付---")
    #         if self.driver.find_element_by_ios_predicate("name == 'pay-option-selected'").is_selected():
    #             pass
    #         else:
    #             self.driver.find_element_by_ios_predicate("name == 'pay-option-selected'").click()
    #             if not self.driver.find_element_by_ios_predicate("name == 'pay-option-selected'").is_selected():
    #                 LOGGER.warning("余额不足！或超过当日限额！")
    #                 self.assertTrue("余额支付失败", "余额不足！或超过当日限额！")
    #         j = 0
    #         for i in pwd:
    #             self.driver.find_elements_by_ios_predicate("type == 'XCUIElementTypeOthe'")[j].click()
    #             if self.driver.find_element_by_ios_predicate("name == '设置'"):
    #                 self.driver.find_element_by_ios_predicate("name == '设置'").click()
    #                 self.driver.find_element_by_ios_predicate("name == '获取验证码'").click()
    #                 msg = GetData().get_msg(phone)
    #                 self.driver.find_elements_by_ios_predicate("type == 'XCUIElementTypeTextField'")[1].send_keys(msg)
    #                 pwd_input = self.driver.find_elements_by_ios_predicate("type == 'XCUIElementTypeSecureTextField'")
    #                 pwd_input[0].send_keys(pwd)
    #                 pwd_input[1].send_keys(pwd)
    #                 self.driver.find_element_by_ios_predicate("name == '确定'").click()
    #             self.driver.find_elements_by_ios_predicate("type == 'XCUIElementTypeOthe'")[j].send_keys(i)
    #             j += 1
    #         self.driver.find_element_by_ios_predicate("name == '去支付'").click()
    #         self.assertEqual()
    #     # 微信支付
    #     elif pay_op == '微信':
    #         LOGGER.info("---微信支付---")
    #         if self.driver.find_element_by_ios_predicate('name == "pay-option-selected"').is_selected():
    #             self.driver.find_element_by_ios_predicate('name == "pay-option-selected"').click()
    #         self.driver.find_element_by_ios_predicate('name == "去支付"').click()
    #         if self.driver.find_element_by_ios_predicate('name == "微信支付"').is_selected():
    #             pass
    #         else:
    #             self.driver.find_element_by_ios_predicate('name == "微信支付"').click()
    #         self.driver.find_element_by_ios_predicate('name == "确定支付"').click()
    #         if self.driver.switch_to_alert.text():
    #             self.assertIn("安装微信", self.driver.switch_to_alert.text(), "没安装微信，支付失败!")
    #         else:
    #             pass
    #             # 微信页面
    #     else:
    #         LOGGER.info("---支付宝支付---")
    #         if self.driver.find_element_by_ios_predicate('name == "pay-option-selected"').is_selected():
    #             self.driver.find_element_by_ios_predicate('name == "pay-option-selected"').click()
    #         self.driver.find_element_by_ios_predicate('name == "去支付"').click()
    #         if self.driver.find_element_by_ios_predicate('name == "支付宝支付"').is_selected():
    #             pass
    #         else:
    #             self.driver.find_element_by_ios_predicate('name == "支付宝支付"').click()
    #         self.driver.find_element_by_ios_predicate('name == "确定支付"').click()
    #         # 吊起支付宝h5
    #     self.compel_waiting(10)
    #     self.quit_()


if __name__ == '__main__':
    num = 0
    while True:
        run = TestRunner('./', '车主邦测试用例', '测试环境：{}', 'Medivh'.format("ios"))
        run.debug()
        num += 1
        if num == 20:
            break

'''
说明：
'./' ： 指定测试目录。
'百度测试用例' ： 指定测试项目标题。
'测试环境：android' ： 指定测试环境描述(注：这里的设备是自动获取，请填写准确)。
'Medivh': 测试人员

debug() # debug模式不生成测试报告
run()   # run模式生成测试报告
'''
