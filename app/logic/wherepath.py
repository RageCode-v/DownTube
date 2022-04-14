from kivy.utils import platform


def down_path():
    from os.path import join

    if platform == 'android':
        from android.permissions import request_permissions, Permission
        from android.storage import primary_external_storage_path

        request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
        path = join(primary_external_storage_path(), 'Download')
    else:
        path = 'E:\\TestDownTube'
    return path
