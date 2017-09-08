#!/bin/bash
###############################
# 此脚本用来全量备份
# 此文件名：mysqlfullbackup.sh
#
# Author: weifei
#
# 每个星期日早上3点做一次全量备份(加 & 为后台执行)
# 0 3 * * * root /root/backup/mysqlfullbackup.sh &
###############################

#设置用户名和密码
mysql_user="root"
mysql_password="23333"

#mysql安装全路径
mysql_dir=/usr/local/mysql/bin

#备份数据库(多数据库，用逗号隔开)
mysql_databases="test"

#设置备份路径，创建备份文件夹
[ -d ~/backup/mysql ] || mkdir ~/backup/mysql
backup_dir=~/backup/mysql

#备份的时间
today=$(date +%Y%m%d)
#_%H%M%S)
full_backup_dir=$backup_dir/$today

#备份日志文件
log_file=full_backup.log

#只保留最近10个星期的备份（其他删除）
time=$(date "-d 70 day ago" +%Y-%m-%d\ %H:%M:%S)

#开始备份,记录备份开始时间 并压缩备份文件
echo -e '['$(date +"%Y-%m-%d %H:%M:%S")'] - '$mysql_databases' - '"备份开始\n" >> $backup_dir/$log_file

#判断目标目录是否已经存在
if [ ! -d $full_backup_dir ] 
then
    mkdir -p $full_backup_dir
fi
echo -e '['$(date +"%Y-%m-%d %H:%M:%S")'] - '$mysql_databases' - '"备份并压缩备份文件\n" >> $backup_dir/$log_file

#备份INNODB 使用下面代码 并压缩备份文件
#mysqldump -u$mysql_user -p$mysql_password --apply-slave-statements --hex-blob --routines --single-transaction --databases $mysql_databases | gzip > $full_backup_dir/$today.sql.gz

#mysqldump -uroot -p${mysql_password} --add-drop-database --all-databases --all-tablespaces --routines --lock-all-tables | gzip > ${backup_dir}/${today}.sql.gz
#[ $? -eq 0 ] && echo -e '['$(date +"%Y-%m-%d %H:%M:%S")'] - 'All DB' - '"备份并压缩备份文件 OK!!!\n" >> $backup_dir/$log_file

#备份MyISAM 使用下面代码
#--apply-slave-statements 先去掉这个 slave 如果之后有需要再加
mysqldump -u$mysql_user -p$mysql_password  --hex-blob --routines --lock-all-tables --flush-logs --delete-master-logs --databases $mysql_databases | gzip > $full_backup_dir/$today.sql.gz
[ $? -eq 0 ] && echo -e '['$(date +"%Y-%m-%d %H:%M:%S")'] - '$mysql_databases' - '"备份并压缩备份文件 OK!!!\n" >> $backup_dir/$log_file



#恢复

#mysql -u$mysql_user -p$mysql_password basename < a.sql
