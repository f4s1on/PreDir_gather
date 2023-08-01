# dir_gather
处理当前已知接口获取网站前置目录，将结果作为其他目录扫描工具的扫描目标

如：从burp的HTTP history中Copy URLs得到:

    https://test.com/aaa/bbb/ccc/ddd
    https://test.com/eee/fff/ggg/hhh
保存到url.txt运行脚本得到结果:

    https://test.com/aaa/
    https://test.com/aaa/bbb/
    https://test.com/aaa/bbb/ccc/
    https://test.com/eee/fff/ggg/
    https://test.com/eee/
    https://test.com/
    https://test.com/eee/fff/    
