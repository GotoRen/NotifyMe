#!/bin/sh

# バックアップファイルを何日分残しておくか
period='+120'

#バックアップファイルを何日後に作成するか
period2='+30'

# バックアップファイルを保存するディレクトリ
dirpath='/home/pi/Img/*.jpg'

#バックアップ元フォルダ
backupfolder='/home/pi/Notify_img_backup'

# ファイル名を定義(※ファイル名で日付がわかるようにしておきます)
mydate=`date +%y%m%d%H%M%S`
filename="images_$mydate.tar.gz"
#backup実行
find $dirpath -type f -mtime $period2 -name "*.jpg*" ! -name "*.gz" | xargs -I {} sh -c 'gzip {} && mv {}.gz $backupfolder'

# パーミッション変更
chmod -R 700 $dirpath
# 古いバックアップファイルを削除

find $dirpath -type f -mtime $period -exec rm {} \;