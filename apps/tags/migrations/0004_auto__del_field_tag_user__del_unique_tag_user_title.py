# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Tag', fields ['user', 'title']
        db.delete_unique(u'tags_tag', ['user_id', 'title'])

        # Deleting field 'Tag.user'
        db.delete_column(u'tags_tag', 'user_id')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Tag.user'
        raise RuntimeError("Cannot reverse this migration. 'Tag.user' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Tag.user'
        db.add_column(u'tags_tag', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='tags', to=orm['auth.User']),
                      keep_default=False)

        # Adding unique constraint on 'Tag', fields ['user', 'title']
        db.create_unique(u'tags_tag', ['user_id', 'title'])


    models = {
        u'tags.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        }
    }

    complete_apps = ['tags']