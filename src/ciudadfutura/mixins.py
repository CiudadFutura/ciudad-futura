from ciudadfutura.decorators import admin_required, staff_required


class StaffMixin(object):

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(StaffMixin, cls).as_view(**initkwargs)
        return staff_required(view)


class AdminMixin(object):

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(AdminMixin, cls).as_view(**initkwargs)
        return admin_required(view)
