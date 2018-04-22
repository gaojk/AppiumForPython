from utils.read_ini import ReadIni


class GetByLocal(object):

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, file_path, section, key):
        read_ini = ReadIni(file_path)
        local = read_ini.get_value(section, key)
        by = local.split('>')[0]
        local_by = local.split('>')[1]
        if by == 'id':
            return self.driver.find_element_by_id(local_by)
        elif by == 'className':
            return self.driver.find_element_by_class_name(local_by)
        else:
            return self.driver.find_element_by_xpath(local_by)
