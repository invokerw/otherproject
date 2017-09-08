#!/bin/bash
###############################
# 此脚本用来增量备份
# 此文件名：mysqldailybackup.sh
#
# Author: weifei
# 每个星期一到六早上3点做一次增量备份(加 & 为后台执行)
# 0 3 * * 1-6 root /root/backup/mysqldailybackup.sh &
#
# 不使用mysqlbinlog来做增量备份的原因：mysql启动后会产生mysql-bin这样的文件，每启动一次，就会增加一个或者多个。
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
full_backup_dir=$backup_dir/daily_backup

#备份的时间
today=$(date +%Y%m%d_%H%M%S)

#备份日志文件
log_file=daily_backup.log

#只保留最近10个星期的备份（其他删除）
time=$(date "-d 70 day ago" +"%Y-%m-%d %H:%M:%S")

#开始备份,记录备份开始时间 并压缩备份文件
echo -e '['$(date +"%Y-%m-%d %H:%M:%S")'] - '$mysql_databases' - '"备份开始\n" >> $backup_dir/$log_file

#判断目标目录是否已经存在
if [ ! -d $full_backup_dir ] 
then
    mkdir -p $full_backup_dir
fi

echo -e '['$(date +"%Y-%m-%d %H:%M:%S")'] - '$mysql_databases' - '"备份并压缩备份文件\n" >> $backup_dir/$log_file
#--apply-slave-statements 一样先注释
#备份INNODB 使用下面代码 并压缩备份文件
mysqldump -u$mysql_user -p$mysql_password --master-data=2 --single-transaction --flush-logs --databases $mysql_databases | gzip > $full_backup_dir/$today.sql.gz

#备份MyISAM 使用下面代码
#$mysql_dir/mysqldump -u$mysql_user -p$mysql_password --apply-slave-statements --master-data=2 --lock-all-tables --flush-logs  --databases $mysql_databases | gzip > $full_backup_dir/$today.sql.gz

#找出70天前备份的文件，然后删除
echo -e '['$(date +"%Y-%m-%d %H:%M:%S")'] - '$mysql_databases' - '"删除10星期前的备份\n" >> $backup_dir/$log_file
for file in `find -not -type d -mtime +70`
do
    rm -rf $file
done
