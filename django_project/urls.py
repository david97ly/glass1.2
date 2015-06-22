from django.conf.urls import patterns, include, url
from django .conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'glass.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^servicios', 'glass.views.servicios', name='servicios'),
    url(r'^detalleservice', 'glass.views.detalleservice', name='detalleservice'),
    url(r'^contacto', 'glass.views.contacto', name='contacto'),
    url(r'^fotos', 'glass.views.fotos', name='fotos'),
    url(r'^quienes', 'glass.views.quienes', name='quienes'),
    url(r'^ubicacion', 'glass.views.ubicacion', name='ubicacion'),
    url(r'^login', 'glass.views.login', name='login'),
    url(r'^conf', 'glass.views.conf', name='conf'),
    url(r'^cfotos', 'glass.views.cfotos', name='cfotos'),
    url(r'^cservicios', 'glass.views.cservicios', name='cservicios'),
    url(r'^banner', 'glass.views.banner', name='banner'),
    url(r'^info', 'glass.views.info', name='info'),
    url(r'^ccontacto', 'glass.views.ccontacto', name='ccontacto'),
    url(r'^slideupdate/(\d+)$', 'glass.views.slideupdate', name='slideupdate'),

  #  url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':'/home/'}),
    
)

