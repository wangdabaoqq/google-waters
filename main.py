'''
Author: baobaobao
Date: 2025-03-03 11:30:47
LastEditTime: 2025-03-03 22:15:34
LastEditors: baobaobao
'''
from auth.google_login import login_google
from DrissionPage import Chromium, ChromiumOptions
from operations.faucet import faucet
from time import sleep
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    """每日自动化任务"""
    try:
        logger.info("任务启动 - 浏览器初始化")
        co = ChromiumOptions()
        co.headless()  # 无头模式
        browser = Chromium(co)
        tab_login = browser.latest_tab
        
        # 谷歌登录
        logger.info("正在执行谷歌登录...")
        login_google(tab_login)
        
        # 获取最新标签页（登录后的页面）
        faucet_tab = browser.latest_tab
        
        # 执行水龙头操作
        logger.info("正在执行水龙头操作...")
        faucet(faucet_tab)
        
    except Exception as e:
        logger.error(f"任务执行失败: {str(e)}", exc_info=True)
    finally:
        if 'browser' in locals():
            browser.quit()
            logger.info("浏览器已关闭")


def schedule_job():
    """定时任务配置"""
    scheduler = BlockingScheduler(timezone=pytz.timezone('Asia/Shanghai'))
    
    # 每天 23:00 执行 (可根据需要修改 hour 和 minute)
    scheduler.add_job(
        main,
        'cron',
        hour=23,
        minute=0,
        name='daily_faucet_task'
    )
    
    try:
        logger.info("定时任务已启动，等待每天 23:00 执行...")
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        logger.info("定时任务已终止")
        
    except Exception as e:
        logger.error(f"调度器异常: {str(e)}", exc_info=True)  

if __name__ == '__main__':
  main()
