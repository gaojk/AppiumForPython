from utils.cmd import Cmd


class Port(object):
    def port_is_used(self, port_num):
        """
            判断端口是否被占用
        :param port_num:
        :return:
        """
        self.cmd = Cmd()
        command = 'lsof -i:' + str(port_num)
        result = self.cmd.excute_cmd_result(command)
        if len(result) > 0:
            flag = True
        else:
            flag = False

        return flag

    def get_ports(self, start_port, count):
        """
            生成可用端口号
        :param start_port:
        :param count:
        :return:
        """
        port_list = []
        if count != None:
            while len(port_list) != count:
                if self.port_is_used(start_port) != True:
                    port_list.append(start_port)
                start_port = start_port + 1

        return port_list


if __name__ == '__main__':
    port = Port()
    print(port.port_is_used(4723))
    print(port.get_ports(4723, 2))
