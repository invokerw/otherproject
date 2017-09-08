#!/bin/bash
###############################
# 此脚本用来增量备份
# 此文件名：mysqldaily.sh
#
# Author: weifei
#
# 每个星期一到六早上3点做一次增量备份(加 & 为后台执行)
# 0 3 * * 1-6 root /root/backup/mysqldailybackup.sh &
#
# mysql 需要开启 binlog
###############################

#设置用户名和密码
mysql_user="root"
mysql_password="23333"

#mysql安装全路径
mysql_dir=/usr/local/mysql/bin

#备份数据库(多数据库，用逗号隔开)
mysql_databases="test"

#设置备份路径，创建备份文件夹
backup_dir=~/backup/mysql

#binfile的目录
binFile=/var/lib/mysql/mysql-bin.index

#binfile的目录
binLog=/var/lib/mysql/

#备份的时间
today=$(date +%Y%m%d)
now=$(date +%Y%m%d_%H)
full_backup_dir=$backup_dir/$today/$now

#备份日志文件
log_file=daily_backup.log

#开始备份,记录备份开始时间 并压缩备份文件
echo -e '['$(date +"%Y-%m-%d %H:%M:%S")'] - '$mysql_databases' - '"备份开始\n" >> $backup_dir/$log_file

#判断目标目录是否已经存在
if [ ! -d $full_backup_dir ] 
then
    mkdir -p $full_backup_dir
fi
cp $binFile $full_backup_dir

mysqladmin -u$mysql_user -p$mysql_password flush-logs
counter=`wc -l $binFile |awk '{print $1}'`
nextNum=0

for file in `cat $binFile`
do
	base=`basename $file`
	#basename用于截取mysql-bin.00000*文件名，去掉./mysql-bin.000005前面的./
	nextNum=`expr $nextNum + 1`
	if [ $nextNum -eq $counter ]
	then
		echo $base skip! \n>>  $backup_dir/$log_file
		break
	else
		dest=$full_backup_dir/$base
		if [ -e $dest ]
		#test -e用于检测目标文件是否存在，存在就写exist!到$LogFile去。
		then
			echo $base exist! >> $backup_dir/$log_file
		else
			cp $binLog/$base $full_backup_dir
			echo $base copying >> $backup_dir/$log_file
		fi
	fi
done
#备份结束
echo -e '['$(date +"%Y-%m-%d %H:%M:%S")'] - '$mysql_databases' - '"备份结束\n" >> $backup_dir/$log_file

#恢复使用如下命令
#mysqlbinlog --no-defaults mysql-bin.000001 | /usr/bin/mysql -uroot -p123456 test
exit 0


