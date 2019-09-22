# !-*- coding: utf-8 -*-
# @Author  : ching(opencoding@hotmail.com)
# @Date    : 2019/03/16
# @Link    : http://www.cnblogs.com/ching126/
# @Version : $
# @Desc    :

import os
import uuid
import json
import datetime as dt
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def upload_image(req, dir_name):
    ##################
    # kindeditor图片上传返回数据格式说明：
    # {"error": 1, "message": "出错信息"}
    # {"error": 0, "url": "图片地址"}
    ##################
    result = {"error": 1, "message": "上传出错"}
    files = req.FILES.get("imgFile", None)
    dir_type = req.GET['dir']
    if files:
        result = process_upload(files, dir_type, dir_name)
    # 结果以json形式返回
    return HttpResponse(json.dumps(result), content_type="application/json")


def is_ext_allowed(dir_type, ext):
    """
    根据类型判断是否支持对应的扩展名
    :param type:
    :param ext:
    :return:
    """
    ext_allowed = {}
    ext_allowed['image'] = ['jpg','jpeg', 'bmp', 'gif', 'png']
    ext_allowed['flash'] = ["swf", "flv"]
    ext_allowed['media'] = ["swf", "flv", "mp3", "wav", "wma", "wmv", "mid", "avi", "mpg", "asf", "rm", "rmvb", "mp4"]
    ext_allowed['file'] = ["doc", "docx", "xls", "xlsx", "ppt", "htm", "html", "txt", "zip", "rar", "gz", "bz2", 'pdf']
    return ext in ext_allowed[dir_type]


# 目录创建
def get_relative_file_path(dir_name):
    """
    获取相对路径
    :param dir_name:
    :return:
    """
    today = dt.datetime.today()
    relative_path = dir_name + '/%s/%s/' % (str(today.year), today.strftime('%m'))
    absolute_path = os.path.join(settings.MEDIA_ROOT, relative_path)

    if not os.path.exists(absolute_path):
        os.makedirs(absolute_path)
    return relative_path


# def get_relative_file_path(dir_name):
#     """
#     获取相对路径
#     :return:
#     """
#     today = dt.datetime.today()
#     relative_path = dir_name + '/%s/%s/' % (today.year, today.month)
#     absolute_path = os.path.join(settings.MEDIA_ROOT, relative_path)
#
#     if not os.path.exists(absolute_path):
#         os.makedirs(absolute_path)
#     return relative_path


# 上传处理
def process_upload(files, dir_type, dir_name):
    dir_types = ['image', 'flash', 'media', 'file']
    # 允许上传文件类型
    if dir_type not in dir_types:
        return {"error":1, "message": u"上传类型不支持[必须是image,flash,media,file]"}

    file_suffix = files.name.split(".")[-1]
    # 判断是否支持对应的扩展名

    # allow_suffix = ['jpg', 'png', 'jpeg', 'gif', 'bmp']
    # if file_suffix not in allow_suffix:
    #     return {"error": 1, "message": "图片格式不正确"}

    if not is_ext_allowed(dir_type, file_suffix):
        return {'error': 1, 'message': u'error:类型不支持%s, 扩展名不支持%s' % (type, file_suffix)}

    relative_path = get_relative_file_path(dir_name)
    path = os.path.join(settings.MEDIA_ROOT, relative_path)

    # linux中一切皆文件
    file_name = str(uuid.uuid1()) + "." + file_suffix
    file_full_path = os.path.join(path, file_name).replace('\\', '/')  # windows中的路径以\分隔
    file_url = settings.MEDIA_URL + relative_path + file_name

    with open(file_full_path, 'wb') as f:
        if files.multiple_chunks() == False:  # 判断是否大于2.5M
            f.write(files.file.read())  # 保存
        else:
            for chunk in files.chunks():
                f.write(chunk)

    return {"error": 0, "url": file_url}
