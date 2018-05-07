__package__ = "IscsUIAutomation"

# -----------------------------------------------------------------------------
# CONFIGURATION DATA TYPES:
# -----------------------------------------------------------------------------
class LogLevel(object):
    pass


class CitConfiguration(object):
    def __init__(self):
        self.url_Base = 'http: // 192.168.6.31:8080 / base /'
        self.Labor = 'http: // 192.168.6.31:8180 / labor /'
        self.Warehouse = 'http: // 192.168.6.31:8280 / warehouse /'
        self.Transportation = 'http: // 192.168.6.31:8380 / transportation /'
        self.Supply = 'http: // 192.168.6.31:8480 / supply /'
        self.Sales = 'http: // 192.168.6.31:8580 / sales /'
        self.DataSync = 'http: // 192.168.6.31:9180 / datasync /'
    pass


class DT1Configuration(object):
    def __init__(self):
        self.url_Base = 'http: // 192.168.6.24:8080 / base /'
        self.Labor = 'http: // 192.168.6.24:8180 / labor /'
        self.Warehouse = 'http: // 192.168.6.24:8280 / warehouse /'
        self.Transportation = 'http: // 192.168.6.24:8380 / transportation /'
        self.Supply = 'http: // 192.168.6.24:8480 / supply /'
        self.Sales = 'http: // 192.168.6.24:8580 / sales /'
        self.DataSync = 'http: // 192.168.6.24:9180 / datasync /'
    pass


class DT2Configuration(object):
    def __init__(self):
        self.url_Base = 'http: // 192.168.6.25:8080 / base /'
        self.Labor = 'http: // 192.168.6.25:8180 / labor /'
        self.Warehouse = 'http: // 192.168.6.25:8280 / warehouse /'
        self.Transportation = 'http: // 192.168.6.25:8380 / transportation /'
        self.Supply = 'http: // 192.168.6.25:8480 / supply /'
        self.Sales = 'http: // 192.168.6.25:8580 / sales /'
        self.DataSync = 'http: // 192.168.6.25:9180 / datasync /'
    pass


class DT3Configuration(object):
    def __init__(self):
        self.url_Base = 'http: // 192.168.6.30:8080 / base /'
        self.Labor = 'http: // 192.168.6.30:8180 / labor /'
        self.Warehouse = 'http: // 192.168.6.30:8280 / warehouse /'
        self.Transportation = 'http: // 192.168.6.30:8380 / transportation /'
        self.Supply = 'http: // 192.168.6.30:8480 / supply /'
        self.Sales = 'http: // 192.168.6.30:8580 / sales /'
        self.DataSync = 'http: // 192.168.6.30:9180 / datasync /'
    pass