from common_utils import CommonUtils

if __name__ == '__main__':
    req_url = "https://www.iesdouyin.com/share/video/7399839202264763686/?region=CN&mid=6727959010609203201&u_code=m66l0am9&did=MS4wLjABAAAAhQWjbJuTldEs8krsI_7u9MZ2Eeqa6PK_8YSFd-I4Qjg&iid=MS4wLjABAAAAtC9e1J62DjGhRPFVMHfFie8Ep02NB3oewIo90djacNo&with_sec_did=1&titleType=title&share_sign=sXTi6dfBe3Ia.Onp3I1jBDjlqBhGESFMfvlqdASyYWg-&share_version=300800&ts=1723085591&from_aid=1128&from_ssr=1&utm_source=copy&utm_campaign=client_share&utm_medium=android&app=aweme&activity_info=%7B%22social_author_id%22%3A%22427085977355711%22%2C%22social_share_id%22%3A%2275838875692_1723085613070%22%2C%22social_share_time%22%3A%221723085613%22%2C%22social_share_user_id%22%3A%2275838875692%22%7D"
    xbogus = CommonUtils().get_xbogus(req_url,"ddd")
    print(xbogus)
