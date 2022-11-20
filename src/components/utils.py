
class Utils:
    """通用工具类
    """

    # 转换日期

    @staticmethod
    def convert_date(dt):
        segments = dt.split('.')
        return segments[0].replace('T', ' ')

    # list转字符串
    @staticmethod
    def concat(separator, data):
        print(data)
        exit
        if isinstance(data, list):
            return separator.join(data)

        return Exception('data type error')
