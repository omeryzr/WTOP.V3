# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'After_Sale.orders'
        db.alter_column(u'member_after_sale', 'orders_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['kullanici.Orders'], unique=True))
        # Adding unique constraint on 'After_Sale', fields ['orders']
        db.create_unique(u'member_after_sale', ['orders_id'])


        # Changing field 'Orders.ship_to_user'
        db.alter_column(u'member_orders', 'ship_to_user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['kullanici.Member'], unique=True))
        # Adding unique constraint on 'Orders', fields ['ship_to_user']
        db.create_unique(u'member_orders', ['ship_to_user_id'])


        # Changing field 'Wallet.kullanici'
        db.alter_column(u'member_wallet', 'member_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['kullanici.Member'], unique=True))
        # Adding unique constraint on 'Wallet', fields ['kullanici']
        db.create_unique(u'member_wallet', ['member_id'])


        # Changing field 'On_Sales.category'
        db.alter_column(u'member_on_sales', 'category_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['kullanici.Category'], unique=True))
        # Adding unique constraint on 'On_Sales', fields ['category']
        db.create_unique(u'member_on_sales', ['category_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'On_Sales', fields ['category']
        db.delete_unique(u'member_on_sales', ['category_id'])

        # Removing unique constraint on 'Wallet', fields ['kullanici']
        db.delete_unique(u'member_wallet', ['member_id'])

        # Removing unique constraint on 'Orders', fields ['ship_to_user']
        db.delete_unique(u'member_orders', ['ship_to_user_id'])

        # Removing unique constraint on 'After_Sale', fields ['orders']
        db.delete_unique(u'member_after_sale', ['orders_id'])


        # Changing field 'After_Sale.orders'
        db.alter_column(u'member_after_sale', 'orders_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['kullanici.Orders']))

        # Changing field 'Orders.ship_to_user'
        db.alter_column(u'member_orders', 'ship_to_user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['kullanici.Member']))

        # Changing field 'Wallet.kullanici'
        db.alter_column(u'member_wallet', 'member_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['kullanici.Member']))

        # Changing field 'On_Sales.category'
        db.alter_column(u'member_on_sales', 'category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['kullanici.Category']))

    models = {
        u'kullanici.after_sale': {
            'Meta': {'object_name': 'After_Sale'},
            'cdate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orders': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['kullanici.Orders']", 'unique': 'True'}),
            'status': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'kullanici.category': {
            'Meta': {'object_name': 'Category'},
            'category_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'kullanici.city': {
            'Meta': {'object_name': 'City'},
            'city_name': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'kullanici.kullanici': {
            'Meta': {'object_name': 'Member'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'points': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'points_counter': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'kullanici.on_sales': {
            'Meta': {'object_name': 'On_Sales'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'amount_bitcoin': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'category': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['kullanici.Category']", 'unique': 'True'}),
            'cdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'edate': ('django.db.models.fields.DateTimeField', [], {}),
            'from_city': ('django.db.models.fields.related.ForeignKey', [], {'default': "'0'", 'to': u"orm['kullanici.City']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'kullanici': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['kullanici.Member']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'total_ticket': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'kullanici.orders': {
            'Meta': {'object_name': 'Orders'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'adress': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'cargo_company': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'cargo_no': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'cdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'on_sales': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['kullanici.On_Sales']"}),
            'ship_to_user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['kullanici.Member']", 'unique': 'True'}),
            'status': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'kullanici.wallet': {
            'Meta': {'object_name': 'Wallet'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kullanici': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['kullanici.Member']", 'unique': 'True'})
        }
    }

    complete_apps = ['kullanici']