'''
根据用户名获取账户如下信息：
'identifier', 'username', 'full_name', 'profile_pic_url', 'profile_pic_url_hd', 'biography', 
'external_url', 'follows_count', 'followed_by_count', 'media_count', 'is_private', 'is_verified', 
'medias', 'blocked_by_viewer', 'country_block', 'followed_by_viewer', 'follows_viewer', 
'has_channel', 'has_blocked_viewer', 'highlight_reel_count', 'has_requested_viewer', 
'is_business_account', 'is_joined_recently', 'business_category_name', 'business_email', 
'business_phone_number', 'business_address_json', 'requested_by_viewer', 'connected_fb_page', 
'_is_new', '_is_loaded', '_is_load_empty', '_is_fake', '_modified', '_data', 'modified'
'''

from context import Instagram # pylint: disable=no-name-in-module

# If account is public you can query Instagram without auth
instagram = Instagram()

# For getting information about account you don't need to auth:
account = instagram.get_account('kevin')

# Available fields
print('Account info:')
print('Id', account.identifier)  
print('Username', account.username)  # 用户名
print('Full name', account.full_name) #全名
print('Biography', account.biography) #简介
print('Profile pic url', account.get_profile_picture_url())  #头像图片地址
print('External Url', account.external_url) # 外部链接
print('Number of published posts', account.media_count) #贴子数 
print('Number of followers', account.followed_by_count) # 粉丝数
print('Number of follows', account.follows_count)  #关注数
print('Is private', account.is_private)  # 是否为私密账户
print('Is verified', account.is_verified) # 是否为认证的账户
