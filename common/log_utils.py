import  os
import  logging

current_path=os.path.dirname(__file__)
log_path=os.path.join(current_path,'../logs/test.log')

class LogUtils():
    def __init__(self,log_path=log_path):
        self.log_path=log_path
        self.logger = logging.getLogger(__name__)  # 创建一个日志对象
        self.logger.setLevel(level=logging.INFO)  # 设置日志级别
        file_log = logging.FileHandler(self.log_path,encoding='utf8')
        formatter = logging.Formatter('file:%(asctime)s - %(name)s - %(levelname)s: %(message)s')
        file_log.setFormatter(formatter)
        self.logger.addHandler(file_log)

    def info(self,message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

# #优化日志，添加一个logger对象
logger=LogUtils()

if __name__=='__main__':
    logger=LogUtils()
    logger.info('新梦想软件测试P5班')

