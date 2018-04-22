from utils.cmd import Cmd
from utils.port import Port
import threading


class AppiumServer(object):
    def __init__(self):
        self.cmd = Cmd()
        self.uuid_list = self.get_uuid()

    def get_uuid(self):
        """
            获取设备uuid
        :return:
        """
        devices_list = []
        result_list = self.cmd.excute_cmd_result('adb devices')
        if len(result_list) >= 2:
            for i in result_list:
                if 'List' in i:
                    continue
                devices_info = i.split('\t')
                if devices_info[1] == 'device':
                    devices_list.append(devices_info[0])
            return devices_list
        else:
            return None

    def create_port_list(self, start_port):
        """
            创建可用的端口
        :return:
        """
        port = Port()
        port_list = port.get_ports(start_port, len(self.uuid_list))
        return port_list

    def create_command_list(self, i):
        """
            生成执行命令
        :param i:
        :return:
        """
        command_list = []
        appium_port_list = self.create_port_list(4700)
        bootstrap_port_list = self.create_port_list(4900)
        command = "appium -p" + str(appium_port_list[i]) + " -bp " + str(bootstrap_port_list[i]) + " -U " + \
                  self.get_uuid()[i]
        command_list.append(command)
        return command_list

    def start_server(self, i):
        """
            启动服务
        :param i:
        :return:
        """
        start_list = self.create_command_list(i)
        self.cmd.excute_cmd(start_list[0])

    def get_pid(self, port):
        """
            根据端口,获取pid
        :param port:
        :return:
        """
        get_cmd = "lsof -i:" + str(port)
        excute_result = self.cmd.excute_cmd_result(get_cmd)
        if excute_result == []:
            return None
        else:
            pid = excute_result[1].split(' ')[2]
            return pid

    def kill_server(self):
        """
            杀掉进程
        :param port:
        :return:
        """
        appium_port_list = self.create_port_list(4700)
        bootstrap_port_list = self.create_port_list(4900)
        port_list = appium_port_list+bootstrap_port_list
        for port in port_list:
            pid = self.get_pid(port)
            if pid != None:
                kill_cmd = "kill -9 " + pid
                self.cmd.excute_cmd(kill_cmd)

    def main(self):
        self.kill_server()
        for i in range(len(self.get_uuid())):
            appium_start = threading.Thread(target=self.start_server, args=(i,))
            appium_start.start()


if __name__ == '__main__':
    appium_server = AppiumServer()
    appium_server.main()
