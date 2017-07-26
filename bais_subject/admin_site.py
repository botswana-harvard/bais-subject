from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):
    site_title = 'Bais Subject'
    site_header = 'Bais Subject'
    index_title = 'Bais Subject'
    site_url = '/bais_subject/list/'


bais_subject_admin = AdminSite(name='bais_subject_admin')
