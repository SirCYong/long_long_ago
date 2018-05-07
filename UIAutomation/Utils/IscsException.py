from selenium.common.exceptions import WebDriverException
__package__ = "IscsUIAutomation"

class IsLoadedException(WebDriverException):
    pass


class PageFactoryException(WebDriverException):
    pass


class InitialPageException(WebDriverException):
    pass


class ParseXmlErrorException(WebDriverException):
    pass


class NoSuchXMLFileException(WebDriverException):
    pass


class PageFactoryNoSuchElementException(WebDriverException):

    pass


class NoSuchEnvironmentException(Exception):
    pass


class UserHasNotRegisterYetException(Exception):
    pass


class SSHConncetionFailedException(Exception):
    pass


class GetCardListFailureException(Exception):
    pass


class LoginFailException(Exception):
    """
    调用requests发送Login请求发生的异常.
    """
    pass


class GlobalSettingErrorException(Exception):
    """
    读取配置文件引发的异常.
    """
    pass


