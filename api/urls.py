from rest_framework.routers import DefaultRouter


from api import views

router=DefaultRouter()

router.register('v2/mobiles',views.MobileView,basename='mobiles')

for u in router.urls:
    print('----------',u,'---------')

urlpatterns = [
 
]+router.urls
