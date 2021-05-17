#!/bin/sh

# バックアップファイルを何日分残すか
period='+120'

# 何日後にバックアップファイルを作成するか
period2='+30'

# バックアップファイルを保存するディレクトリ
dirpath='/home/pi/Img/*.jpg'

# バックアップするフォルダ
backupfolder='/home/pi/Notify_img_backup'

# ファイル名: 日付
mydate=`date + %y%m%d%H%M%S`
filename="images_$mydate.tar.gz"

# 実行
find $dirpath -type f -mtime $period2 -name "*.jpg*" ! -name "*.gz" | xargs -I {} sh -c 'gzip {} && mv {}.gz $backupfolder'
chmod -R 700 $dirpath
find $dirpath -type f -mtime $period -exec rm {} \;
