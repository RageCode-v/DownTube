from kivy.utils import platform

if platform == 'android':
    from jnius import autoclass, cast
    from logic.exceptions import NotificationChannelFailed

    Apptivity = autoclass('org.kivy.android.PythonActivity').mActivity
    context = Apptivity.getApplicationContext()
    AndroidString = autoclass('java.lang.String')
    NotiManager = autoclass('android.app.NotificationManager')
    NotiChannel = autoclass('android.app.NotificationChannel')
    NotiCompat = autoclass('androidx.core.app.NotificationCompat')
    NotiComBuild = autoclass('androidx.core.app.NotificationCompat$Builder')
    NotiManCompat = autoclass('androidx.core.app.NotificationManagerCompat')
    func_from = getattr(NotiManCompat, 'from')
    channel_id = AndroidString('DownsOfTube')


    def channel_creator():
        name = cast('java.lang.CharSequence', AndroidString('DownTube downloads'))
        desc = AndroidString('Progresso de downloads do DownTube')
        importance = NotiManager.IMPORTANCE_DEFAULT

        channel = NotiChannel(channel_id, name, importance)
        channel.setDescription(desc)

        notimana = context.getSystemService(NotiManager)
        try:
            notimana.createNotificationChannel(channel)
        except Exception as erro:
            print(erro)
            raise NotificationChannelFailed


    def notbar(name, percent, first):
        builder = NotiComBuild(context, channel_id)
        if first:
            builder.setContentTitle(cast('java.lang.CharSequence', AndroidString(str(name))))
            builder.setContentText(cast('java.lang.CharSequence', AndroidString('Downloading')))
            builder.setSmallIcon(context.getApplicationInfo().icon)
            builder.setPriority(NotiCompat.PRIORITY_LOW)
            builder.setVisibility(NotiCompat.VISIBILITY_PUBLIC)
            builder.setProgress(cast('java.lang.Integer', int(100)), cast('java.lang.Integer', int(0)), cast(
                'java.lang.Boolean', bool(False)))
        else:
            builder.setProgress(cast('java.lang.Integer', int(100)), cast('java.lang.Integer', int(percent)), cast(
                'java.lang.Boolean', bool(False)))

        copatmana = NotiManCompat.func_from(context)
        copatmana.notify(str(name[:3]), builder.build())


else:
    def notbar(name, percent, nah):
        if percent < 100:
            print(f'\033[36m{name}\n    \033[32m{percent:.0f}% completo')
        else:
            print(f'\033[mDownload de {name}\n      \033[33mCOMPLETO')
