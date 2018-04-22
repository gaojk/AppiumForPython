import os


class Cmd(object):
    def excute_cmd_result(self, command):
        """
            获取执行命令
        :param command:
        :return:
        """
        result_list = []
        result = os.popen(command).readlines()
        for i in result:
            if i == '\n':
                continue
            result_list.append(i.strip('\n'))
        return result_list

    def excute_cmd(self, command):
        """
            命令执行
        :param command:
        :return:
        """
        os.system(command)


if __name__ == '__main__':
    cmd = Cmd()
    print(cmd.excute_cmd_result('adb devices'))
