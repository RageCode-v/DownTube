package com.ragecodev.downtube;

import android.content.Context;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import androidx.core.app.NotificationCompat;
import androidx.core.app.NotificationManagerCompat;
import android.app.Notification;
import com.ragecodev.downtube.R;
import android.os.Build;
import java.lang.Math;

public class Notify{
    public void iniciar(Context context, CharSequence name, int percent) {
        this.createChannelProgress(context);
        this.createChannelFinal(context);
        this.sendNotification(context, name, percent);
    }

    private void createChannelProgress(Context context) {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.N) {
            CharSequence name = "Downloads ativo";
            String desc = "Exibir progresso de download";
            int importance = NotificationManager.IMPORTANCE_DEFAULT;
            NotificationChannel channel = new NotificationChannel("DownActives", name, importance);
            channel.setDescription(desc);
            NotificationManager notificationManager = context.getSystemService(NotificationManager.class);
            notificationManager.createNotificationChannel(channel);
        }
    }

    private void createChannelFinal(Context context) {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.N) {
            CharSequence name = "Downloads completos";
            String desc = "Exibir o download após completo";
            int importance = NotificationManager.IMPORTANCE_DEFAULT;
            NotificationChannel channel = new NotificationChannel("CompleteDowns", name, importance);
            channel.setDescription(desc);
            NotificationManager notificationManager = context.getSystemService(NotificationManager.class);
            notificationManager.createNotificationChannel(channel);
        }
    }

    private void sendNotification(Context context, CharSequence name, int percent) {
        int notification_id = 618;

        NotificationCompat.Builder builder = new NotificationCompat.Builder(context, "DownActives");
        builder.setContentTitle(name)
                .setContentText(percent + "%")
                .setSmallIcon(R.drawable.ic_launcher)
                .setPriority(NotificationCompat.PRIORITY_LOW)
                .setCategory(NotificationCompat.CATEGORY_SERVICE)
                .setVisibility(NotificationCompat.VISIBILITY_PUBLIC);

        if (percent < 100) {
            builder.setProgress(100, percent, false);
        }
        else {
            builder.setProgress(0, 0, false);
            this.finalNotify(context, name);
        }
        NotificationManagerCompat notificationManager = NotificationManagerCompat.from(context);
        notificationManager.notify(notification_id, builder.build());
    }

    private void finalNotify(Context context, CharSequence name) {
        int notification_id = (int)(Math.random()*(8000-1+1)+1);

        NotificationCompat.Builder builder = new NotificationCompat.Builder(context, "CompleteDowns");
        builder.setContentTitle(name)
                .setContentText("Download concluído")
                .setSmallIcon(R.drawable.ic_launcher)
                .setPriority(NotificationCompat.PRIORITY_DEFAULT)
                .setCategory(NotificationCompat.CATEGORY_MESSAGE)
                .setVisibility(NotificationCompat.VISIBILITY_PUBLIC);

        NotificationManagerCompat notificationManager = NotificationManagerCompat.from(context);
        notificationManager.notify(notification_id, builder.build());
    }
}