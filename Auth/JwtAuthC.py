# -*- coding: utf-8 -*-
# by dl
import datetime
import jwt
import time
from commonClass.PrintExpectC import PrintExpect

from Config import config

__author__ = "DL"


class JwtAuth:
    """
    JWT用户验证
    """

    @staticmethod
    def encode_auth_token(user_id, login_time):
        """
        生成认证Token
        :param user_id: <id>
        :param login_time: int(timestamp)
        :return: string
        """
        # 签发时间 此处用的是国际时间
        iat = datetime.datetime.utcnow()
        # 过期时间
        exp = iat + datetime.timedelta(days=0,
                                       seconds=config.login_life_time)

        try:
            payload = {
                # 签发时间
                'iat': iat,
                # 过期时间
                'exp': exp,
                # token签发者
                'iss': 'DL',
                # 实际数据
                'data': {
                    # 用户id
                    'user_id': user_id,
                    # 登录时间
                    'login_time': login_time,
                }
            }
            return jwt.encode(
                    # 数据载荷
                    payload,
                    # 秘钥
                    config.jwt_secret,
                    # 加密方式
                    algorithm='HS256').decode()
        except:
            return PrintExpect.p_e()

    @staticmethod
    def decode_auth_token(auth_token):
        """
        验证Token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(
                # token值
                auth_token,
                # 秘钥
                config.jwt_secret,
                # 和过去时间对比的余地量 可能是为了容错一些时间偏差
                # leeway=datetime.timedelta(seconds=10)
            )
            # 不验证是否过期
            # payload = jwt.decode(auth_token, config.jwt_secret, options={'verify_exp': True})
            # 键值检查
            if ('data' in payload and 'user_id' in payload['data']):
                return payload
            else:
                raise jwt.InvalidTokenError

        except jwt.ExpiredSignatureError:

            return 'OSR-BearerToken 过期'

        except jwt.InvalidTokenError:
            return '非法 OSR-BearerToken'


if __name__ == '__main__':
    # 加密
    auth_token = JwtAuth.encode_auth_token(123, int(time.time()))
    print(auth_token)

    res = JwtAuth.decode_auth_token(auth_token)
    print(res)
