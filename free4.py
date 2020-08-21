import os
import time
import random

import fire


class go():
    def compress(self, 文件名):
        几十秒 = random.randint(10, 90)
        time.sleep(几十秒)
        os.remove(文件名)
        主名, 扩展名 = os.path.splitext(文件名)
        open(f'{主名}.rimo', 'w')
        print('亚索好了。')

    def decompress(self, 文件名):
        print('自己重写一遍吧，我想不起来怎么解压了！')


fire.Fire(go)
