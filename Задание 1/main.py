#ссылка на github: https://github.com/Alexia-w-creator/VKPlay
import os
import ctypes
#путь к файлу с настройками Dota
file = r'C:\Program Files (x86)\Steam\steamapps\common\Underlords\game\dac\cfg\video.txt'
#возможные разрешения экрана
graf = (('800', '600'), ('1024', '768'), ('1280', '720'), ('1366', '768'), ('1920', '1080'))

def setNewRes(file):
    getSettingFromFile(file)

#функция нахождения старого разрешения
def findOldRes(oldData):
    for i in range(0, len(graf)):
        for j in range(0, len(graf[i])):
            index = oldData.find(graf[i][j])
            if(index != -1):
                oldRes = graf[i][j]
                oldRes1 = graf[i][:]
    return oldRes1

#функция обновления разрешения в файле
def update(oldData, file):

    oldRes = findOldRes(oldData)
    new_sett = systemMetrics()

    with open(file, 'r') as f:
        old_data = f.read()
    new_data = old_data.replace(oldRes[0], str(new_sett[0]))
    new_data = new_data.replace(oldRes[1], str(new_sett[1]))
    with open(file, 'w') as f:
        f.write(new_data)

#функция находит расположение настроек расширения в файле и обновляет данне
#если настройки не найдены, то возвращается сообщение об отсутствии данных
def getSettingFromFile(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        oldData = ""

        for line in lines:
            line = line.strip()
            if line.startswith('"setting.defaultres"'):
                oldData = line
                update(oldData, file)

        if(oldData == ""):
            print("Not data found")

#функция получения резрешения экрана пользователя
def systemMetrics():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
    return [w, h]


if __name__ == '__main__':
    setNewRes(file)

    os.system(r'start C:\"Program Files (x86)"\Steam\steam.exe')


