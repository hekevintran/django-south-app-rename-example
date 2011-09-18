# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from old_app.migration_utils import get_app_name

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Something'
        db.create_table('old_app_something', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(get_app_name(), ['Something'])


    def backwards(self, orm):
        
        # Deleting model 'Something'
        db.delete_table('old_app_something')


    models = {
        'old_app.something': {
            'Meta': {'object_name': 'Something'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['old_app']
