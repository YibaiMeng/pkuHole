#! /usr/bin/python3
# This file is part of project pkuHole
# https://github.com/YibaiMeng/pkuHole
# Released to the Public Domain
# 
# Name: hole_consts.py
# Description: 
#    Constants of pkuHole.
#    Needs to be included in most of the files.

PROJECT_ROOT_DIR = "/home/mengyibai/Projects/pkuHole/"

STORAGE_DIR = {"image": PROJECT_ROOT_DIR + "image/", "audio" : PROJECT_ROOT_DIR + "audio/" }

DB_PATH = PROJECT_ROOT_DIR + "data.sqlite"

FIRST_VALID_POST = 32860

FIRST_NAMES = ["Alice","Bob","Carol","Dave","Eve","Francis","Grace","Hans","Isabella","Jason","Kate","Louis","Margaret","Nathan","Olivia","Paul","Queen","Richard","Susan","Thomas","Uma","Vivian","Winnie","Xander","Yasmine","Zach"]

SECOND_NAMES = ["Angry","Baby","Crazy","Diligent","Excited","Fat","Greedy","Hungry","Interesting","Japanese","Kind","Little","Magic","Naïve","Old","Powerful","Quiet","Rich","Superman","THU","Undefined","Valuable","Wifeless","Xiangbuchulai","Young","Zombie"]

hostname  = "www.pkuhelper.com"

# TODO: Need to check once in a while!
IPv4 = "162.105.205.61"

RESOURCE_END_POINT = {"image": "/services/pkuhole/images/", "audio" :  "/services/pkuhole/audios/" }
