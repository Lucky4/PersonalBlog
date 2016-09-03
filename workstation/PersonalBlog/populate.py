import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PersonalBlog.settings')

import django
django.setup()

from PersonalBlog_app.models import User, Post
import datetime


def populate():
    zp_user = add_user('ZhangPeng', '123456', '591398706@qq.com', 'no detail')
    add_post('my first blog', 'haha', 'test', user=zp_user)

    add_post('language', 'hello world', 'java,C++', user=zp_user)

    for u in User.objects.all():
        for p in Post.objects.filter(user=u):
            print "{0}-{1}".format(str(u), str(p))

def add_user(username, password, email, description):
    u = User.objects.get_or_create(username=username, password=password,
            email=email, description=description)[0]
    return u

def add_post(title, posts, tags, user):
    p = Post.objects.get_or_create(title=title, posts=posts, tags=tags,
            create_time=datetime.datetime.utcnow(),
            modify_time=datetime.datetime.utcnow(),
            user=user)[0]
    return p

if __name__ == '__main__':
    print "Starting population script..."
    populate()
