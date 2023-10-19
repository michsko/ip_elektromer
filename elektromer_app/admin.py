from django.contrib import admin
from .models import Svj
from .models import Customer
from .models import Chairman
from .models import Sub_chairman
from .models import Gsm_modul
from .models import Flat
from .models import Main_electrometer
from .models import Sub_electrometer
from .models import Solar_electrometer
from .models import Balance_main
from .models import Balance_sub
from .models import Balance_solar
from simple_history.admin import SimpleHistoryAdmin


# Register your models here.


admin.site.register(Svj,SimpleHistoryAdmin)
admin.site.register(Customer, SimpleHistoryAdmin)
admin.site.register(Chairman, SimpleHistoryAdmin)
admin.site.register(Sub_chairman, SimpleHistoryAdmin)
admin.site.register(Gsm_modul, SimpleHistoryAdmin)
admin.site.register(Flat, SimpleHistoryAdmin)
admin.site.register(Main_electrometer, SimpleHistoryAdmin)
admin.site.register(Sub_electrometer, SimpleHistoryAdmin)
admin.site.register(Solar_electrometer, SimpleHistoryAdmin)
admin.site.register(Balance_main, SimpleHistoryAdmin)
admin.site.register(Balance_sub, SimpleHistoryAdmin)
admin.site.register(Balance_solar, SimpleHistoryAdmin)



