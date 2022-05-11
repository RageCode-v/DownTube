package com.ragecodev.downtube;

import android.content.Intent;
import android.content.Context;
import android.net.Uri;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import androidx.core.app.NotificationCompat;
import androidx.core.app.NotificationManagerCompat;
import android.app.Notification;
import com.ragecodev.downtube.R;
import android.os.Build;
import android.os.Environment;

public class Notify{
    public void iniciar(Context context, CharSequence name, int percent) {
        this.sendNotification(context, name, percent);
    }

    public void createChannel(Context context) {
        this.createChannelProgress(context);
    }

    private void createChannelProgress(Context context) {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.N) {
            CharSequence name = "Downloads ativo";
            String desc = "Exibir progresso de download";
            int importance = NotificationManager.IMPORTANCE_LOW;
            NotificationChannel channel = new NotificationChannel("DownActives", name, importance);
            channel.setDescription(desc);
            NotificationManager notificationManager = context.getSystemService(NotificationManager.class);
            notificationManager.createNotificationChannel(channel);
        }
    }

    private void sendNotification(Context context, Intent intent, CharSequence name, int percent) {
        int notification_id = 618;

        NotificationCompat.Builder builder = new NotificationCompat.Builder(context, "DownActives");
        builder.setContentTitle(name)
                .setContentText(percent + "%")
                .setSmallIcon(R.drawable.download)
                .setPriority(NotificationCompat.PRIORITY_LOW)
                .setCategory(NotificationCompat.CATEGORY_SERVICE)
                .setVisibility(NotificationCompat.VISIBILITY_PUBLIC)
                .setAutoCancel(true);

        if (percent < 100) {
            builder.setProgress(100, percent, false);
        }
        else {
            String path = Environment.getExternalStorageDirectory() + "/" + "Download" + "/" + name.toString();
            Uri uri = Uri.parse(path);
            Intent file = new Intent(Intent.ACTION_PICK);
            file.setDataAndType(uri, "*/*");

            builder.setProgress(0, 0, false);
            builder.setSmallIcon(R.drawable.check);
            builder.setLargeIcon(R.drawable.check);
            builder.setContentIntent(file);
        }
        NotificationManagerCompat notificationManager = NotificationManagerCompat.from(context);
        notificationManager.notify(notification_id, builder.build());
    }
}
