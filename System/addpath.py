##Incomplete: 已废弃

import os
import winreg


class Win(object):
    def get_desktop_path(self):
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
        desktop_dir = winreg.QueryValueEx(key, "Desktop")[0]
        return desktop_dir

    def ergodic_files(self,path):
        for files in os.walk(path): 
            for file in files: 
                path = os.path.join(file).encode('utf-8')
                flag = path.find('Internet Download Manager')
                if flag == -1:
                    pass
                else:
                    return path



class QuickAccess(object):
    def call_IDM(self):
        desktop_dir = Win().get_desktop_path()    #b'*'
        IDM_path = Win().ergodic_files(path = desktop_dir)
        os.system(IDM_path)

QuickAccess().call_IDM()
#os.system("C:\Users\Lenovo\Desktop\Internet Download Manager.lnk")