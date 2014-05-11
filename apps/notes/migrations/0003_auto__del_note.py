# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Note'
        db.delete_table(u'notes_note')


    def backwards(self, orm):
        # Adding model 'Note'
        db.create_table(u'notes_note', (
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=140, null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='notes', to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')(max_length=10000)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'notes', ['Note'])


    models = {
        
    }

    complete_apps = ['notes']