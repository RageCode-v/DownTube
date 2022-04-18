from kivy.utils import platform

if platform == 'android':
    from plyer.facades.notification import Notification


    def notbar(name, percent, nah):
        if nah:
            Notification().notify(str(name), 'Download iniciado')
        else:
            Notification().notify(str(name), f'Download em {percent:.0f}', timeout=2, toast=True)


else:
    def notbar(name, percent, nah):
        if percent < 100:
            print(f'\033[36m{name}\n    \033[32m{percent:.0f}% completo')
        else:
            print(f'\033[mDownload de {name}\n      \033[33mCOMPLETO')
