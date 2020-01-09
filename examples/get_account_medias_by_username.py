'''
根据username获取所有的帖子，保存每一个帖子的图像地址以及创建的时间，帖子内容
'''
from context import Instagram # pylint: disable=no-name-in-module
from datetime import datetime
import pymongo

client = pymongo.MongoClient(host='localhost', port=27017) #连接本地mongodb数据库
DATABASE = client["Instagram_users"] 
USERS = [ 'total','unilever', 'volkswagen', 'orange']
#'adidas', 'airbus', 'allianz', 'amadeusitgroup', 'abinbev', 'asmlcompany', 'axa', 'bbva',
#'santander_es', 'basf_global', 'bayerofficial', 'bmwgroup', 'bnpparibas', 'daimler_ag',
#'deutscheboersegroup', 'deutschepost', 'deutschetelekom', 'enelgroup', 'engie',
#'eni', 'essilor', 'luxottica', 'fresenius.group', 'iberdrola', 'intesasanpaolo', 
#'kering_official', 'lindeplc', 'loreal','lvmh', 'nokia', 'philips', 'safran_group',
#'sanofi', 'sap', 'schneiderelectric', 'siemens', 'societegenerale', 'telefonica', 

instagram = Instagram()

for oneUser in USERS:
    print ('get %s data from instagram'% oneUser)
    collection = DATABASE[oneUser]
    account = instagram.get_account(oneUser) #获取账户信息
    postNum = account.__dict__['media_count']  #所有帖子的数量
    
    medias = instagram.get_medias(oneUser, postNum) #获取所有的帖子
    medias_List = []
    for one in reversed(medias):  #按照时间排列顺序插入
        oneDict = {}
        createdTime = one.__dict__['created_time']  #创建的时间   
        oneDict['publishedAt_utc'] = datetime.utcfromtimestamp(createdTime)
        oneDict['content'] = one.__dict__['caption']
        oneDict['url'] = one.__dict__['link']
        oneDict['urlToImage'] = one.__dict__['image_high_resolution_url']
        medias_List.append(oneDict)

    collection.insert_many(medias_List)

# print('Username', account.username)
# print('Full Name', account.full_name)
# print('Profile Pic Url', account.get_profile_picture_url_hd())


# If account private you should be subscribed and after auth it will be available

# username = ''
# password = ''
# session_folder = ''
# instagram = Instagram()
# instagram.with_credentials(username, password, session_folder)
# instagram = Instagram()
# instagram.login()
# instagram.get_medias('private_account', 100)
