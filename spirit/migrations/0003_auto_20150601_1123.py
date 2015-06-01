# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spirit', '0002_auto_20150601_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='topic',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='commentbookmark',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='commentbookmark',
            name='topic',
        ),
        migrations.RemoveField(
            model_name='commentbookmark',
            name='user',
        ),
        migrations.DeleteModel(
            name='CommentBookmark',
        ),
        migrations.RemoveField(
            model_name='commentflag',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='commentflag',
            name='moderator',
        ),
        migrations.DeleteModel(
            name='CommentFlag',
        ),
        migrations.RemoveField(
            model_name='commenthistory',
            name='comment_fk',
        ),
        migrations.DeleteModel(
            name='CommentHistory',
        ),
        migrations.AlterUniqueTogether(
            name='commentlike',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='commentlike',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='commentlike',
            name='user',
        ),
        migrations.DeleteModel(
            name='CommentLike',
        ),
        migrations.AlterUniqueTogether(
            name='flag',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='flag',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='flag',
            name='user',
        ),
        migrations.DeleteModel(
            name='Flag',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='topicfavorite',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='topicfavorite',
            name='topic',
        ),
        migrations.RemoveField(
            model_name='topicfavorite',
            name='user',
        ),
        migrations.DeleteModel(
            name='TopicFavorite',
        ),
        migrations.AlterUniqueTogether(
            name='topicnotification',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='topicnotification',
            name='comment',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.RemoveField(
            model_name='topicnotification',
            name='topic',
        ),
        migrations.RemoveField(
            model_name='topicnotification',
            name='user',
        ),
        migrations.DeleteModel(
            name='TopicNotification',
        ),
        migrations.AlterUniqueTogether(
            name='topicprivate',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='topicprivate',
            name='topic',
        ),
        migrations.RemoveField(
            model_name='topicprivate',
            name='user',
        ),
        migrations.DeleteModel(
            name='TopicPrivate',
        ),
        migrations.AlterUniqueTogether(
            name='topicunread',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='topicunread',
            name='topic',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
        migrations.RemoveField(
            model_name='topicunread',
            name='user',
        ),
        migrations.DeleteModel(
            name='TopicUnread',
        ),
    ]
