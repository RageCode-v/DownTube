from kivy.utils import platform

if platform == 'android':
    from jnius import autoclass

    manager = autoclass('android.app.NotificationManager$notify')
    compat = autoclass('android.app.NotificationCompat')
    build = autoclass('android.app.Notification.Builder')
    channelpadrao = autoclass('android.app.NotificationChannel')
    builder = build(channelpadrao.DEFAULT_CHANNEL_ID)


    def notbar(name, percent, first):
        if first:
            builder.setContentTitle(str(name))
            builder.setContentText('Download em progresso')
            builder.setPriority(compat.PRIORITY_DEFAULT)
            builder.setProgress(100, 0, False)
            manager(618, builder.build())
        else:
            builder.setProgress(100, percent)
            manager(618, builder.build())
else:
    def notbar(name, percent, nah):
        if percent < 100:
            print(f'\033[36m{name}\n    \033[32m{percent:.0f}% completo')
        else:
            print(f'\033[mDownload de {name}\n      \033[33mCOMPLETO')
