lua 包 5.1.4
tolua++ 包 1.0.93 对应处理5.1.4

*1.安装lua*
    解压 lua 包，
    make linux
    make install //可选
   
*2.yum 安装 scons //类似于make*

*3.安装tolua++*
    解压（修改文件名，把空格去掉）
    修改配置
        vim config_linux.py
    找到
        LIBS = ['lua50', 'lualib50', 'dl', 'm']
    改为
        LIBS = ['lua', 'dl', 'm']
    设置 lua 头文件地址
        LINKFLAGS = ['-I../lua-5.1.4/src', '-g', '-ansi', '-Wall']
        CCFLAGS = ['-I../lua-5.1.4/src', '-O2', '-ansi', '-Wall'] 
    编译
        scons all
    安装
        scons install
