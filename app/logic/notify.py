from kivy.utils import platform

if platform == 'android':
    from jnius import autoclass

    mActivity = autoclass('org.kivy.android.PythonActivity').mActivity

    context = mActivity.getApplicationContext()
    javacl = autoclass('com.ragecodev.downtube.Notify')
    notifyJ = javacl()

    notifyJ.createChannel(context)


    def notbar(name, percent):
        percent = int(percent)

        notifyJ.iniciar(context, name, percent)


else:
    def notbar(name, percent):
        if percent < 100:
            print(f'\033[36m{name}\n    \033[32m{percent:.0f}% completo')
        else:
            print(f'\033[mDownload de {name}\n      \033[33mCOMPLETO')
