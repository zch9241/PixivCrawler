import socket
import socks

class proxy(object):
    def socks(self):
        try:
            socks.set_default_proxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 10808)
            socket.socket = socks.socksocket
            
        except ValueError:
            print("[proxy(fetal)]: ValueError: 请检查代理状态是否为PAC，而非Http;请确定v2rayN版本为 3.27;请检查shadowsocks端口")
        except:
            print('[proxy(fetal)]: 未知错误...')
